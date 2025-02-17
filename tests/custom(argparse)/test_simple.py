"""Tests a simple parser"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent.parent))
from cli2gui import Cli2Gui


def handle(args: argparse.Namespace) -> None:
	"""Handle the args."""
	print(args)


@Cli2Gui(parser="input()", run_function=handle)
def cli() -> None:
	"""Cli entrypoint."""
	parser = argparse.ArgumentParser("Simple Parser")

	# Positional and file
	parser.add_argument("positional", help="positional arg")
	parser.add_argument(
		"positional-file", type=argparse.FileType("r"), help="positional arg for a file"
	)
	parser.add_argument("--optional", help="optional arg")

	# Store true, false, store, count, choices
	parser.add_argument("--store-true", action="store_true", help="optional arg store true")
	parser.add_argument("--store-false", action="store_false", help="optional arg store false")
	parser.add_argument("--store", action="store", help="optional arg store")
	parser.add_argument("--count", action="count", help="optional arg count")
	parser.add_argument(
		"--choices",
		action="store",
		choices=["choice1", "choice2"],
		help="optional arg store with choices",
	)

	args = parser.parse_args()

	handle(args)


cli()
