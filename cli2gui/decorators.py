"""Decorator and entry point for the program
"""
import json
from os import path
import sys
from functools import reduce
from copy import deepcopy

# Parsers - these are all default so will not crash everything
from argparse import ArgumentParser
from optparse import OptionParser
import getopt

# Import module
from cli2gui import (
	application,
	argparse2json,
	getopt2json,
	optparse2json)

DO_COMMAND = '--cli2gui'

if sys.platform.startswith("win"):
	def quote(value):
		return u'"{}"'.format(u'{}'.format(value).replace(u'"', u'""'))
else:	# POSIX shell
	def quote(value):
		return u"'{}'".format(u'{}'.format(value).replace(u"'", u"'\\''"))


def merge(*maps):
	"""Merge all maps left to right"""
	copies = map(deepcopy, maps)
	return reduce(lambda acc, val: acc.update(val) or acc, copies)


def create_from_parser(self_parser, args_parser, kwargs_parser, source_path, **kwargs):
	"""Create a build_spec dict for use in the application

	Args:
		parser ([type]): [description]
		source_path ([type]): [description]

	Returns:
		dict: build_spec
	"""
	run_cmd = kwargs.get('target')
	if run_cmd is None:
		if hasattr(sys, 'frozen'):
			run_cmd = quote(source_path)
		else:
			run_cmd = '{} -u {}'.format(quote(sys.executable), quote(source_path))

	argparser = kwargs.get("argparser", "argparse")

	build_spec = {
		'run_function': kwargs.get('run_function'),
		"argparser": argparser,
		"theme": kwargs.get("theme", None),
		"darkTheme": kwargs.get("darkTheme", None),
		"sizes": kwargs.get("sizes", None),
		'image': kwargs.get('image', None),
		'program_name':	kwargs.get('program_name') or path.basename(sys.argv[0]).replace('.py', ''),
		'program_description': kwargs.get('program_description') or '',
		'max_args_shown':	kwargs.get('max_args_shown', 5),
	}

	build_spec['program_description'] = build_spec['program_description']

	# Select parser
	if argparser == "optparse":
		build_spec.update(optparse2json.convert(self_parser, **build_spec))
	if argparser == "getopt":
		build_spec.update(getopt2json.convert(args_parser, **build_spec))
	if argparser == "argparse":
		build_spec['program_description'] = self_parser.description
		build_spec.update(argparse2json.convert(self_parser, **build_spec))

	return build_spec


def Cli2Gui(run_function, argparser="argparse", theme=None, darkTheme=None, sizes=None, image=None,
program_name=None, program_description=None, max_args_shown=5, **kwargs):
	'''
	Decorator for client code's main function.
	Serializes argparse data to JSON for use with the Cli2Gui front end
	'''
	params = merge(locals(), locals()['kwargs'])

	def build(calling_function):
		def run_cli2gui(self, *args, **kwargs):
			# Generate the buildspec and run the GUI
			source_path = sys.argv[0]
			build_spec = create_from_parser(
				self, args, kwargs,
				source_path,
				payload_name=calling_function.__name__,
				**params)
			application.run(build_spec)

		def inner(*args, **kwargs):
			getopt.getopt = run_cli2gui
			getopt.gnu_getopt = run_cli2gui
			OptionParser.parse_args = run_cli2gui
			ArgumentParser.parse_args = run_cli2gui
			return calling_function(*args, **kwargs)

		inner.__name__ = calling_function.__name__
		return inner


	def run_without_cli2gui(func):
		return lambda *args, **kwargs: func(*args, **kwargs)

	if DO_COMMAND not in sys.argv:
		return run_without_cli2gui

	return build

if __name__ == '__main__':
	pass
