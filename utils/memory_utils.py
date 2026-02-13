import os
import asyncio
from typing import List, Dict, Any, Optional

try:
    import cognee
    from cognee.api.v1.add import add
    from cognee.api.v1.search import search
    from cognee.modules.search.types import SearchType
    # Configure cognee - using a local directory for storage by default
    # You might need to set environmental variables for vector store if not using default
except ImportError:
    cognee = None
    print("Warning: cognee not found. Memory features will be disabled.")


class CogneeManager:
    """
    Manages interactions with the Cognee memory library.
    Provides methods to add trade reasoning and search for past context.
    """

    def __init__(self, user_id: str = "default_user"):
        self.user_id = user_id
        self.enabled = cognee is not None
        if self.enabled:
            # Initialize any cognee specific setup if required
            pass

    async def add_memory(self, text: str, dataset_name: str = "trade_history"):
        """
        Add a piece of text to the memory graph.

        Args:
            text: The text content to remember (e.g., "Bought NIFTY because RSI < 30").
            dataset_name: Grouping for the memory.
        """
        if not self.enabled:
            return

        try:
            # Cognee 'add' typically takes data and processes it.
            # Depending on version, signature might vary. Using general v1 pattern.
            await add(
                data=text,
                dataset_name=dataset_name,
            )
            print(f"Memory added: {text[:50]}...")
        except Exception as e:
            print(f"Error adding to memory: {e}")

    async def search_memory(self, query: str, search_type: str = "SIMILARITY") -> List[Any]:
        """
        Search for relevant info in memory.

        Args:
            query: The question or topic to search for.
            search_type: Type of search (SIMILARITY, GRAPH, etc. dependent on cognee support).

        Returns:
            List of search results.
        """
        if not self.enabled:
            return []

        try:
            # Mapping string to enum if needed, or passing directly
            # Assuming search returns a list of results
            results = await search(query_text=query, search_type=SearchType.SIMILARITY)
            return results
        except Exception as e:
            print(f"Error searching memory: {e}")
            return []

    async def get_trading_context(self, symbol: str, current_indicators: Dict[str, Any]) -> str:
        """
        Constructs a query based on current state to find relevant past trades.
        """
        if not self.enabled:
            return "Memory disabled."

        # Example: "NIFTY RSI 25.5"
        query = f"{symbol}"
        for k, v in current_indicators.items():
            query += f" {k} {v}"

        results = await self.search_memory(query)

        # Format results into a generic string context
        if not results:
            return "No relevant past context found."

        return f"Found {len(results)} relevant past notes: {str(results)}"
