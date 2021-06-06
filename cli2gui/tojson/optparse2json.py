"""Generate a dict describing optparse arguments.

pylint and pylance both want me to not access protected methods - I know better ;)
"""
# pylint: disable=protected-access,deprecated-module
# pyright: reportPrivateUsage=false
from __future__ import annotations

import optparse

from .. import c2gtypes


def extractOptions(optionGroup: optparse.OptionGroup) -> c2gtypes.Group:
	"""Get the actions as json for each item under a group."""
	return {
		"name": optionGroup.title,  # type: ignore # title is confirmed to exist
		# List of arg_items that are not help messages
		"arg_items": list(
			categorize(
				[action for action in optionGroup.option_list if action.action not in "help"]
			)
		),
		"groups": [],
	}


def extractGroups(parser: optparse.OptionParser) -> c2gtypes.Group:
	"""Get the actions as json for each item and group under the parser."""
	argItems = list(
		categorize([action for action in parser.option_list if action.action not in "help"])
	)
	return {
		"name": "Arguments",
		"arg_items": argItems,
		"groups": [extractOptions(group) for group in parser.option_groups],
	}


def actionToJson(action: optparse.Option, widget: str) -> c2gtypes.Item:
	"""Generate json for an action and set the widget - used by the application."""
	return {
		"type": widget,
		"display_name": str(action.metavar or action.dest),
		"help": str(action.help),
		"commands": action._long_opts + action._short_opts,
		"choices": action.choices if action.choices else [],  # type: ignore
		"dest": action.dest or "",
		"_other": {"nargs": str(action.nargs or "")},
	}


def categorize(actions: list[optparse.Option]):
	"""Catergorise each action and generate json."""
	for action in actions:
		# _actions which are either, store_bool, etc..
		if action.action in ("store_true", "store_false"):
			yield actionToJson(action, "Bool")
		# _actions which are of type _CountAction
		elif action.choices:  # type: ignore # choices is confirmed to exist
			yield actionToJson(action, "Dropdown")
		elif action.action in "count":
			yield actionToJson(action, "Counter")
		else:
			yield actionToJson(action, "TextBox")


def convert(parser: optparse.OptionParser) -> c2gtypes.ParserRep:
	"""Convert argparse to a dict.

	Args:
		parser (optparse.OptionParser): optparse parser

	Returns:
		c2gtypes.ParserRep: dictionary representing parser object
	"""
	return {"parser_description": "", "widgets": [extractGroups(parser)]}
