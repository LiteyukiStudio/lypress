"""
Entry of litepress cli
"""

import argparse
import sys
import os

from litepress.log import logger

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LitePress CLI Parser")
    subparsers = parser.add_subparsers(description="Subcommands", dest="subcommand")

    parser_gencfg = subparsers.add_parser("gencfg", help="Generate a default config file for LitePress.")
    parser_build = subparsers.add_parser("build", help="Build the documentation.")
    parser_dev = subparsers.add_parser("dev", help="Start a watchdog for development.")

    parser.add_argument("path", type=str, help="Required: Path to the Python module or package.")
    parser.add_argument("-o", "--output", default=".dist", type=str, help="Optional: Output directory.")
    parser.add_argument("-c", "--config", default=None, type=str, help="Optional: Config file.")

    args = parser.parse_args()

    if config := args.config:
        if not os.path.exists(config):
            logger.error(f"Config file {config} does not exist. Skip.")
