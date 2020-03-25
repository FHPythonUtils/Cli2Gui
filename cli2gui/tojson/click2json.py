"""Generate a dict describing optparse arguments
"""
# pylint: disable=protected-access
from os import path
from sys import argv


def extract(parser):
	'''Get the actions as json for the parser '''
	try:
		argumentList = [{
			'name': "Positional Arguments",
			'items':list(categorizeCommand([parser.commands[key] for key in parser.commands])),
			'groups': [],
		}]
	except AttributeError:
		argumentList = []
	argumentList.append({
		'name': "Optional Arguments",
		'items': list(categorize(parser.params)),
		'groups': [],
	})
	return argumentList



def action_to_json(action, widget):
	'''Generate json for an action and set the widget - used by the application'''
	nargs = ""
	try:
		action.params[0].nargs if len(action.params) > 0 else '' or ''
	except AttributeError:
		pass
	return {
		'type': widget,
		'data': {
			'display_name': action.name,
			'help': action.help,
			'nargs': nargs,
			'commands': ("--" if len(action.name) > 1 else "-") + action.name,
			'choices': [],
			'dest': action.callback or ("--" if len(action.name) > 1 else "-") + action.name,
		},
	}

def categorize(actions):
	'''Catergorise each action and generate json '''
	for action in actions:
		yield action_to_json(action, "TextBox")

def categorizeCommand(actions):
	'''Catergorise each action and generate json '''
	for action in actions:
		yield action_to_json(action, "Bool")


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
				'name': path.split(argv[0])[-1],
				'contents': extract(parser)
			}
		]
	}
