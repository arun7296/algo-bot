from __future__ import annotations

from typing import Any, Dict, List

from .base import Broker


class DummyBroker(Broker):
    """Simple broker for backtesting or dry-run."""

    def __init__(self) -> None:
        self._orders: List[Dict[str, Any]] = []

    def place_order(self, order: Dict[str, Any]) -> str:
        order_id = f"order_{len(self._orders)+1}"
        order["id"] = order_id
        self._orders.append(order)
        return order_id

    def cancel_order(self, order_id: str) -> None:
        self._orders = [o for o in self._orders if o.get("id") != order_id]

    def positions(self) -> List[Dict[str, Any]]:
        return self._orders
