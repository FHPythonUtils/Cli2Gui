"""Generate a dict describing argparse arguments
"""
import argparse
import json
import os
import sys
from argparse import (
	_CountAction,
	_HelpAction,
	_StoreFalseAction,
	_StoreTrueAction,
	_SubParsersAction)
from collections import OrderedDict
from uuid import uuid4


def is_subparser(action):
	'''Is the element a subparser? '''
	return isinstance(action, _SubParsersAction)

def get_subparser(actions):
	'''Get the subparser '''
	return list(filter(is_subparser, actions))[0]

def iter_parsers(parser):
	''' Iterate over name, parser pairs '''
	try:
		return get_subparser(parser._actions).choices.items()
	except:
		return iter([('::cli2gui/default', parser)])

def is_default_progname(name, subparser):
	return subparser.prog == '{} {}'.format(os.path.split(sys.argv[0])[-1], name)


def choose_name(name, subparser):
	'''Get the program name	'''
	return name if is_default_progname(name, subparser) else subparser.prog

def get_subparser_help(parser):
	return getattr(parser, 'usage', '')

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

def is_help_message(action):
	''' Is the element a help message? '''
	return isinstance(action, _HelpAction)

def extract_groups(action_group):
	'''
	Recursively extract argument groups and associated actions
	from ParserGroup objects
	'''
	return {
		'name': action_group.title,
		'description': action_group.description,
		'items': [action for action in action_group._group_actions
				  if not is_help_message(action)],
		'groups': [extract_groups(group)
				   for group in action_group._action_groups],

	}

def is_mutex(action):
	return isinstance(action, argparse._MutuallyExclusiveGroup)

def action_to_json(action, widget):

	return {
		'id': action.option_strings[0] if action.option_strings else action.dest,
		'type': widget,
		'data': {
			'display_name': action.metavar or action.dest,
			'help': action.help,
			'nargs': action.nargs or '',
			'commands': action.option_strings,
			'choices': list(map(str, action.choices)) if action.choices else [],
			'dest': action.dest,
		},
	}

def build_radio_group(mutex_group, widget_group, options):
  return {
	'id': str(uuid4()),
	'type': 'RadioGroup',
	'group_name': 'Choose Option',
	'required': mutex_group.required,
	'data': {
	  'commands': [action.option_strings for action in mutex_group._group_actions],
	  'widgets': list(categorize(mutex_group._group_actions, widget_group, options))
	}
  }

def is_flag(action):
	""" _actions which are either, store_bool, etc.. """
	action_types = [_StoreTrueAction, _StoreFalseAction]
	return any(list(map(lambda Action: isinstance(action, Action), action_types)))

def is_counter(action):
	""" _actions which are of type _CountAction """
	return isinstance(action, _CountAction)


def categorize(actions, widget_dict, options):
	for action in actions:
		if is_mutex(action):
			yield build_radio_group(action, widget_dict, options)
		elif is_flag(action):
			yield action_to_json(action, "Bool")
		elif is_counter(action):
			yield action_to_json(action, "Counter")
		else:
			yield action_to_json(action, "TextBox")



def categorize2(groups, widget_dict, options):
	return [{
		'name': group['name'],
		'items': list(categorize(group['items'], widget_dict, options)),
		'groups': categorize2(group['groups'], widget_dict, options),
		'description': group['description'],
	} for group in groups]

def strip_empty(groups):
	return [group for group in groups if group['items']]

def process(parser, widget_dict, options):
	mutex_groups = parser._mutually_exclusive_groups
	raw_action_groups = [extract_groups(group) for group in parser._action_groups
						 if group._group_actions]
	corrected_action_groups = reapply_mutex_groups(mutex_groups, raw_action_groups)

	return categorize2(strip_empty(corrected_action_groups), widget_dict, options)


def convert(parser, **kwargs):
	"""Convert argparse to a dict

	Args:
		parser (argparse): argparse parser

	Returns:
		dict: dictionary representing parser object
	"""
	return {
		'widgets': OrderedDict(
			(choose_name(name, sub_parser), {
				'command': name,
				'name': choose_name(name, sub_parser),
				'help': get_subparser_help(sub_parser),
				'description': '',
				'contents': process(sub_parser,
					getattr(sub_parser, 'widgets', {}),
					getattr(sub_parser, 'options', {}))
			}) for name, sub_parser in iter_parsers(parser))
	}
