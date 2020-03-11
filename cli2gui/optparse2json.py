"""Generate a dict describing optparse arguments
"""
import optparse

def extract_options(option_group):
	return {
		'name': option_group.title,
		# List of items that are not help messages
		'items': list(categorize([action for action in option_group.option_list if action.action not in "help"])),
		'groups': [],
	}

def extract_groups(parser):
	items = list(categorize([action for action in parser.option_list if action.action not in "help"]))
	for group in parser.option_groups:
		items.extend(list(categorize([action for action in group.option_list if action.action not in "help"])))

	return {
		'name': "foo",
		'items': items,
		'groups': [extract_options(group)
                    for group in parser.option_groups],
	}


def action_to_json(action, widget):
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
	for action in actions:
		# _actions which are either, store_bool, etc..
		if action.action in ("store_true", "store_false"):
			yield action_to_json(action, "Bool")
		# _actions which are of type _CountAction
		elif action.action in "count":
			yield action_to_json(action, "Counter")
		else:
			yield action_to_json(action, "TextBox")


def convert(parser, **kwargs):
	"""Convert argparse to a dict

	Args:
		parser (argparse): argparse parser

	Returns:
		dict: dictionary representing parser object
	"""
	return {
		'widgets': [
			{
				'name': parser.get_prog_name(),
				'contents': extract_groups(parser)
			}
		]
	}
