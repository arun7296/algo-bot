from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class Strategy(ABC):
    """Base class for strategies."""

    @abstractmethod
    def generate_signals(self, market_data: Any) -> Any:
        """Generate trading signals."""

    @abstractmethod
    def on_fill(self, fill: Any) -> None:
        """Handle order fills."""
