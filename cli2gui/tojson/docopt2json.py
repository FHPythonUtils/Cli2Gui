"""Generate a dict for docopt
"""
from __future__ import annotations
import re
from typing import Any, Iterator

from cli2gui import c2gtypes


def actionToJson(action: tuple[str, str, str, Any, str], widget: str,
isPos: bool) -> c2gtypes.Item:
	'''Generate json for an action and set the widget - used by the application'''
	if isPos:
		name = action[0]
	else:
		name = action[1].replace("--", "") if action[1] is not None else action[0].replace("-", "")

	if isPos or action[1] is None:
		commands = [action[0]]
	elif action[0] is None:
		commands = [action[1]]
	else:
		commands = [action[0], action[1]]

	return {
		'type': widget,
		'display_name': name,
		'help': action[-1],
		'commands': commands,
		'choices': [],
		'dest': action[1] if not isPos and action[1] is not None else action[0],
		'_other': {	'nargs': action[2] if not isPos else ''}
	}



def categorize(actions: list[tuple[str, str, str, Any, str]], isPos: bool=False) -> Iterator[c2gtypes.Item]:
	'''Catergorise each action and generate json '''
	for action in actions:
		# ('-h', '--help', 0, False, 'show this help message and exit')
		if not isPos and action[3] in (True, False):
			yield actionToJson(action, "Bool", isPos)
		else:
			yield actionToJson(action, "TextBox", isPos)

def extract(parser: Any) -> list[c2gtypes.Group]:
	'''Get the actions as json for the parser '''
	return [{
		'name': "Positional Arguments",
		'arg_items':list(categorize(parsePos(parser), True)),
		'groups': [],
	}, {
		'name': "Optional Arguments",
		'arg_items': list(categorize(parseOpt(parser))),
		'groups': [],
	}]



def parseSection(name: str, source: Any) -> list[str]:
	'''Taken from docopt '''
	pattern = re.compile('^([^\n]*' + name + '[^\n]*\n?(?:[ \t].*?(?:\n|$))*)',
						 re.IGNORECASE | re.MULTILINE)
	return [s.strip() for s in pattern.findall(source)]


def parse(optionDescription: str) -> tuple[str, str, str, Any, str]:
	'''Parse an option help text, adapted from docopt '''
	short, long, argcount, value = "", "", 0, False
	options, _, description = optionDescription.strip().partition('  ')
	options = options.replace(',', ' ').replace('=', ' ')
	for section in options.split():
		if section.startswith('--'):
			long = section
		elif section.startswith('-'):
			short = section
		else:
			argcount = 1
	if argcount > 0:
		matched = re.findall(r'\[default: (.*)\]', description, flags=re.I)
		value = matched[0] if matched else ""
	return (short, long, str(argcount), value, description.strip())


def parseOpt(doc: Any) -> list[tuple[str, str, str, Any, str]]:
	'''Parse an option help text, adapted from docopt '''
	defaults = []
	for section in parseSection('options:', doc):
		_, _, section = section.partition(':')
		split = re.split(r'\n[ \t]*(-\S+?)', '\n' + section)[1:]
		split = [s1 + s2 for s1, s2 in zip(split[::2], split[1::2])]
		options = [parse(s) for s in split if s.startswith('-')]
		defaults += options
	return defaults


def parsePos(doc: Any) -> list[tuple[str, str, str, Any, str]]:
	'''Parse positional arguments from docstring '''
	defaults = []
	for section in parseSection('arguments:', doc):
		_, _, section = section.partition(':')
		defaults.append(tuple([col.strip() for col in section.strip().partition('  ') if len(col.strip()) > 0]))
	return defaults


def convert(parser: Any) -> c2gtypes.ParserRep:
	"""Convert getopt to a dict

	Args:
		parser (Any): docopt parser

	Returns:
		c2gtypes.ParserRep: dictionary representing parser object
	"""

	return {
		'parser_description': "",
		'widgets': extract(parser)
	}
