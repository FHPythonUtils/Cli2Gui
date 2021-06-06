"""Generate a dict describing optparse arguments."""
# pylint: disable=protected-access
from __future__ import annotations

from typing import Any, Generator

from .. import c2gtypes


def extract(parser: Any) -> list[c2gtypes.Group]:
	"""Get the actions as json for the parser."""
	try:
		argumentList = [
			{
				"name": "Positional Arguments",
				"arg_items": list(
					categorizeCommand([parser.commands[key] for key in parser.commands])
				),
				"groups": [],
			}
		]
	except AttributeError:
		argumentList: list[c2gtypes.Group] = []
	argumentList.append(
		{
			"name": "Optional Arguments",
			"arg_items": list(categorize(parser.params)),
			"groups": [],
		}
	)
	return argumentList


def actionToJson(action: Any, widget: str) -> c2gtypes.Item:
	"""Generate json for an action and set the widget - used by the application."""
	nargs = ""
	try:
		action.params[0].nargs if len(action.params) > 0 else "" or ""
	except AttributeError:
		pass
	return {
		"type": widget,
		"display_name": action.name,
		"help": action.help,
		"commands": ("--" if len(action.name) > 1 else "-") + action.name,
		"choices": [],
		"dest": action.callback or ("--" if len(action.name) > 1 else "-") + action.name,
		"_other": {"nargs": nargs},
	}


def categorize(actions: list[Any]) -> Generator[c2gtypes.Item, None, None]:
	"""Catergorise each action and generate json."""
	for action in actions:
		yield actionToJson(action, "TextBox")


def categorizeCommand(actions: list[Any]) -> Generator[c2gtypes.Item, None, None]:
	"""Catergorise each action and generate json."""
	for action in actions:
		yield actionToJson(action, "Bool")


def convert(parser: Any) -> c2gtypes.ParserRep:
	"""Convert click to a dict.

	Args:
		parser (click.core.Command): click parser

	Returns:
		c2gtypes.ParserRep: dictionary representing parser object
	"""
	return {"parser_description": "", "widgets": extract(parser)}
