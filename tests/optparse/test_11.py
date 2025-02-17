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
	print(type(args))
	print(args)
	print(type(args[0]))
	print(args[0])
	print(args[1])


@Cli2Gui(run_function=handle, parser="optparse")
def cli() -> None:
	"""Cli entrypoint."""
	parser = optparse.OptionParser("Simple Parser")

	parser.add_option("--optional", help="optional arg")

	# Store true, false, store, count, choices
	parser.add_option(
		"--store-true", action="store_true", help="optional arg store true", default=True
	)
	parser.add_option(
		"--store-false", action="store_false", help="optional arg store false", default=True
	)
	parser.add_option("--store", action="store", help="optional arg store", default="store me")
	parser.add_option("--count", action="count", help="optional arg count", default=1)
	parser.add_option(
		"--choices",
		action="store",
		choices=["choice1", "choice2"],
		help="optional arg store with choices",
	)

	args = parser.parse_args()

	handle(args)


cli()
