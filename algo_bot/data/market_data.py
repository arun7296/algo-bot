from __future__ import annotations

from typing import Any


class MarketDataClient:
    """Placeholder market data client."""

    def get_latest(self, symbol: str) -> Any:
        return {
            "symbol": symbol,
            "price": 0.0,
        }
