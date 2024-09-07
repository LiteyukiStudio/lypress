"""
Module docs
"""
from typing import Literal

from pydantic import BaseModel


class Config(BaseModel):
    """
    Config model
    """
    output: str = ".dist"
    """output folder"""

    langs: list[str] = ["en", "zh"]
    """languages, you can add more languages"""

    index_filename: str = "index"
    """index filename for __init__.py, in vitepress, it will be index.md, in vuepress, it will be README.md"""

    style: Literal["google", "numpy", "rst"] = "google"
    """document style"""


def load_config():
    """
    Load config from file
    """
    pass
