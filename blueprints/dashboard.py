from flask import Blueprint, redirect, render_template, session, url_for

from database.auth_db import get_api_key_for_tradingview, get_auth_token
from database.settings_db import get_analyze_mode
from services.funds_service import get_funds
from utils.logging import get_logger
from utils.session import check_session_validity

logger = get_logger(__name__)

dashboard_bp = Blueprint("dashboard_bp", __name__, url_prefix="/")
scalper_process = None


@dashboard_bp.route("/dashboard")
@check_session_validity
def dashboard():
    login_username = session["user"]
    AUTH_TOKEN = get_auth_token(login_username)

    if AUTH_TOKEN is None:
        logger.warning(f"No auth token found for user {login_username}")
        return (
            render_template(
                "dashboard.html",
                margin_data={},
                error_message="Broker authentication expired. Please reconnect your broker.",
            ),
            200,
        )

    broker = session.get("broker")
    if not broker:
        logger.error("Broker not set in session")
        return "Broker not set in session", 400

    # Check if in analyze mode and route accordingly
    if get_analyze_mode():
        # Get API key for sandbox mode
        api_key = get_api_key_for_tradingview(login_username)
        if api_key:
            success, response, status_code = get_funds(api_key=api_key)
        else:
            logger.error("No API key found for analyze mode")
            return "API key required for analyze mode", 400
    else:
        # Use live broker
        success, response, status_code = get_funds(auth_token=AUTH_TOKEN, broker=broker)

    if not success:
        error_message = response.get("message", "Unknown error")
        logger.error(f"Failed to get funds data: {error_message}")
        if status_code == 404:
            error_message = "Failed to import broker module"
        if "Invalid_Authentication" in error_message:
            try:
                from database.auth_db import upsert_auth

                upsert_auth(login_username, "", broker, revoke=True)
                logger.warning(
                    f"Revoked broker token for user {login_username} due to invalid auth"
                )
                error_message = "Invalid authentication. Please reconnect your broker."
            except Exception as revoke_error:
                logger.exception(f"Failed to revoke broker token: {revoke_error}")
        return render_template("dashboard.html", margin_data={}, error_message=error_message), 200

    margin_data = response.get("data", {})

    # Check if margin_data is empty (authentication failed)
    if not margin_data:
        logger.error(
            f"Failed to get margin data for user {login_username} - authentication may have expired"
        )
        return (
            render_template(
                "dashboard.html",
                margin_data={},
                error_message="Failed to load margin data. Please reconnect your broker.",
            ),
            200,
        )

    # Check if all values are zero (but don't log warning during known service hours)
    if (
        margin_data.get("availablecash") == "0.00"
        and margin_data.get("collateral") == "0.00"
        and margin_data.get("utiliseddebits") == "0.00"
    ):
        # This could be service hours or authentication issue
        # The service already logs the appropriate message
        logger.debug(f"All margin data values are zero for user {login_username}")

    return render_template("dashboard.html", margin_data=margin_data, error_message=None)
