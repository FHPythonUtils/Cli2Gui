"""Decorator and entry point for the program
"""
import json
import os
import sys
from argparse import ArgumentParser
from functools import reduce
from copy import deepcopy
from cli2gui import argparse2json
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


def create_from_parser(parser, source_path, **kwargs):
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

	build_spec = {
		'run_function': kwargs.get('run_function'),
		"theme": kwargs.get("theme", None),
		"darkTheme": kwargs.get("darkTheme", None),
		"sizes": kwargs.get("sizes", None),
		'image': kwargs.get('image', None),
		'program_name':	kwargs.get('program_name') or os.path.basename(sys.argv[0]).replace('.py', ''),
		'program_description': kwargs.get('program_description') or '',
		'max_args_shown':	kwargs.get('max_args_shown', 5),
	}

	build_spec['program_description'] = parser.description or build_spec['program_description']

	build_spec.update(argparse2json.convert(parser, **build_spec))
	return build_spec


def Cli2Gui(run_function, theme=None, darkTheme=None, sizes=None, image=None,
program_name=None, program_description=None, max_args_shown=5, **kwargs):
	'''
	Decorator for client code's main function.
	Serializes argparse data to JSON for use with the Cli2Gui front end
	'''
	params = merge(locals(), locals()['kwargs'])

	def build(payload):
		def run_cli2gui(self, args=None, namespace=None):
			from cli2gui import application
			source_path = sys.argv[0]

			build_spec = create_from_parser(
				self,
				source_path,
				payload_name=payload.__name__,
				**params)

			application.run(build_spec)

		def inner(*args, **kwargs):
			ArgumentParser.original_parse_args = ArgumentParser.parse_args
			ArgumentParser.parse_args = run_cli2gui
			return payload(*args, **kwargs)

		inner.__name__ = payload.__name__
		return inner


	def run_without_cli2gui(func):
		return lambda *args, **kwargs: func(*args, **kwargs)

	if DO_COMMAND not in sys.argv:
		return run_without_cli2gui

	return build



if __name__ == '__main__':
	pass
