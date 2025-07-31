import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from algo_bot.config.config import load_config, parse_config, apply_overrides


def test_load_config(tmp_path):
    cfg_path = tmp_path / "test.yml"
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
  regimes:
    low:
      target_delta: 0.25
      width: 150
risk:
  max_position_size: 10
  max_drawdown: 0.1
"""
    )
    data = load_config(cfg_path)
    cfg = parse_config(data)
    assert cfg.app.log_file == "test.log"
    assert cfg.strategy.target_delta == 0.2
    assert "low" in cfg.strategy.regimes


def test_apply_overrides(tmp_path):
    cfg_path = tmp_path / "test.yml"
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
  regimes:
    low:
      target_delta: 0.25
      width: 150
risk:
  max_position_size: 10
  max_drawdown: 0.1
"""
    )
    data = load_config(cfg_path)
    data = apply_overrides(data, [
        "strategy.target_delta=0.3",
        "app.log_level=DEBUG",
        "strategy.regimes.low.width=200",
    ])
    cfg = parse_config(data)
    assert cfg.strategy.target_delta == 0.3
    assert cfg.app.log_level == "DEBUG"
    assert cfg.strategy.regimes["low"]["width"] == 200
