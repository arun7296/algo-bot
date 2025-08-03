from __future__ import annotations

from time import sleep

from rich.live import Live
from rich.table import Table

from ..backtesting.backtester import Backtester


class CLIDashboard:
    """Simple CLI dashboard using rich tables."""

    def __init__(self, backtester: Backtester) -> None:
        self.backtester = backtester

    def _create_table(self) -> Table:
        table = Table(title="Iron Condor Bot")
        table.add_column("Regime")
        table.add_column("Positions")
        table.add_column("Drawdown")
        regime = self.backtester.strategy.regime_detector.current
        positions = str(len(self.backtester.broker.positions()))
        drawdown = f"{self.backtester.risk.state.drawdown:.2%}"
        table.add_row(regime, positions, drawdown)
        return table

    def run(self, steps: int = 1, interval: float = 1.0) -> None:
        """Run the dashboard, stepping the backtester and updating output."""
        with Live(self._create_table(), refresh_per_second=4) as live:
            for _ in range(steps):
                self.backtester.step()
                live.update(self._create_table())
                sleep(interval)
