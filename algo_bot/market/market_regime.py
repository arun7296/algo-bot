from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass
class RegimeThresholds:
    low: float = 15.0
    normal: float = 25.0
    high: float = 35.0


def detect_regime(vix: float, thresholds: RegimeThresholds | None = None) -> str:
    """Return market regime string given VIX value."""
    th = thresholds or RegimeThresholds()
    if vix < th.low:
        return "low"
    if vix < th.normal:
        return "normal"
    if vix < th.high:
        return "high"
    return "extreme"


class MarketRegimeDetector:
    """Very simple regime detector based on VIX only."""

    def __init__(self, thresholds: RegimeThresholds | None = None) -> None:
        self.thresholds = thresholds or RegimeThresholds()
        self.current = "normal"

    def update(self, market_data: Dict[str, float]) -> str:
        """Update regime based on latest market data."""
        vix = market_data.get("vix", 20.0)
        self.current = detect_regime(vix, self.thresholds)
        return self.current
