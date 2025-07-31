import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # noqa: E402
from algo_bot.strategy.iron_condor import IronCondorStrategy  # noqa: E402
from algo_bot.config.config import StrategyConfig  # noqa: E402
from algo_bot.broker.dummy_broker import DummyBroker  # noqa: E402


def test_strategy_signal_generation():
    cfg = StrategyConfig(
        name="iron_condor",
        target_delta=0.25,
        width=50,
        regimes={"low": {"target_delta": 0.3, "width": 60}},
    )
    broker = DummyBroker()
    strat = IronCondorStrategy(cfg, broker)
    signal = strat.generate_signals({"vix": 10})
    assert signal["regime"] == "low"
    assert signal["target_delta"] == 0.3
    assert signal["width"] == 60
