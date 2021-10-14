#!/usr/bin/env python3
"""Tests a simple parser
"""

import getopt
import sys
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent.parent))
from cli2gui import Cli2Gui


def handle(args):
	"""Handle the args."""
	print(args)


@Cli2Gui(run_function=handle, parser="getopt")
def cli():
	"""Cli entrypoint."""
	options = getopt.getopt(
		sys.argv[1:],
		"ts:c:o",
		[
			"store-true",
			"store=",
			"count=",
			"choice=",
		],
	)
	handle(options)


cli()
