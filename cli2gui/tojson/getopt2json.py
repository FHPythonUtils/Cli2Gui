"""Generate a dict for getopt.
"""
from __future__ import annotations

from collections.abc import Callable
from typing import Generator

from cli2gui.types import Group, Item, ItemType, ParserRep

# ruff: noqa: SLF001


def actionToJson(action: str, widget: ItemType, *, short: bool = True) -> Item:
	"""Convert an arg to json, behave in the same way as argparse hence the large
	amount of duplication.
	"""
	return Item(
		type=widget,
		display_name=action,
		help="",
		commands=[("-" if short else "--") + action],
		dest=("-" if short else "--") + action,
		default=None,
		additional_properties={},
	)


def catLong(actions: list[str]) -> Generator[Item, None, None]:
	"""Categorize long args."""
	for action in actions:
		# True/ false
		if "=" in action:
			yield actionToJson(action[:-1], ItemType.Text, short=False)
		else:
			yield actionToJson(action, ItemType.Bool, short=False)


def catShort(actions: list[str]) -> Generator[Item, None, None]:
	"""Categorize short args."""
	index = 0
	while index < len(actions):
		try:
			# True/ false
			if ":" in actions[index + 1]:
				yield actionToJson(actions[index], ItemType.Text)
				index += 2
			else:
				yield actionToJson(actions[index], ItemType.Bool)
				index += 1
		except IndexError:
			yield actionToJson(actions[index], ItemType.Bool)
			break


def process(
	group: list[str],
	groupName: str,
	categorize: Callable[[list[str]], Generator[Item, None, None]],
) -> list[Group]:
	"""Generate a group (or section)."""
	return [Group(name=groupName, arg_items=list(categorize(group)), groups=[])]


def convert(parser: tuple[list[str], list[str]]) -> ParserRep:
	"""Convert getopt to a dict.

	Args:
	----
		parser (tuple[list[str], list[str]]): getopt parser

	Returns:
	-------
		ParserRep: dictionary representing parser object

	"""
	return ParserRep(
		parser_description="",
		widgets=process(parser[0], "Short Args", catShort)
		+ process(parser[1], "Long Args", catLong),
	)
