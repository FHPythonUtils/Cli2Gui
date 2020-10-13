"""Decorator and entry point for the program
"""
# pylint: disable=import-outside-toplevel
from __future__ import annotations
from typing import Union
from collections.abc import Callable

from os import path
import sys
from typing import Any
import warnings

# Parsers - these are all default so will not crash everything
from argparse import ArgumentParser
from optparse import OptionParser
import getopt

from cli2gui import c2gtypes


# Import module
from cli2gui.tojson import (
	argparse2json,
	getopt2json,
	optparse2json,
	docopt2json,
	click2json
)
from cli2gui.application import application

DO_COMMAND = '--cli2gui'
DO_NOT_COMMAND = '--disable-cli2gui'

if sys.platform.startswith("win"):
	def quote(value: str):
		""" quote """
		return u'"{}"'.format(u'{}'.format(value).replace(u'"', u'""'))
else:	# POSIX shell
	def quote(value: str):
		""" quote """
		return u"'{}'".format(u'{}'.format(value).replace(u"'", u"'\\''"))


def createFromParser(selfParser: Union[object, None],
argsParser: Union[tuple[Any, Any], None], kwargsParser: Union[dict[Any, Any], None],
sourcePath: str, buildSpec: c2gtypes.BuildSpec, **kwargs: dict[Any, Any]) -> c2gtypes.FullBuildSpec:
	"""Generate a buildSpec from a parser

	Args:
		selfParser (Union[object, None]): A parser that acts on self. eg. ArgumentParser.parse_args
		argsParser (Union[tuple[Any, Any], None]): A parser that acts on function arguments. eg. getopt.getopt
		kwargsParser (Union[dict[Any, Any], None]): A parser that acts on named params
		sourcePath (str): Program source path
		buildSpec (c2gtypes.BuildSpec): Build spec
		**kwargs (dict[Any, Any]): kwargs

	Returns:
		c2gtypes.FullBuildSpec: buildSpec to be used by the application
	"""
	runCmd = kwargs.get('target')
	if runCmd is None:
		if hasattr(sys, 'frozen'):
			runCmd = quote(sourcePath)
		else:
			runCmd = '{} -u {}'.format(quote(sys.executable), quote(sourcePath))
	buildSpec["program_name"] = (buildSpec["program_name"] if buildSpec["program_name"] is not None else path.basename(sys.argv[0]).replace(".py", ""))

	parser = buildSpec["parser"]
	# Select parser
	if selfParser is not None:
		if parser == "optparse":
			buildSpec = {**optparse2json.convert(selfParser), **buildSpec}
		if parser in ["argparse", "dephell_argparse"]:
			buildSpec = {**argparse2json.convert(selfParser), **buildSpec}
		if parser == "docopt":
			buildSpec = {**docopt2json.convert(selfParser), **buildSpec}
	if argsParser is not None:
		if parser == "getopt":
			buildSpec = {**getopt2json.convert(argsParser), **buildSpec}
	if parser == "click":
		buildSpec = {**click2json.convert(buildSpec["run_function"]), **buildSpec}
	return buildSpec # type: ignore


def Click2Gui(run_function: Callable[..., Any], gui: str="pysimplegui", theme: Union[str, list[str], None]=None, darkTheme: Union[str, list[str], None]=None,
 sizes: Union[dict[str, int], None]=None, image: Union[str, None]=None, program_name: Union[str, None]=None, program_description: Union[str, None]=None,
 max_args_shown: int=5, menu: Union[dict[str, Any], None]=None, **kwargs: dict[str, Any]) -> Any:
	"""Decorator to use in the function that contains the argument parser
	Serialises data to JSON and launches the Cli2Gui application

	Args:
		run_function (Callable[..., Any]): The name of the function to call eg.
		gui (str, optional): Override the gui to use. Current options are:
		"pysimplegui", "pysimpleguiqt","pysimpleguiweb". Defaults to
		"pysimplegui".
		theme (Union[str, list[str], None], optional): Set a base24 theme. Can
		also pass a base24 scheme file. eg. one-light.yaml. Defaults to None.
		darkTheme (Union[str, list[str], None], optional): Set a base24 dark
		theme variant. Can also pass a base24 scheme file. eg. one-dark.yaml.
		Defaults to None.
		sizes (Union[dict[str, int], None], optional): Set the UI sizes such as
		the button size. Defaults to None.
		image (image: Union[str, None], optional): Set the program icon. File
		extensions can be any that PIL supports. Defaults to None.
		program_name (Union[str, None], optional): Override the program name.
		Defaults to None.
		program_description (Union[str, None], optional): Override the program
		description. Defaults to None.
		max_args_shown (int, optional): Maximum number of args shown before
		using a scrollbar. Defaults to 5.
		menu (Union[dict[str, Any], None], optional): Add a menu to the program.
		Defaults to None. eg. THIS_DIR = str(Path(__file__).resolve().parent)
		menu={"File": THIS_DIR + "/file.md"}
		**kwargs (dict[Any, Any]): kwargs

	Returns:
		Any: Runs the application
	"""
	bSpec: c2gtypes.BuildSpec = {
		'run_function': run_function,
		"parser": "click",
		"gui": gui,
		"theme": theme,
		"darkTheme": darkTheme,
		"sizes": sizes,
		'image': image,
		'program_name':	program_name,
		'program_description': program_description,
		'max_args_shown':	max_args_shown,
		'menu': menu,
	}

	buildSpec = createFromParser(
		None, None, kwargs,
		sys.argv[0],
		bSpec,
		**{**locals(), **locals()['kwargs']}
	)
	return application.run(buildSpec)


