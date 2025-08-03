from __future__ import annotations

import argparse
from pathlib import Path

from algo_bot.config.config import load_config, parse_config, apply_overrides
from algo_bot.utils.logging import setup_logging
from algo_bot.backtesting.backtester import Backtester
from algo_bot.ui.cli_dashboard import CLIDashboard


def main() -> None:
    parser = argparse.ArgumentParser(description="Iron Condor Bot")
    parser.add_argument("--config", default="configs/default.yml")
    parser.add_argument(
        "--override",
        action="append",
        default=[],
        help=(
            "Override config values, e.g. "
            "--override strategy.target_delta=0.3"
        ),
    )
    parser.add_argument(
        "--cli-dashboard",
        action="store_true",
        help="Run with CLI dashboard",
    )
    args = parser.parse_args()

    raw_cfg = load_config(Path(args.config))
    raw_cfg = apply_overrides(raw_cfg, args.override)
    cfg = parse_config(raw_cfg)

    setup_logging(cfg.app.log_file)

    backtester = Backtester(cfg)
    if args.cli_dashboard:
        dashboard = CLIDashboard(backtester)
        dashboard.run(steps=5)
    else:
        backtester.run()


if __name__ == "__main__":
    main()
