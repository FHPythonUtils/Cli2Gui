"""Generate a dict for docopt.
"""
from __future__ import annotations

import re
from typing import Any, Iterator

from cli2gui import types


def actionToJson(
	action: tuple[str, str, int, Any, str], widget: types.ItemType, *, isPos: bool
) -> types.Item:
	"""Generate json for an action and set the widget - used by the application."""

	if isPos or len(action) < 5:
		return {
			"type": widget,
			"display_name": action[0],
			"help": action[1],
			"commands": [action[0]],
			"dest": action[0],
			"default": None,
			"additional_properties": {"nargs": ""},
		}

	default = action[3] if action[3] != "" else None
	return {
		"type": widget,
		"display_name": (action[1] or action[0]).replace("-", " ").strip(),
		"help": action[4],
		"commands": [x for x in action[0:2] if x != ""],
		"dest": action[1] or action[0],
		"default": default,
		"additional_properties": {"nargs": action[2]},
	}


def categorize(
	actions: list[tuple[str, str, int, Any, str]], *, isPos: bool = False
) -> Iterator[types.Item]:
	"""Catergorise each action and generate json.

	Each action is in the form (short, long, argcount, value, help_message)

	"""
	for action in actions:
		# ('-h', '--help', 0, False, 'show this help message and exit')
		if action[0] == "-h" and action[1] == "--help":
			pass
		elif not isPos and action[2] == 0:
			yield actionToJson(action, types.ItemType.Bool, isPos=isPos)
		else:
			yield actionToJson(action, types.ItemType.Text, isPos=isPos)


def extract(parser: Any) -> list[types.Group]:
	"""Get the actions as json for the parser."""
	return [
		{
			"name": "Positional Arguments",
			"arg_items": list(categorize(parsePos(parser), isPos=True)),  # type: ignore
			"groups": [],
		},
		{
			"name": "Optional Arguments",
			"arg_items": list(categorize(parseOpt(parser))),
			"groups": [],
		},
	]


def parseSection(name: str, source: str) -> list[str]:
	"""Taken from docopt."""
	pattern = re.compile(
		"^([^\n]*" + name + "[^\n]*\n?(?:[ \t].*?(?:\n|$))*)",
		re.IGNORECASE | re.MULTILINE,
	)
	return [s.strip() for s in pattern.findall(source)]


def parse(optionDescription: str) -> tuple[str, str, int, Any, str]:
	"""Parse an option help text, adapted from docopt."""
	short, long, argcount, value = "", "", 0, False
	options, _, description = optionDescription.strip().partition("  ")
	options = options.replace(",", " ").replace("=", " ")
	for section in options.split():
		if section.startswith("--"):
			long = section
		elif section.startswith("-"):
			short = section
		else:
			argcount = 1
	if argcount > 0:
		matched = re.findall(r"\[default: (.*)\]", description, flags=re.I)
		value = matched[0] if matched else ""
	return (short, long, argcount, value, description.strip())


def parseOpt(doc: Any) -> list[tuple[str, str, int, Any, str]]:
	"""Parse an option help text, adapted from docopt."""
	defaults = []
	for section in parseSection("options:", doc):
		_, _, section = section.partition(":")
		split = re.split(r"\n[ \t]*(-\S+?)", "\n" + section)[1:]
		split = [s1 + s2 for s1, s2 in zip(split[::2], split[1::2])]
		options = [parse(s) for s in split if s.startswith("-")]
		defaults += options
	return defaults


def parsePos(doc: str) -> list[tuple[str, str]]:
	"""Parse positional arguments from docstring."""
	defaults = []
	for section in parseSection("arguments:", doc):
		_, _, section = section.partition(":")
		defaults.append(
			tuple(col.strip() for col in section.strip().partition("  ") if len(col.strip()) > 0)
		)
	return defaults


def convert(parser: Any) -> types.ParserRep:
	"""Convert getopt to a dict.

	Args:
	----
		parser (Any): docopt parser

	Returns:
	-------
		types.ParserRep: dictionary representing parser object

	"""
	return {"parser_description": "", "widgets": extract(parser)}
