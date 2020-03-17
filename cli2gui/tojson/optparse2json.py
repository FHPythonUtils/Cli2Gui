"""Generate a dict describing optparse arguments
"""

def extract_options(option_group):
	'''Get the actions as json for each item under a group '''
	return {
		'name': option_group.title,
		# List of items that are not help messages
		'items': list(categorize([action for action in option_group.option_list
		if action.action not in "help"])),
		'groups': [],
	}

def extract_groups(parser):
	'''Get the actions as json for each item and group under the parser '''
	items = list(categorize([action for action in parser.option_list if action.action not in "help"]))
	return {
		'name': "Arguments",
		'items': items,
		'groups': [extract_options(group)
                    for group in parser.option_groups],
	}


def action_to_json(action, widget):
	'''Generate json for an action and set the widget - used by the application'''
	return {
		'type': widget,
		'data': {
			'display_name': action.metavar or action.dest,
			'help': action.help,
			'nargs': action.nargs or '',
			'commands': action._long_opts + action._short_opts,
			'choices': list(map(str, action.choices)) if action.choices else [],
			'dest': action.dest or "",
		},
	}


def categorize(actions):
	'''Catergorise each action and generate json '''
	for action in actions:
		# _actions which are either, store_bool, etc..
		if action.action in ("store_true", "store_false"):
			yield action_to_json(action, "Bool")
		# _actions which are of type _CountAction
		elif action.choices:
			yield action_to_json(action, "Dropdown")
		elif action.action in "count":
			yield action_to_json(action, "Counter")
		else:
			yield action_to_json(action, "TextBox")


def convert(parser):
	"""Convert argparse to a dict

	Args:
		parser (argparse): argparse parser

	Returns:
		dict: dictionary representing parser object
	"""
	return {
		'parser_description': "",
		'widgets': [
			{
				'name': parser.get_prog_name(),
				'contents': extract_groups(parser)
			}
		]
	}
