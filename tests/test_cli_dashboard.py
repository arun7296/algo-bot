import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # noqa: E402
from algo_bot.ui.cli_dashboard import CLIDashboard  # noqa: E402
from algo_bot.backtesting.backtester import Backtester  # noqa: E402
from algo_bot.config.config import parse_config, load_config  # noqa: E402


def test_dashboard_table(tmp_path):
    cfg_path = tmp_path / "cfg.yml"
    cfg_path.write_text(
        """
app:
  log_file: test.log
  log_level: INFO
broker:
  name: dummy
  api_key: key
  api_secret: secret
strategy:
  name: iron_condor
  target_delta: 0.2
  width: 100
risk:
  max_position_size: 10
  max_drawdown: 0.1
"""
    )
    data = load_config(cfg_path)
    cfg = parse_config(data)
    backtester = Backtester(cfg)
    dash = CLIDashboard(backtester)
    table = dash._create_table()
    assert table.row_count == 1
    assert len(table.columns) == 3
