import os

import jwt
from dhanhq import dhanhq as Dhan

from utils.logging import get_logger

logger = get_logger(__name__)


def _resolve_dhan_client_id(auth_token: str) -> str:
    """
    Resolve Dhan client ID using the most reliable source first.

    Priority:
    1. JWT claim `dhanClientId` from the live access token
    2. `BROKER_API_KEY` prefix in `client_id:::app_id` format
    """
    try:
        decoded = jwt.decode(auth_token, options={"verify_signature": False})
        token_client_id = decoded.get("dhanClientId")
        if token_client_id:
            return str(token_client_id)
    except Exception as err:
        logger.debug(f"Unable to parse Dhan client ID from token: {err}")

    broker_key = os.getenv("BROKER_API_KEY", "")
    if ":::" in broker_key:
        env_client_id = broker_key.split(":::", 1)[0].strip()
        if env_client_id:
            return env_client_id

    return ""


def test_auth_token(auth_token):
    """Test if the auth token is valid using DhanHQ library."""
    try:
        client_id = _resolve_dhan_client_id(auth_token)
        if not client_id:
            return False, "Client ID not found in configuration"

        dhan_client = Dhan(client_id, auth_token)

        response = dhan_client.get_fund_limits()

        if response.get("status") == "success":
            return True, None
        return False, response.get("remarks", "Unknown error")

    except Exception as e:
        logger.error(f"Error testing auth token with DhanHQ: {str(e)}")
        return False, f"Error validating authentication: {str(e)}"


def get_margin_data(auth_token):
    """Fetch margin data using DhanHQ library."""
    try:
        client_id = _resolve_dhan_client_id(auth_token)

        if not client_id:
            logger.error("Client ID not found in Dhan token or BROKER_API_KEY")
            return {"errorType": "ConfigError", "errorMessage": "Client ID configuration missing"}

        dhan_client = Dhan(client_id, auth_token)

        margin_response = dhan_client.get_fund_limits()
        logger.info(f"DhanHQ Funds Response: {margin_response}")

        if margin_response.get("status") != "success":
            error_msg = margin_response.get("remarks", "Unknown error")
            if "unauthorized" in str(error_msg).lower() or "invalid" in str(error_msg).lower():
                return {"errorType": "Invalid_Authentication", "errorMessage": error_msg}
            return {"errorType": "FundsError", "errorMessage": str(error_msg)}

        data = margin_response.get("data", {})

        try:
            pos_response = dhan_client.get_positions()
            logger.info(f"DhanHQ Positions Response: {pos_response}")
            position_book = pos_response.get("data", [])
        except Exception as e:
            logger.error(f"Error fetching positions: {e}")
            position_book = []

        total_realised = 0
        total_unrealised = 0

        if isinstance(position_book, list):
            total_realised = sum(float(p.get("realizedProfit", 0)) for p in position_book)
            total_unrealised = sum(float(p.get("unrealizedProfit", 0)) for p in position_book)

        processed_margin_data = {
            "availablecash": "{:.2f}".format(
                float(data.get("availabelBalance", data.get("availableBalance", 0)))
            ),
            "collateral": "{:.2f}".format(float(data.get("collateralAmount", 0))),
            "m2munrealized": "{:.2f}".format(total_unrealised),
            "m2mrealized": "{:.2f}".format(total_realised),
            "utiliseddebits": "{:.2f}".format(float(data.get("utilizedAmount", 0))),
        }

        return processed_margin_data

    except Exception as e:
        logger.error(f"Error in get_margin_data (DhanHQ): {e}")
        return {"errorType": "Exception", "errorMessage": str(e)}
