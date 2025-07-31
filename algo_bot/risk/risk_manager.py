from __future__ import annotations

from dataclasses import dataclass
from typing import Any, List

from ..config.config import RiskConfig


@dataclass
class RiskState:
    pnl: float = 0.0
    drawdown: float = 0.0


class RiskManager:
    """Basic risk manager stub."""

    def __init__(self, config: RiskConfig) -> None:
        self.config = config
        self.state = RiskState()

    def check_risk(self, positions: List[Any]) -> bool:
        # Placeholder risk checks
        return self.state.drawdown < self.config.max_drawdown
