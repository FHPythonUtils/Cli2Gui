"""Generate a dict for getopt
"""

def action_to_json(action, widget, short=True):
	"""Convert an arg to json, behave in the same way as argparse hence the large
	amount of duplication  """
	return {
		'type': widget,
		'data': {
			'display_name': action,
			'help': "",
			'nargs': "",
			'commands': ("-" if short else "--") + action,
			'choices': [],
			'dest': ("-" if short else "--") + action,
		},
	}

def cat_long(actions):
	"""Categorise long args """
	for action in actions:
		# True/ false
		if "=" in action:
			yield action_to_json(action[:-1], "TextBox", short=False)
		else:
			yield action_to_json(action, "Bool", short=False)

def cat_short(actions):
	"""Categorise short args """
	index = 0
	while index < len(actions):
		try:
			# True/ false
			if ":" in actions[index+1]:
				yield action_to_json(actions[index], "TextBox")
				index += 2
			else:
				yield action_to_json(actions[index], "Bool")
				index += 1
		except IndexError:
			yield action_to_json(actions[index], "Bool")
			break



def process(group, group_name, categorize):
	"""Generate a group (or section) """
	return [{
		'name': group_name,
		'items': list(categorize(group)),
		'groups': [],
	}]

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
				'contents': process(parser[0], "Short Args", cat_short) +
				process(parser[1], "Long Args", cat_long)
			}
		]
	}
