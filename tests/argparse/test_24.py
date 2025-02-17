"""Tests an advanced parser"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

THISDIR = Path(__file__).resolve().parent
sys.path.insert(0, str(THISDIR.parent.parent))
from cli2gui import Cli2Gui


def handle(args: argparse.Namespace) -> None:
	"""Handle the args."""
	print(args)
	try:
		args.write_path.write_bytes(b"test")
	except AttributeError:
		print("Oops! write_path was never specified")


@Cli2Gui(
	run_function=handle,
	menu={
		"File": f"{THISDIR}/file.md",
		"Another File": f"{THISDIR}/another_file.md",
	},
	gui="freesimplegui",
)
def cli() -> None:
	"""Cli entrypoint."""
	parser = argparse.ArgumentParser("Simple Parser")

	# Positional and file
	parser.add_argument("positional", help="positional arg")
	parser.add_argument(
		"positional_file", type=argparse.FileType("r"), help="positional arg for a file"
	)
	parser.add_argument(
		"write_file", type=argparse.FileType("wb"), help="positional arg for a file"
	)

	parser.add_argument("write_path", type=Path, help="positional arg for a file")

	args = parser.parse_args()

	handle(args)


cli()
