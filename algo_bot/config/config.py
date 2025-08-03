from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List

import yaml


def _env_interpolate(value: str) -> str:
    """Replace ${VAR:-default} patterns with environment values."""
    if not isinstance(value, str):
        return value
    while "${" in value:
        start = value.find("${")
        end = value.find("}", start)
        if start == -1 or end == -1:
            break
        expr = value[start + 2:end]
        if ':-' in expr:
            var, default = expr.split(':-', 1)
        else:
            var, default = expr, ''
        repl = os.getenv(var, default)
        value = value[:start] + repl + value[end + 1:]
    return value


def load_config(path: str | Path) -> Dict[str, Any]:
    with open(path, "r") as f:
        data = yaml.safe_load(f)

    def recurse(obj):
        if isinstance(obj, dict):
            return {k: recurse(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [recurse(v) for v in obj]
        else:
            return _env_interpolate(obj)
    return recurse(data)


def apply_overrides(
    data: Dict[str, Any],
    overrides: List[str],
) -> Dict[str, Any]:
    """Apply CLI key=value overrides to the loaded config dict."""
    for item in overrides:
        if "=" not in item:
            continue
        key, value = item.split("=", 1)
        current = data
        parts = key.split(".")
        for p in parts[:-1]:
            current = current.setdefault(p, {})
        current[parts[-1]] = yaml.safe_load(value)
    return data


@dataclass
class AppConfig:
    log_file: str
    log_level: str


@dataclass
class BrokerConfig:
    name: str
    api_key: str
    api_secret: str


@dataclass
class StrategyConfig:
    name: str
    target_delta: float
    width: int
    regimes: Dict[str, Dict[str, Any]] | None = None


@dataclass
class RiskConfig:
    max_position_size: int
    max_drawdown: float


@dataclass
class Config:
    app: AppConfig
    broker: BrokerConfig
    strategy: StrategyConfig
    risk: RiskConfig


def parse_config(data: Dict[str, Any]) -> Config:
    return Config(
        app=AppConfig(**data["app"]),
        broker=BrokerConfig(**data["broker"]),
        strategy=StrategyConfig(**data.get("strategy", {})),
        risk=RiskConfig(**data["risk"]),
    )
