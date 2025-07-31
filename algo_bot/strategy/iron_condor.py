from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

from ..market.market_regime import MarketRegimeDetector

from ..config.config import StrategyConfig
from ..broker.base import Broker
from .base import Strategy


@dataclass
class IronCondorState:
    open_positions: list


class IronCondorStrategy(Strategy):
    """Iron Condor strategy stub."""

    def __init__(self, config: StrategyConfig, broker: Broker) -> None:
        self.config = config
        self.broker = broker
        self.state = IronCondorState(open_positions=[])
        self.regime_detector = MarketRegimeDetector()
        
    def generate_signals(self, market_data: Any) -> Any:
        regime = self.regime_detector.update(market_data)
        params: Dict[str, Any] = self.config.regimes.get(regime, {}) if self.config.regimes else {}
        target_delta = params.get("target_delta", self.config.target_delta)
        width = params.get("width", self.config.width)
        signal = {
            "type": "IRON_CONDOR",
            "regime": regime,
            "target_delta": target_delta,
            "width": width,
        }
        return signal

    def on_fill(self, fill: Any) -> None:
        self.state.open_positions.append(fill)
