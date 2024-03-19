"""Generate a dict describing optparse arguments."""

from __future__ import annotations

import contextlib
from typing import Any, Generator

from cli2gui import types


def extract(parser: Any) -> list[types.Group]:
	"""Get the actions as json for the parser."""
	try:
		argumentList = [
			{
				"name": "Positional Arguments",
				"arg_items": list(categorize([parser.commands[key] for key in parser.commands])),
				"groups": [],
			}
		]
	except AttributeError:
		argumentList: list[types.Group] = []
	argumentList.append(
		{
			"name": "Optional Arguments",
			"arg_items": list(categorize(parser.params)),
			"groups": [],
		}
	)
	return argumentList


def actionToJson(action: Any, widget: types.ItemType, other: dict | None = None) -> types.Item:
	"""Generate json for an action and set the widget - used by the application."""
	nargs = ""
	with contextlib.suppress(AttributeError):
		nargs = action.params[0].nargs if len(action.params) > 0 else "" or ""

	commands = action.opts + action.secondary_opts
	return {
		"type": widget,
		"display_name": action.name,
		"help": action.help,
		"commands": commands,
		"dest": action.callback or commands[0],
		"default": action.default,
		"additional_properties": {"nargs": nargs, **(other or {})},
	}


def categorize(actions: list[Any]) -> Generator[types.Item, None, None]:
	"""Catergorise each action and generate json."""
	import click

	for action in actions:
		if isinstance(action.type, click.Choice):
			yield actionToJson(action, types.ItemType.Choice, {"choices": action.type.choices})
		elif isinstance(action.type, click.types.IntParamType):
			yield actionToJson(action, types.ItemType.Int)
		elif isinstance(action.type, click.types.BoolParamType):
			yield actionToJson(action, types.ItemType.Bool)
		else:
			yield actionToJson(action, types.ItemType.Text)


def convert(parser: Any) -> types.ParserRep:
	"""Convert click to a dict.

	Args:
	----
		parser (click.core.Command): click parser

	Returns:
	-------
		types.ParserRep: dictionary representing parser object

	"""
	return {"parser_description": "", "widgets": extract(parser)}
