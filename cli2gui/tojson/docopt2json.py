"""Generate a dict for docopt
"""
import re

def action_to_json(action, widget, is_pos):
	'''Generate json for an action and set the widget - used by the application'''
	if is_pos:
		name = action[0]
	else:
		name = action[1].replace("--", "") if action[1] is not None else action[0].replace("-")

	if is_pos or action[1] is None:
		commands = [action[0]]
	elif action[0] is None:
		commands = [action[1]]
	else:
		commands = [action[0], action[1]]

	return {
		'type': widget,
		'data': {
			'display_name': name,
			'help': action[-1],
			'nargs': action[2] if not is_pos else '',
			'commands': commands,
			'choices': [],
			'dest': action[1] if not is_pos and action[1] is not None else action[0],
		},
	}



def categorise(actions, is_pos=False):
	'''Catergorise each action and generate json '''
	for action in actions:
		# ('-h', '--help', 0, False, 'show this help message and exit')
		if not is_pos and action[3] in (True, False):
			yield action_to_json(action, "Bool", is_pos)
		else:
			yield action_to_json(action, "TextBox", is_pos)

def extract(parser):
	'''Get the actions as json for the parser '''
	return [{
		'name': "Positional Arguments",
		'items':list(categorise(parse_pos(parser), True)),
		'groups': [],
	}, {
		'name': "Optional Arguments",
		'items': list(categorise(parse_opt(parser))),
		'groups': [],
	}]



def parse_section(name, source):
	'''Taken from docopt '''
	pattern = re.compile('^([^\n]*' + name + '[^\n]*\n?(?:[ \t].*?(?:\n|$))*)',
						 re.IGNORECASE | re.MULTILINE)
	return [s.strip() for s in pattern.findall(source)]


def parse(option_description):
	'''Parse an option help text, adapted from docopt '''
	short, long, argcount, value = None, None, 0, False
	options, _, description = option_description.strip().partition('  ')
	options = options.replace(',', ' ').replace('=', ' ')
	for s in options.split():
		if s.startswith('--'):
			long = s
		elif s.startswith('-'):
			short = s
		else:
			argcount = 1
	if argcount:
		matched = re.findall(r'\[default: (.*)\]', description, flags=re.I)
		value = matched[0] if matched else None
	return (short, long, argcount, value, description.strip())


def parse_opt(doc):
	'''Parse an option help text, adapted from docopt '''
	defaults = []
	for s in parse_section('options:', doc):
		_, _, s = s.partition(':')
		split = re.split(r'\n[ \t]*(-\S+?)', '\n' + s)[1:]
		split = [s1 + s2 for s1, s2 in zip(split[::2], split[1::2])]
		options = [parse(s) for s in split if s.startswith('-')]
		defaults += options
	return defaults


def parse_pos(doc):
	'''Parse positional arguments from docstring '''
	defaults = []
	for s in parse_section('arguments:', doc):
		_, _, s = s.partition(':')
		defaults.append(tuple([col.strip() for col in s.strip().partition('  ') if len(col.strip()) > 0]))
	return defaults


def convert(parser):
	"""Convert getopt to a dict

	Args:
		parser (argparse): argparse parser

	Returns:
		dict: dictionary representing parser object
	"""

	return {
		'parser_description': "",
		'widgets': [
			{
				'name': "",
				'contents': extract(parser)
			}
		]
	}
