"""Tests a simple parser"""

from __future__ import annotations

import optparse
import sys
from pathlib import Path
from typing import Any

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent.parent))
from cli2gui import Cli2Gui


def handle(args: tuple[Any, list[str]]) -> None:
	"""Handle the args."""
	print(args)


@Cli2Gui(run_function=handle, parser="optparse")
def cli() -> None:
	"""Cli entrypoint."""
	parser = optparse.OptionParser("Simple Parser")

	parser.add_option("--optional", help="optional arg")

	# Store true, false, store, count, choices
	parser.add_option("--store-true", action="store_true", help="optional arg store true")
	parser.add_option("--store-false", action="store_false", help="optional arg store false")
	parser.add_option("--store", action="store", help="optional arg store")
	parser.add_option("--count", action="count", help="optional arg count")
	parser.add_option(
		"--choices",
		action="store",
		choices=["choice1", "choice2"],
		help="optional arg store with choices",
	)

	args = parser.parse_args()

	handle(args)


cli()
