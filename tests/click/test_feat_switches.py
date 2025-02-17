"""Program from https://click.palletsprojects.com/en/8.1.x/"""

from __future__ import annotations

import sys
from pathlib import Path

import click

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent.parent))
import sys

from cli2gui import Click2Gui


@click.command()
@click.option("--upper", "transformation", flag_value="upper", default=True)
@click.option("--lower", "transformation", flag_value="lower")
def info(transformation) -> None:
	click.echo(getattr(sys.platform, transformation)())


Click2Gui(run_function=info)
