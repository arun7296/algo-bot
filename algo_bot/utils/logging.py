import logging
from logging.handlers import RotatingFileHandler
from typing import Optional


def setup_logging(
    log_file: str = "algo_bot.log",
    level: int = logging.INFO,
) -> None:
    """Configure root logger with console and rotating file handler."""
    logger = logging.getLogger()
    logger.setLevel(level)
    formatter = logging.Formatter(
        fmt="%(asctime)s %(levelname)s [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    if log_file:
        fh = RotatingFileHandler(log_file, maxBytes=1_000_000, backupCount=3)
        fh.setFormatter(formatter)
        logger.addHandler(fh)


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """Return a logger with the given name."""
    return logging.getLogger(name)
