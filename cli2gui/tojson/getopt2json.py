"""Generate a dict for getopt.
"""
from __future__ import annotations

from collections.abc import Callable
from typing import Generator

from cli2gui import types

# ruff: noqa: SLF001


def actionToJson(action: str, widget: types.ItemType, *, short: bool = True) -> types.Item:
	"""Convert an arg to json, behave in the same way as argparse hence the large
	amount of duplication.
	"""
	return {
		"type": widget,
		"display_name": action,
		"help": "",
		"commands": [("-" if short else "--") + action],
		"dest": ("-" if short else "--") + action,
		"default": None,
		"additional_properties": {},
	}


def catLong(actions: list[str]) -> Generator[types.Item, None, None]:
	"""Categorize long args."""
	for action in actions:
		# True/ false
		if "=" in action:
			yield actionToJson(action[:-1], types.ItemType.Text, short=False)
		else:
			yield actionToJson(action, types.ItemType.Bool, short=False)


def catShort(actions: list[str]) -> Generator[types.Item, None, None]:
	"""Categorize short args."""
	index = 0
	while index < len(actions):
		try:
			# True/ false
			if ":" in actions[index + 1]:
				yield actionToJson(actions[index], types.ItemType.Text)
				index += 2
			else:
				yield actionToJson(actions[index], types.ItemType.Bool)
				index += 1
		except IndexError:
			yield actionToJson(actions[index], types.ItemType.Bool)
			break


def process(
	group: list[str],
	groupName: str,
	categorize: Callable[[list[str]], Generator[types.Item, None, None]],
) -> list[types.Group]:
	"""Generate a group (or section)."""
	return [
		{
			"name": groupName,
			"arg_items": list(categorize(group)),
			"groups": [],
		}
	]


def convert(parser: tuple[list[str], list[str]]) -> types.ParserRep:
	"""Convert getopt to a dict.

	Args:
	----
		parser (tuple[list[str], list[str]]): getopt parser

	Returns:
	-------
		types.ParserRep: dictionary representing parser object

	"""
	return {
		"parser_description": "",
		"widgets": process(parser[0], "Short Args", catShort)
		+ process(parser[1], "Long Args", catLong),
	}
