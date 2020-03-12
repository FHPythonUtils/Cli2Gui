import re
try:
	import docopt
except ImportError:
	print("FATAL: requires docopt")


def action_to_json(action, widget, ispos):
	'''Generate json for an action and set the widget - used by the application'''
	if ispos:
		name = action[0]
	else:
		name = action[1].replace("--", "") if action[1] is not None else action[0].replace("-")

	if ispos or action[1] is None:
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
			'nargs': action[2] if not ispos else '',
			'commands': commands,
			'choices': [],
			'dest': action[1] if not ispos and action[1] is not None else action[0],
		},
	}



def categorise(actions, ispos=False):
	'''Catergorise each action and generate json '''
	for action in actions:
		# ('-h', '--help', 0, False, 'show this help message and exit')
		if not ispos and action[3] in (True, False):
			yield action_to_json(action, "Bool", ispos)
		else:
			yield action_to_json(action, "TextBox", ispos)

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
	pattern = re.compile('^([^\n]*' + name + '[^\n]*\n?(?:[ \t].*?(?:\n|$))*)',
						 re.IGNORECASE | re.MULTILINE)
	return [s.strip() for s in pattern.findall(source)]


def parse(option_description):
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
		matched = re.findall('\[default: (.*)\]', description, flags=re.I)
		value = matched[0] if matched else None
	return (short, long, argcount, value, description.strip())


def parse_opt(doc):
	defaults = []
	for s in parse_section('options:', doc):
		_, _, s = s.partition(':')
		split = re.split('\n[ \t]*(-\S+?)', '\n' + s)[1:]
		split = [s1 + s2 for s1, s2 in zip(split[::2], split[1::2])]
		options = [parse(s) for s in split if s.startswith('-')]
		defaults += options
	return defaults


def parse_pos(doc):
	defaults = []
	for s in parse_section('arguments:', doc):
		_, _, s = s.partition(':')
		defaults.append(tuple([col.strip() for col in s.strip().partition('  ') if len(col.strip()) > 0]))
	return defaults


def convert(parser, **kwargs):
	"""Convert getopt to a dict

	Args:
		parser (argparse): argparse parser

	Returns:
		dict: dictionary representing parser object
	"""

	return {
		'widgets': [
			{
				'name': "",
				'contents': extract(parser)
			}
		]
	}
