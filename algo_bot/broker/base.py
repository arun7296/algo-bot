from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict


class Broker(ABC):
    """Abstract broker interface."""

    @abstractmethod
    def place_order(self, order: Dict[str, Any]) -> str:
        """Place an order and return order id."""

    @abstractmethod
    def cancel_order(self, order_id: str) -> None:
        """Cancel a given order."""

    @abstractmethod
    def positions(self) -> Any:
        """Return current positions."""
