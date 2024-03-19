"""Generate a dict describing argparse arguments.
pylint and pylance both want me to not access protected methods - I know better ;).
"""
# ruff: noqa: SLF001

from __future__ import annotations

import argparse
from argparse import (
	Action,
	_CountAction,
	_HelpAction,
	_MutuallyExclusiveGroup,
	_StoreFalseAction,
	_StoreTrueAction,
	_SubParsersAction,
)
from os import path
from sys import argv
from typing import Any, Generator, TypedDict

from cli2gui import types


class ArgparseGroup(TypedDict):
	"""Class to represent an ArgparseGroup."""

	name: str
	arg_items: list[argparse.Action]
	groups: list[ArgparseGroup] | list[Any]


def iterParsers(
	parser: argparse.ArgumentParser,
) -> list[tuple[str, argparse.ArgumentParser]]:
	"""Iterate over name, parser pairs."""
	defaultParser = [
		("::cli2gui/default", parser),
	]
	candidateSubparsers = [
		action for action in parser._actions if isinstance(action, _SubParsersAction)
	]
	if len(candidateSubparsers) == 0:
		return defaultParser

	return defaultParser + list(candidateSubparsers[0].choices.items())


def isDefaultProgname(name: str, subparser: argparse.ArgumentParser) -> bool:
	"""Identify if the passed name is the default program name."""
	return subparser.prog == f"{path.split(argv[0])[-1]} {name}"


def chooseName(name: str, subparser: argparse.ArgumentParser) -> str:
	"""Get the program name."""
	return name if isDefaultProgname(name, subparser) else subparser.prog


def containsActions(
	actionA: list[argparse.Action], actionB: list[argparse.Action]
) -> set[argparse.Action]:
	"""Check if any actions(a) are present in actions(b)."""
	return set(actionA).intersection(set(actionB))


def reapplyMutexGroups(
	mutexGroups: list[argparse._MutuallyExclusiveGroup],
	actionGroups: list[Any],
) -> list[Any]:
	"""_argparse stores mutually exclusive groups independently.
	of all other groups. So, they must be manually re-combined
	with the groups/subgroups to which they were originally declared
	in order to have them appear in the correct location in the UI.

	Order is attempted to be preserved by inserting the MutexGroup
	into the _actions list at the first occurrence of any item
	where the two groups intersect.
	"""

	def swapActions(actions: list[Action]) -> list[Action]:
		for mutexgroup in mutexGroups:
			mutexActions = mutexgroup._group_actions
			if containsActions(mutexActions, actions):
				# make a best guess as to where we should store the group
				targetindex = actions.index(mutexgroup._group_actions[0])
				# insert the _ArgumentGroup container
				actions[targetindex] = mutexgroup
				# remove the duplicated individual actions
				actions = [action for action in actions if action not in mutexActions]
		return actions

	return [
		group.update({"arg_items": swapActions(group["arg_items"])}) or group
		for group in actionGroups
	]


def extractRawGroups(actionGroup: argparse._ArgumentGroup) -> ArgparseGroup:
	"""Recursively extract argument groups and associated actions from ParserGroup objects."""
	return {
		"name": str(actionGroup.title),
		# List of arg_items that are not help messages
		"arg_items": [
			action for action in actionGroup._group_actions if not isinstance(action, _HelpAction)
		],
		"groups": [extractRawGroups(group) for group in actionGroup._action_groups],
	}


def actionToJson(action: argparse.Action, widget: types.ItemType) -> types.Item:
	"""Generate json for an action and set the widget - used by the application."""
	choices = [str(choice) for choice in action.choices] if action.choices else []
	return {
		"type": widget,
		"display_name": str(action.metavar or action.dest),
		"help": str(action.help),
		"commands": list(action.option_strings),
		"dest": action.dest,
		"default": action.default,
		"additional_properties": {"choices": choices, "nargs": action.nargs},
	}


def buildRadioGroup(mutexGroup: _MutuallyExclusiveGroup) -> types.Item:
	"""Create a radio group for a mutex group of arguments."""
	commands = [action.option_strings for action in mutexGroup._group_actions]
	return {
		"type": types.ItemType.RadioGroup,
		"commands": commands,
		"additional_properties": {"radio": list(categorizeItems(mutexGroup._group_actions))},
	}  # type: ignore


def categorizeItems(
	actions: list[argparse.Action],
) -> Generator[types.Item, None, None]:
	"""Catergorise each action and generate json."""
	for action in actions:
		if isinstance(action, _MutuallyExclusiveGroup):
			yield buildRadioGroup(action)
		elif isinstance(action, (_StoreTrueAction, _StoreFalseAction)):
			yield actionToJson(action, types.ItemType.Bool)
		elif isinstance(action, _CountAction):
			yield actionToJson(action, types.ItemType.Int)
		elif action.choices:
			yield actionToJson(action, types.ItemType.Choice)
		elif isinstance(action.type, argparse.FileType):
			yield actionToJson(action, types.ItemType.File)
		else:
			yield actionToJson(action, types.ItemType.Text)


def categorizeGroups(groups: list[ArgparseGroup]) -> list[types.Group]:
	"""Categorize the parser groups and arg_items."""
	return [
		{
			"name": group["name"],
			"arg_items": list(categorizeItems(group["arg_items"])),
			"groups": categorizeGroups(group["groups"]),
		}
		for group in groups
	]


def stripEmpty(groups: list[ArgparseGroup]) -> list[ArgparseGroup]:
	"""Remove groups where group['arg_items'] is false."""
	return [group for group in groups if group["arg_items"]]


def process(parser: argparse.ArgumentParser) -> list[types.Group]:
	"""Reapply the mutex groups and then categorize them and the arg_items under the parser."""
	mutexGroups = parser._mutually_exclusive_groups
	rawActionGroups = [
		extractRawGroups(group) for group in parser._action_groups if group._group_actions
	]
	correctedActionGroups = reapplyMutexGroups(mutexGroups, rawActionGroups)
	return categorizeGroups(stripEmpty(correctedActionGroups))


def convert(parser: argparse.ArgumentParser) -> types.ParserRep:
	"""Convert argparse to a dict.

	Args:
	----
		parser (argparse.ArgumentParser): argparse parser

	Returns:
	-------
		types.ParserRep: dictionary representing parser object

	"""
	widgets = []
	for _, subparser in iterParsers(parser):
		widgets.extend(process(subparser))

	return {"parser_description": f"{parser.prog}: {parser.description or ''}", "widgets": widgets}
