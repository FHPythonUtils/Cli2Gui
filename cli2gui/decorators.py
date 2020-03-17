"""Decorator and entry point for the program
"""
from os import path
import sys
from functools import reduce
from copy import deepcopy

# Parsers - these are all default so will not crash everything
from argparse import ArgumentParser
from optparse import OptionParser
import getopt

# Import module
from cli2gui.tojson import (
	argparse2json,
	getopt2json,
	optparse2json,
	docopt2json)
from cli2gui.application import application

DO_COMMAND = '--cli2gui'
DO_NOT_COMMAND = '--disable-cli2gui'

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
	"""Generate a build_spec from a parser

	Args:
		self_parser (obj): A parser that acts on self. eg. ArgumentParser.parse_args
		args_parser (tuple): A parser that acts on function arguments. eg. getopt.getopt
		kwargs_parser (dict): A parser that acts on named params
		source_path (str): Program source path

	Returns:
		dict: build_spec to be used by the application
	"""
	run_cmd = kwargs.get('target')
	if run_cmd is None:
		if hasattr(sys, 'frozen'):
			run_cmd = quote(source_path)
		else:
			run_cmd = '{} -u {}'.format(quote(sys.executable), quote(source_path))

	parser = kwargs.get("parser", "argparse")

	build_spec = {
		'run_function': kwargs.get('run_function'),
		"parser": parser,
		"gui": kwargs.get('gui'),
		"theme": kwargs.get("theme", None),
		"darkTheme": kwargs.get("darkTheme", None),
		"sizes": kwargs.get("sizes", None),
		'image': kwargs.get('image', None),
		'program_name':	kwargs.get('program_name') or path.basename(sys.argv[0]).replace('.py', ''),
		'program_description': kwargs.get('program_description', None),
		'max_args_shown':	kwargs.get('max_args_shown', 5),
	}

	# Select parser
	if parser == "optparse":
		build_spec.update(optparse2json.convert(self_parser))
	if parser == "getopt":
		build_spec.update(getopt2json.convert(args_parser))
	if parser == "argparse":
		build_spec.update(argparse2json.convert(self_parser))
	if parser == "docopt":
		build_spec.update(docopt2json.convert(self_parser))

	return build_spec


def Cli2Gui(run_function=None, auto_enable=False, parser="argparse",
gui="pysimplegui", theme=None, darkTheme=None, sizes=None, image=None,
program_name=None, program_description=None, max_args_shown=5, **kwargs):
	"""Decorator to use in the function that contains the argument parser
	Serialises data to JSON and launches the Cli2Gui application

	Args:
		run_function (def, optional): The name of the function to call eg.
		main(args). Defaults to None. If not specified, program continues as
		normal (can only run once)
		auto_enable (bool, optional): Enable the GUI by default. If enabled by
		default requires `--disable-cli2gui`, otherwise requires `--cli2gui`.
		Defaults to False.
		parser (str, optional): Override the parser to use. Current
		options are: "argparse", "getopt", "optparse", "docopt". Defaults to
		"argparse".
		gui (str, optional): Override the gui to use. Current options are:
		"pysimplegui", "pysimpleguiqt","pysimpleguiweb". Defaults to
		"pysimplegui".
		theme (str[], optional): Set a base24 theme. Can also pass a base24
		scheme file. eg. one-light.yaml. Defaults to None.
		darkTheme (str[], optional): Set a base24 dark theme variant. Can also
		pass a base24 scheme file. eg. one-dark.yaml. Defaults to None.
		sizes (dict, optional): Set the UI sizes such as the button size.
		Defaults to None.
		image (string, optional): Set the program icon. File extensions can be
		any that PIL supports. Defaults to None.
		program_name (string, optional): Override the program name. Defaults to
		None.
		program_description (string, optional): Override the program
		description. Defaults to None.
		max_args_shown (int, optional): Maximum number of args shown before
		using a scrollbar. Defaults to 5.

	Returns:
		void: Runs the application
	"""
	params = merge(locals(), locals()['kwargs'])

	def build(calling_function):
		def run_cli2gui(self, *args, **kwargs):
			"""Generate the buildspec and run the GUI

			Args:
				calling_function (def): The calling function eg.
				ArgumentParser.parse_args
			"""
			source_path = sys.argv[0]
			build_spec = create_from_parser(
				self, args, kwargs,
				source_path,
				payload_name=calling_function.__name__,
				**params)
			return application.run(build_spec)

		def inner(*args, **kwargs):
			"""Replace the inner functions with run_cli2gui. eg. When
			ArgumentParser.parse_args is called, do run_cli2gui

			Returns:
				func(): Do the calling_function
			"""
			getopt.getopt = run_cli2gui
			getopt.gnu_getopt = run_cli2gui
			OptionParser.parse_args = run_cli2gui
			ArgumentParser.parse_args = run_cli2gui
			try:
				import docopt
				docopt.docopt = run_cli2gui
			except ImportError:
				pass

			return calling_function(*args, **kwargs)

		inner.__name__ = calling_function.__name__
		return inner


	def run_without_cli2gui(func):
		return lambda *args, **kwargs: func(*args, **kwargs)

	"""If enabled by default requires do_not_command, otherwise requires do_command """
	if (not auto_enable and DO_COMMAND not in sys.argv) or (auto_enable
	and DO_NOT_COMMAND in sys.argv):
		if DO_NOT_COMMAND in sys.argv:
			sys.argv.remove(DO_NOT_COMMAND)
		return run_without_cli2gui

	return build

if __name__ == '__main__':
	pass
