"""Types for cli2gui.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from enum import Enum
from typing import Any, TypedDict

# pylint: disable=invalid-name


@dataclass
class BuildSpec(TypedDict):
	"""Representation for the BuildSpec."""

	run_function: Callable[..., Any] | None
	parser: str | ParserType
	gui: str | GUIType
	theme: str | list[str] | None
	darkTheme: str | list[str] | None
	sizes: dict[str, Any] | None
	image: str | None
	program_name: str | None
	program_description: str | None
	max_args_shown: int
	menu: dict[str, Any] | None


@dataclass
class Item(TypedDict):
	"""Representation for an arg_item."""

	type: str
	display_name: str
	help: str
	commands: list[str]
	choices: list[str]
	dest: str
	_other: dict[str, Any]


@dataclass
class Group(TypedDict):
	"""Representation for an argument group."""

	name: str
	arg_items: list[Item]
	groups: list[Group] | list[Any]


@dataclass
class ParserRep(TypedDict):
	"""Representation for a parser."""

	parser_description: str | None
	widgets: list[Group]


@dataclass
class FullBuildSpec(TypedDict):
	"""Representation for the FullBuildSpec (BuildSpec + ParserRep)."""

	run_function: Callable[..., Any] | None
	parser: str
	gui: str
	theme: str | list[str] | None
	darkTheme: str | list[str] | None
	sizes: dict[str, Any] | None
	image: str | None
	program_name: str | None
	program_description: str | None
	max_args_shown: int
	menu: dict[str, Any] | None
	parser_description: str
	widgets: list[Group]


# Supported parser types
class ParserType(str, Enum):
	"""Supported parser types.

	OPTPARSE = "optparse"
	ARGPARSE = "argparse"
	DEPHELL_ARGPARSE = "dephell_argparse"
	DOCOPT = "docopt"
	GETOPT = "getopt"
	CLICK = "click"
	CUSTOM = "input()"  # this seems like a pretty poor pattern to use
	"""

	OPTPARSE = "optparse"
	ARGPARSE = "argparse"
	DEPHELL_ARGPARSE = "dephell_argparse"
	DOCOPT = "docopt"
	GETOPT = "getopt"
	CLICK = "click"
	CUSTOM = "input()"  # this seems like a pretty poor pattern to use


# Supported gui types
class GUIType(str, Enum):
	"""Supported gui types.

	DEFAULT = "pysimplegui"
	WEB = "pysimpleguiweb"
	QT = "pysimpleguiqt"
	"""

	DEFAULT = "pysimplegui"
	WEB = "pysimpleguiweb"
	QT = "pysimpleguiqt"
