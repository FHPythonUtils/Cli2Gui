"""Decorator and entry point for the program.
"""
# pylint: disable=import-outside-toplevel, deprecated-module
from __future__ import annotations

import getopt  # Parser
import sys
import warnings
from argparse import ArgumentParser  # Parser
from collections.abc import Callable
from optparse import OptionParser  # Parser
from os import path
from shlex import quote
from typing import Any

from .application import application
from .c2gtypes import BuildSpec, FullBuildSpec, GUIType, ParserType
from .tojson import (argparse2json, click2json, docopt2json, getopt2json,
                     optparse2json)

DO_COMMAND = "--cli2gui"
DO_NOT_COMMAND = "--disable-cli2gui"


def createFromParser(
	selfParser: Any,
	argsParser: tuple[Any, ...],
	kwargsParser: dict[Any, Any],
	sourcePath: str,
	buildSpec: BuildSpec,
	**kwargs: dict[Any, Any],
) -> FullBuildSpec:
	"""Generate a buildSpec from a parser.

	Args:
		selfParser (Union[object, None]): A parser that acts on self. eg. ArgumentParser.parse_args
		argsParser (Union[tuple[Any, Any], None]): A parser that acts on function
		arguments. eg. getopt.getopt
		kwargsParser (Union[dict[Any, Any], None]): A parser that acts on named params
		sourcePath (str): Program source path
		buildSpec (c2gtypes.BuildSpec): Build spec
		**kwargs (dict[Any, Any]): kwargs

	Returns:
		c2gtypes.FullBuildSpec: buildSpec to be used by the application

	Raises:
		RuntimeError: Throw error if incorrect parser selected
	"""
	runCmd = kwargs.get("target")
	if runCmd is None:
		if hasattr(sys, "frozen"):
			runCmd = quote(sourcePath)
		else:
			runCmd = f"{quote(sys.executable)} -u {quote(sourcePath)}"
	buildSpec["program_name"] = buildSpec["program_name"] or path.basename(sys.argv[0]).replace(
		".py", ""
	)

	# CUSTOM: this seems like a pretty poor pattern to use...
	if buildSpec["parser"] == ParserType.CUSTOM:
		buildSpec["parser"] = input(
			f"!Custom parser selected! Choose one of: {[x.value for x in ParserType]}"
		)
		if buildSpec["parser"] not in ParserType._value2member_map_:
			raise RuntimeError(f"!Custom parser must be one of: {[x.value for x in ParserType]}")

	parser = buildSpec["parser"]
	# Select parser
	convertMap = {
		"self": {
			ParserType.OPTPARSE: optparse2json.convert,
			ParserType.ARGPARSE: argparse2json.convert,
			ParserType.DEPHELL_ARGPARSE: argparse2json.convert,
			ParserType.DOCOPT: docopt2json.convert,
		},
		"args": {
			ParserType.GETOPT: getopt2json.convert,
		},
	}
	if parser in convertMap["self"]:
		return FullBuildSpec(**convertMap["self"][parser](selfParser), **buildSpec)
	if parser in convertMap["args"]:
		return FullBuildSpec(**convertMap["args"][parser](argsParser), **buildSpec)

	# click is unique in behaviour so we cant use the mapping -_-
	if parser == ParserType.CLICK:
		return FullBuildSpec(**click2json.convert(buildSpec["run_function"]), **buildSpec)

	raise RuntimeError(f"!Parser must be one of: {[x.value for x in ParserType]}")


def Click2Gui(  # pylint: disable=invalid-name
	run_function: Callable[..., Any],
	gui: str | GUIType = "pysimplegui",
	theme: str | list[str] | None = None,
	darkTheme: str | list[str] | None = None,
	sizes: dict[str, int] | None = None,
	image: str | None = None,
	program_name: str | None = None,
	program_description: str | None = None,
	max_args_shown: int = 5,
	menu: dict[str, Any] | None = None,
	**kwargs: dict[str, Any],
) -> Any:
	"""Decorator to use in the function that contains the argument parser...

	Serialises data to JSON and launches the Cli2Gui application.

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
		image (Union[str, None], optional): Set the program icon. File
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
	bSpec = BuildSpec(
		run_function,
		ParserType.CLICK,
		gui,
		theme,
		darkTheme,
		sizes,
		image,
		program_name,
		program_description,
		max_args_shown,
		menu,
	)

	buildSpec = createFromParser(
		None, (), kwargs, sys.argv[0], bSpec, **{**locals(), **locals()["kwargs"]}
	)
	return application.run(buildSpec)


def Cli2Gui(  # pylint: disable=invalid-name
	run_function: Callable[..., Any] | None,
	auto_enable: bool = False,
	parser: str | ParserType = "argparse",
	gui: str | ParserType = "pysimplegui",
	theme: str | list[str] | None = None,
	darkTheme: str | list[str] | None = None,
	sizes: dict[str, int] | None = None,
	image: str | None = None,
	program_name: str | None = None,
	program_description: str | None = None,
	max_args_shown: int = 5,
	menu: dict[str, Any] | None = None,
	**kwargs: dict[str, Any],
) -> Any:
	"""Decorator to use in the function that contains the argument parser...

	Serialises data to JSON and launches the Cli2Gui application.

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
		image (Union[str, None], optional): Set the program icon. File
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
	bSpec = BuildSpec(
		**{
			"run_function": run_function,
			"parser": parser,
			"gui": gui,
			"theme": theme,
			"darkTheme": darkTheme,
			"sizes": sizes,
			"image": image,
			"program_name": program_name,
			"program_description": program_description,
			"max_args_shown": max_args_shown,
			"menu": menu,
		}
	)

	def build(callingFunction: Callable[..., Any]) -> Callable[..., Any]:
		"""Generate the buildspec and run the GUI.

		Args:
			callingFunction (Callable[..., Any]): The calling function eg.
			ArgumentParser.parse_args

		Returns:
			Callable[..., Any]: some calling function
		"""

		def runCli2Gui(self, *args: Any, **kwargs: Any) -> Any:
			"""runCli2Gui. run the gui/ application.

			Args:
				*args (Any): Unpack args
				**kwargs (Any): Unpack kwargs

			Returns:
				Any: run the gui/ application
			"""
			buildSpec = createFromParser(
				self,
				args,
				kwargs,
				callingFunction.__name__,
				bSpec,
				**{**locals(), **locals()["kwargs"]},
			)
			return application.run(buildSpec)

		def inner(*args: tuple[Any, Any], **kwargs: dict[Any, Any]) -> Any:
			"""Replace the inner functions with run_cli2gui. eg. When...

			ArgumentParser.parse_args is called, do run_cli2gui.

			Returns:
				Any: Do the calling_function
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

	"""If enabled by default requires do_not_command, otherwise requires do_command."""
	if (not auto_enable and DO_COMMAND not in sys.argv) or (
		auto_enable and DO_NOT_COMMAND in sys.argv
	):
		if DO_NOT_COMMAND in sys.argv:
			sys.argv.remove(DO_NOT_COMMAND)
		return runWithoutCli2Gui
	return build


if __name__ == "__main__":
	pass
