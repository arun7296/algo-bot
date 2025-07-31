from __future__ import annotations
from ..broker.dummy_broker import DummyBroker
from ..data.market_data import MarketDataClient
from ..strategy.iron_condor import IronCondorStrategy
from ..config.config import Config
from ..risk.risk_manager import RiskManager
from ..utils.logging import get_logger

class Backtester:
    """Simple backtester stub."""

    def __init__(self, config: Config) -> None:
        self.config = config
        self.broker = DummyBroker()
        self.market_data = MarketDataClient()
        self.strategy = IronCondorStrategy(config.strategy, self.broker)
        self.risk = RiskManager(config.risk)
        self.logger = get_logger(__name__)

    def step(self) -> None:
        """Run a single backtest step."""
        data = self.market_data.get_latest("NIFTY")
        signal = self.strategy.generate_signals(data)
        self.logger.info("Generated signal %s", signal)
        if self.risk.check_risk(self.broker.positions()):
            order_id = self.broker.place_order(signal)
            self.strategy.on_fill({"id": order_id})
            self.logger.info("Positions: %s", self.broker.positions())
        else:
            self.logger.warning("Risk check failed. No order placed.")

    def run(self, steps: int = 1) -> None:
        """Run a backtest for a given number of steps."""
        for _ in range(steps):
            self.step()
