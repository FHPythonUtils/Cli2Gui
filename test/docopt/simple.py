#!/usr/bin/env python3
"""
usage:
  simple.py [-h] [--optional OPTIONAL] [--store-true] [--store-false]
  [--store STORE] [--count] [--choices {choice1,choice2}] PATH

Arguments:
  PATH            positional arg

Options:
  -h, --help            show this help message and exit
  --optional OPTIONAL   optional arg
  --store-true          optional arg store true
  --store-false         optional arg store false
  --store STORE         optional arg store
  --count               optional arg count
  --choices {choice1,choice2}
                        optional arg store with choices

"""

import sys
import os
from pathlib import Path
THISDIR = str(Path(__file__).resolve().parent.parent)
sys.path.insert(0, os.path.dirname(THISDIR))

import docopt
from cli2gui import Cli2Gui

def handle(args):
	'''Handle the args '''
	print(args)

@Cli2Gui(run_function=handle, parser="docopt")
def cli():
	'''Cli entrypoint '''
	args = docopt.docopt(__doc__)
	handle(args)

cli()
