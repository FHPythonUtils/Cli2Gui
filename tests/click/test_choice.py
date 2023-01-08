"""Program from https://click.palletsprojects.com/en/8.1.x/
"""

from __future__ import annotations

import sys
from pathlib import Path

import click

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent.parent))
from cli2gui import Click2Gui


@click.command()
@click.option("--hash-type", type=click.Choice(["MD5", "SHA1"], case_sensitive=False))
def digest(hash_type):
	click.echo(hash_type)


Click2Gui(run_function=digest)
