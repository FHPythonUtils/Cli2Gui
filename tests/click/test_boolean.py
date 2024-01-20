"""Tests a simple parser

Program from https://click.palletsprojects.com/en/7.x/#documentation
"""

from __future__ import annotations

import sys
from pathlib import Path

import click

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent.parent))
from cli2gui import Click2Gui


@click.command()
@click.option("--print-version", default=True, help="Print the version?")
def hello(*, print_version: bool) -> None:
	if print_version:
		print("v1.0")


Click2Gui(run_function=hello)
# hello()