def Cli2Gui(run_function: Union[Callable[..., Any], None], auto_enable: bool=False, parser: str="argparse", gui: str="pysimplegui", theme: Union[str, list[str], None]=None, darkTheme: Union[str, list[str], None]=None,
 sizes: Union[dict[str, int], None]=None, image: Union[str, None]=None, program_name: Union[str, None]=None, program_description: Union[str, None]=None,
 max_args_shown: int=5, menu: Union[dict[str, Any], None]=None, **kwargs: dict[str, Any]) -> Any:
	"""Decorator to use in the function that contains the argument parser
	Serialises data to JSON and launches the Cli2Gui application

	Args:
		run_function (Callable[..., Any]): The name of the function to call eg.
		auto_enable (bool, optional): Enable the GUI by default. If enabled by
		default requires `--disable-cli2gui`, otherwise requires `--cli2gui`.
		Defaults to False.
		parser (str, optional): Override the parser to use. Current
		options are: "argparse", "getopt", "optparse", "docopt",
		"dephell_argparse". Defaults to "argparse".
		gui (str, optional): Override the gui to use. Current options are:
		"pysimplegui", "pysimpleguiqt","pysimpleguiweb". Defaults to
		"pysimplegui".
		theme (Union[str, list[str], None], optional): Set a base24 theme. Can
		also pass a base24 scheme file. eg. one-light.yaml. Defaults to None.
		darkTheme (Union[str, list[str], None], optional): Set a base24 dark
		theme variant. Can also pass a base24 scheme file. eg. one-dark.yaml.
		Defaults to None.
		sizes (Union[dict[str, int], None], optional): Set the UI sizes such as
		the button size. Defaults to None.
		image (image: Union[str, None], optional): Set the program icon. File
		extensions can be any that PIL supports. Defaults to None.
		program_name (Union[str, None], optional): Override the program name.
		Defaults to None.
		program_description (Union[str, None], optional): Override the program
		description. Defaults to None.
		max_args_shown (int, optional): Maximum number of args shown before
		using a scrollbar. Defaults to 5.
		menu (Union[dict[str, Any], None], optional): Add a menu to the program.
		Defaults to None. eg. THIS_DIR = str(Path(__file__).resolve().parent)
		menu={"File": THIS_DIR + "/file.md"}
		**kwargs (dict[Any, Any]): kwargs

	Returns:
		Any: Runs the application
	"""
	bSpec: c2gtypes.BuildSpec = {
		'run_function': run_function,
		"parser": parser,
		"gui": gui,
		"theme": theme,
		"darkTheme": darkTheme,
		"sizes": sizes,
		'image': image,
		'program_name':	program_name,
		'program_description': program_description,
		'max_args_shown':	max_args_shown,
		'menu': menu,
	}

	def build(callingFunction: Callable[..., Any]) -> Callable[..., Any]:
		def runCli2Gui(self, *args: tuple[Any, Any], **kwargs: dict[Any, Any]):
			"""Generate the buildspec and run the GUI

			Args:
				calling_function (def): The calling function eg.
				ArgumentParser.parse_args
			"""
			buildSpec = createFromParser(
				self, args, kwargs,
				#sys.argv[0],
				callingFunction.__name__,
				bSpec,
				**{**locals(), **locals()['kwargs']})
			return application.run(buildSpec)

		def inner(*args: tuple[Any, Any], **kwargs: dict[Any, Any]):
			"""Replace the inner functions with run_cli2gui. eg. When
			ArgumentParser.parse_args is called, do run_cli2gui

			Returns:
				func(): Do the calling_function
			"""
			getopt.getopt = runCli2Gui
			getopt.gnu_getopt = runCli2Gui
			OptionParser.parse_args = runCli2Gui
			ArgumentParser.parse_args = runCli2Gui
			try:
				import docopt
				docopt.docopt = runCli2Gui
			except ImportError:
				pass
			try:
				import dephell_argparse
				dephell_argparse.Parser.parse_args = runCli2Gui
			except ImportError:
				pass
			# Using type=argparse.FileType('r') leads to a resource warning
			with warnings.catch_warnings():
				warnings.filterwarnings("ignore", category=ResourceWarning)
				return callingFunction(*args, **kwargs)

		inner.__name__ = callingFunction.__name__
		return inner


	def runWithoutCli2Gui(callingFunction: Callable[..., Any]) -> Callable[..., Any]:
		def inner(*args: tuple[Any, Any], **kwargs: dict[Any, Any]):
			# Using type=argparse.FileType('r') leads to a resource warning
			with warnings.catch_warnings():
				warnings.filterwarnings("ignore", category=ResourceWarning)
				return callingFunction(*args, **kwargs)
		inner.__name__ = callingFunction.__name__
		return inner

	"""If enabled by default requires do_not_command, otherwise requires do_command """
	if (not auto_enable and DO_COMMAND not in sys.argv) or (auto_enable
	and DO_NOT_COMMAND in sys.argv):
		if DO_NOT_COMMAND in sys.argv:
			sys.argv.remove(DO_NOT_COMMAND)
		return runWithoutCli2Gui
	return build

if __name__ == '__main__':
	pass
