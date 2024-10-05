"""Generate a dict describing optparse arguments."""

from __future__ import annotations

import contextlib
from typing import Any, Generator

from cli2gui.types import Group, Item, ItemType, ParserRep


def extract(parser: Any) -> list[Group]:
	"""Get the actions as json for the parser."""
	try:
		argumentList = [
			Group(
				name="Positional Arguments",
				arg_items=list(categorize([parser.commands[key] for key in parser.commands])),
				groups=[],
			)
		]
	except AttributeError:
		argumentList: list[Group] = []
	argumentList.append(
		Group(name="Optional Arguments", arg_items=list(categorize(parser.params)), groups=[])
	)
	return argumentList


def actionToJson(action: Any, widget: ItemType, other: dict | None = None) -> Item:
	"""Generate json for an action and set the widget - used by the application."""
	nargs = ""
	with contextlib.suppress(AttributeError):
		nargs = action.params[0].nargs if len(action.params) > 0 else "" or ""

	commands = action.opts + action.secondary_opts
	return Item(
		type=widget,
		display_name=action.name,
		help=action.help,
		commands=commands,
		dest=action.callback or commands[0],
		default=action.default,
		additional_properties={"nargs": nargs, **(other or {})},
	)


def categorize(actions: list[Any]) -> Generator[Item, None, None]:
	"""Catergorise each action and generate json."""
	import click

	for action in actions:
		if isinstance(action.type, click.Choice):
			yield actionToJson(action, ItemType.Choice, {"choices": action.type.choices})
		elif isinstance(action.type, click.types.IntParamType):
			yield actionToJson(action, ItemType.Int)
		elif isinstance(action.type, click.types.FloatParamType):
			yield actionToJson(action, ItemType.Float)
		elif isinstance(action.type, click.types.BoolParamType):
			yield actionToJson(action, ItemType.Bool)
		elif isinstance(action.type, click.types.Path):
			yield actionToJson(action, ItemType.Path)
		else:
			yield actionToJson(action, ItemType.Text)


def convert(parser: Any) -> ParserRep:
	"""Convert click to a dict.

	Args:
	----
		parser (click.core.Command): click parser

	Returns:
	-------
		ParserRep: dictionary representing parser object

	"""
	return ParserRep(parser_description="", widgets=extract(parser))
