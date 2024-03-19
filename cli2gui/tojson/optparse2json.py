"""Generate a dict describing optparse arguments.

pylint and pylance both want me to not access protected methods - I know better ;)
"""

# ruff: noqa: SLF001
from __future__ import annotations

import optparse
from typing import Generator

from cli2gui import types


def extractOptions(optionGroup: optparse.OptionGroup) -> types.Group:
	"""Get the actions as json for each item under a group."""
	return {
		"name": optionGroup.title,  # type: ignore[general-type-issues] # title is confirmed to exist
		# List of arg_items that are not help messages
		"arg_items": list(
			categorize(
				[action for action in optionGroup.option_list if action.action not in "help"]
			)
		),
		"groups": [],
	}


def extractGroups(parser: optparse.OptionParser) -> types.Group:
	"""Get the actions as json for each item and group under the parser."""
	argItems = list(
		categorize([action for action in parser.option_list if action.action not in "help"])
	)
	return {
		"name": "Arguments",
		"arg_items": argItems,
		"groups": [extractOptions(group) for group in parser.option_groups],
	}


def actionToJson(action: optparse.Option, widget: types.ItemType) -> types.Item:
	"""Generate json for an action and set the widget - used by the application."""
	choices = action.choices or []  # type: ignore[general-type-issues] # choices is confirmed to exist\
	default = action.default if action.default != ("NO", "DEFAULT") else None
	return {
		"type": widget,
		"display_name": str(action.metavar or action.dest),
		"help": str(action.help),
		"commands": action._long_opts + action._short_opts,
		"dest": action.dest or "",
		"default": default,
		"additional_properties": {
			"nargs": str(action.nargs or ""),
			"choices": choices,
		},
	}


def categorize(actions: list[optparse.Option]) -> Generator[types.Item, None, None]:
	"""Catergorise each action and generate json."""
	for action in actions:
		# _actions which are either, store_bool, etc..
		if action.action in ("store_true", "store_false"):
			yield actionToJson(action, types.ItemType.Bool)
		# _actions which are of type _CountAction
		elif action.choices:  # type: ignore[general-type-issues] # choices is confirmed to exist
			yield actionToJson(action, types.ItemType.Choice)
		elif action.action in ("count",):
			yield actionToJson(action, types.ItemType.Int)
		else:
			yield actionToJson(action, types.ItemType.Text)


def convert(parser: optparse.OptionParser) -> types.ParserRep:
	"""Convert argparse to a dict.

	Args:
	----
		parser (optparse.OptionParser): optparse parser

	Returns:
	-------
		types.ParserRep: dictionary representing parser object

	"""
	return {"parser_description": "", "widgets": [extractGroups(parser)]}
