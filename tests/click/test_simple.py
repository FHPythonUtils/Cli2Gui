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
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(count, name):
	"""Simple program that greets NAME for a total of COUNT times."""
	for _index in range(count):
		click.echo("Hello %s!" % name)


Click2Gui(run_function=hello)
# ⬇️ This is how you call the function without a GUI
# hello()
