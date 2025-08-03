# Iron Condor Bot

This repository contains a minimal scaffold of an Iron Condor options trading bot for
Indian markets. It is designed to be modular and extensible. All parameters are
configured via YAML files with environment variable interpolation.

## Structure

- `algo_bot/` – core library modules
- `configs/` – example configuration files
- `tests/` – pytest based unit tests
- `main.py` – entry point for running the bot or backtests

## Quick Start

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the backtester:
   ```bash
   python main.py --config configs/default.yml
   ```
   You can override any configuration value from the command line:
   ```bash
   python main.py --config configs/default.yml \
       --override strategy.target_delta=0.3 \
       --override app.log_level=DEBUG
   ```
3. Run tests:
 ```bash
  pytest
  ```

### CLI Dashboard

Run the backtester with an interactive CLI dashboard using `rich`:

```bash
python main.py --config configs/default.yml --cli-dashboard
```

This project is a starting point and does not contain real trading logic. It
illustrates how the modules interact and where advanced features should be
implemented.

### Market Regime Detection

The strategy now includes a basic market regime detector driven by VIX levels.
The detector selects between `low`, `normal`, `high`, and `extreme` regimes and
adapts strike parameters accordingly. Regime specific settings can be provided
under `strategy.regimes` in the YAML config.
