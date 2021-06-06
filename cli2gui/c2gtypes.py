"""Types for cli2gui.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any, TypedDict


class BuildSpec(TypedDict):
	"""Representation for the BuildSpec."""

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


class Item(TypedDict):
	"""Representation for an arg_item."""

	type: str
	display_name: str
	help: str
	commands: list[str]
	choices: list[str]
	dest: str
	_other: dict[str, Any]


class Group(TypedDict):
	"""Representation for an argument group."""

	name: str
	arg_items: list[Item]
	groups: list[Group] | list[Any]


class ParserRep(TypedDict):
	"""Representation for a parser."""

	parser_description: str | None
	widgets: list[Group]


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
