"""Generate a dict describing optparse arguments.

pylint and pylance both want me to not access protected methods - I know better ;)
"""

# ruff: noqa: SLF001
from __future__ import annotations

import optparse
from typing import Generator

from cli2gui.types import Group, Item, ItemType, ParserRep


def extractOptions(optionGroup: optparse.OptionGroup) -> Group:
	"""Get the actions as json for each item under a group."""
	return Group(
		name=optionGroup.title,
		arg_items=list(
			categorize(
				[action for action in optionGroup.option_list if action.action not in "help"]
			)
		),
		groups=[],
	)


def extractGroups(parser: optparse.OptionParser) -> Group:
	"""Get the actions as json for each item and group under the parser."""
	argItems = list(
		categorize([action for action in parser.option_list if action.action not in "help"])
	)
	return Group(
		name="Arguments",
		arg_items=argItems,
		groups=[extractOptions(group) for group in parser.option_groups],
	)


def actionToJson(action: optparse.Option, widget: ItemType) -> Item:
	"""Generate json for an action and set the widget - used by the application."""
	choices = action.choices or []  # type: ignore[general-type-issues] # choices is confirmed to exist\
	default = action.default if action.default != ("NO", "DEFAULT") else None
	return Item(
		type=widget,
		display_name=str(action.metavar or action.dest),
		help=str(action.help),
		commands=action._long_opts + action._short_opts,
		dest=action.dest or "",
		default=default,
		additional_properties={
			"nargs": str(action.nargs or ""),
			"choices": choices,
		},
	)


def categorize(actions: list[optparse.Option]) -> Generator[Item, None, None]:
	"""Catergorise each action and generate json."""
	for action in actions:
		# _actions which are either, store_bool, etc..
		if action.action in ("store_true", "store_false"):
			yield actionToJson(action, ItemType.Bool)
		# _actions which are of type _CountAction
		elif action.choices:  # type: ignore[general-type-issues] # choices is confirmed to exist
			yield actionToJson(action, ItemType.Choice)
		elif action.action in ("count",):
			yield actionToJson(action, ItemType.Int)
		else:
			yield actionToJson(action, ItemType.Text)


def convert(parser: optparse.OptionParser) -> ParserRep:
	"""Convert argparse to a dict.

	Args:
	----
		parser (optparse.OptionParser): optparse parser

	Returns:
	-------
		ParserRep: dictionary representing parser object

	"""
	return ParserRep(parser_description="", widgets=[extractGroups(parser)])
