"""Generate a dict for getopt.
"""
from __future__ import annotations

from collections.abc import Callable
from typing import Generator

from .. import c2gtypes


def actionToJson(action: str, widget: str, short: bool = True) -> c2gtypes.Item:
	"""Convert an arg to json, behave in the same way as argparse hence the large...

	amount of duplication.
	"""
	return {
		"type": widget,
		"display_name": action,
		"help": "",
		"commands": [("-" if short else "--") + action],
		"choices": [],
		"dest": ("-" if short else "--") + action,
		"_other": {},
	}


def catLong(actions: list[str]):
	"""Categorize long args."""
	for action in actions:
		# True/ false
		if "=" in action:
			yield actionToJson(action[:-1], "TextBox", short=False)
		else:
			yield actionToJson(action, "Bool", short=False)


def catShort(actions: list[str]):
	"""Categorize short args."""
	index = 0
	while index < len(actions):
		try:
			# True/ false
			if ":" in actions[index + 1]:
				yield actionToJson(actions[index], "TextBox")
				index += 2
			else:
				yield actionToJson(actions[index], "Bool")
				index += 1
		except IndexError:
			yield actionToJson(actions[index], "Bool")
			break


def process(
	group: list[str],
	groupName: str,
	categorize: Callable[[list[str]], Generator[c2gtypes.Item, None, None]],
) -> list[c2gtypes.Group]:
	"""Generate a group (or section)."""
	return [
		{
			"name": groupName,
			"arg_items": list(categorize(group)),
			"groups": [],
		}
	]


def convert(parser: tuple[list[str], list[str]]) -> c2gtypes.ParserRep:
	"""Convert getopt to a dict.

	Args:
		parser (tuple[list[str], list[str]]): getopt parser

	Returns:
		c2gtypes.ParserRep: dictionary representing parser object
	"""
	return {
		"parser_description": "",
		"widgets": process(parser[0], "Short Args", catShort)
		+ process(parser[1], "Long Args", catLong),
	}
