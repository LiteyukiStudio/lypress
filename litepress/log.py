"""
日志模块
"""
import sys
import loguru

logger = loguru.logger

# DEBUG日志格式
debug_format: str = (
        "<c>{time:MM-DD HH:mm:ss}</c> "
        "<lvl>[{level.icon}]</lvl> "
        "<c><{name}.{module}.{function}:{line}></c> "
        "{message}"
)

default_format: str = (
        "<c>{time:MM-DD HH:mm:ss}</c> "
        "<lvl>[{level.icon}]</lvl> "
        "<c><{name}></c> "
        "{message}"
)

def get_format(level: str) -> str:
    if level == "DEBUG":
        return debug_format
    else:
        return default_format


logger.remove()
logger.add(
    sys.stdout,
    level=0,
    diagnose=False,
    format=get_format("DEBUG"),
)
