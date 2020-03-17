"""Generate a dict describing argparse arguments
"""
import argparse
from os import path
from sys import argv
from argparse import (
	_CountAction,
	_HelpAction,
	_StoreFalseAction,
	_StoreTrueAction,
	_SubParsersAction,
	_MutuallyExclusiveGroup)


def iter_parsers(parser):
	''' Iterate over name, parser pairs '''
	try:
		# Get the actions from the subparser
		return [action for action in parser._actions if isinstance(
			action, _SubParsersAction)][0].choices.items()
	except BaseException:
		# There is no subparser
		return list([('::cli2gui/default', parser)])

def is_default_progname(name, subparser):
	return subparser.prog == '{} {}'.format(path.split(argv[0])[-1], name)


def choose_name(name, subparser):
	'''Get the program name	'''
	return name if is_default_progname(name, subparser) else subparser.prog

def contains_actions(a, b):
	''' check if any actions(a) are present in actions(b) '''
	return set(a).intersection(set(b))

def reapply_mutex_groups(mutex_groups, action_groups):
	# argparse stores mutually exclusive groups independently
	# of all other groups. So, they must be manually re-combined
	# with the groups/subgroups to which they were originally declared
	# in order to have them appear in the correct location in the UI.
	#
	# Order is attempted to be preserved by inserting the MutexGroup
	# into the _actions list at the first occurrence of any item
	# where the two groups intersect
	def swap_actions(actions):
		for mutexgroup in mutex_groups:
			mutex_actions = mutexgroup._group_actions
			if contains_actions(mutex_actions, actions):
				# make a best guess as to where we should store the group
				targetindex = actions.index(mutexgroup._group_actions[0])
				# insert the _ArgumentGroup container
				actions[targetindex] = mutexgroup
				# remove the duplicated individual actions
				actions = [action for action in actions
						if action not in mutex_actions]
		return actions

	return [group.update({'items': swap_actions(group['items'])}) or group
			for group in action_groups]


def extract_groups(action_group):
	'''
	Recursively extract argument groups and associated actions
	from ParserGroup objects
	'''
	return {
		'name': action_group.title,
		# List of items that are not help messages
		'items': [action for action in action_group._group_actions
                    if not isinstance(action, _HelpAction)],
		'groups': [extract_groups(group)
                    for group in action_group._action_groups],
	}

def action_to_json(action, widget):
	'''Generate json for an action and set the widget - used by the application'''
	return {
		'type': widget,
		'data': {
			'display_name': action.metavar or action.dest,
			'help': action.help,
			'commands': action.option_strings,
			'choices': list(map(str, action.choices)) if action.choices else [],
			'dest': action.dest,
		},
	}


def build_radio_group(mutex_group, widget_group, options):
	return {
		'type': 'Group',
		'data': {
			'commands': [action.option_strings for action in mutex_group._group_actions],
			'widgets': list(categorize(mutex_group._group_actions, widget_group, options))
		}
  	}


def categorize(actions, widget_dict, options):
	'''Catergorise each action and generate json '''
	for action in actions:
		if isinstance(action, _MutuallyExclusiveGroup):
			yield build_radio_group(action, widget_dict, options)
		elif isinstance(action, (_StoreTrueAction, _StoreFalseAction)):
			yield action_to_json(action, "Bool")
		elif isinstance(action, _CountAction):
			yield action_to_json(action, "Counter")
		elif action.choices:
			yield action_to_json(action, "Dropdown")
		elif isinstance(action.type, argparse.FileType):
			yield action_to_json(action, "File")
		else:
			yield action_to_json(action, "TextBox")


def categorize2(groups, widget_dict, options):
	return [{
		'name': group['name'],
		'items': list(categorize(group['items'], widget_dict, options)),
		'groups': categorize2(group['groups'], widget_dict, options),
	} for group in groups]


def strip_empty(groups):
	return [group for group in groups if group['items']]


def process(parser, widget_dict, options):
	mutex_groups = parser._mutually_exclusive_groups
	raw_action_groups = [extract_groups(group) for group in parser._action_groups
                      if group._group_actions]
	corrected_action_groups = reapply_mutex_groups(mutex_groups, raw_action_groups)
	return categorize2(strip_empty(corrected_action_groups), widget_dict, options)


def convert(parser):
	"""Convert argparse to a dict

	Args:
		parser (argparse): argparse parser

	Returns:
		dict: dictionary representing parser object
	"""
	return {
		'parser_description': parser.description,
		'widgets': [
			{
				'name': choose_name(name, sub_parser),
				'contents': process(sub_parser,
					getattr(sub_parser, 'widgets', {}),
					getattr(sub_parser, 'options', {}))
			} for name, sub_parser in iter_parsers(parser)
		]
	}
