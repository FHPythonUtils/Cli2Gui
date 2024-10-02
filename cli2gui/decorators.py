"""Decorator and entry point for the program.
"""

from __future__ import annotations

import getopt
import sys
import warnings
from argparse import ArgumentParser
from collections.abc import Callable
from optparse import OptionParser
from pathlib import Path
from shlex import quote
from typing import Any, Iterable

from cli2gui.application import application
from cli2gui.tojson import (
	argparse2json,
	click2json,
	docopt2json,
	getopt2json,
	optparse2json,
)
from cli2gui.types import BuildSpec, FullBuildSpec, GUIType, ParserType

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
	----
		selfParser (Any): A parser that acts on self. eg. ArgumentParser.parse_args
		argsParser (tuple[Any, ...]): A parser that acts on function
		arguments. eg. getopt.getopt
		kwargsParser (dict[Any, Any]): A parser that acts on named params
		sourcePath (str): Program source path
		buildSpec (BuildSpec): Build spec
		**kwargs (dict[Any, Any]): kwargs

	Returns:
	-------
		types.FullBuildSpec: buildSpec to be used by the application

	Raises:
	------
		RuntimeError: Throw error if incorrect parser selected

	"""
	_ = kwargsParser
	runCmd = kwargs.get("target")
	if runCmd is None:
		if hasattr(sys, "frozen"):
			runCmd = quote(sourcePath)
		else:
			runCmd = f"{quote(sys.executable)} -u {quote(sourcePath)}"
	buildSpec["program_name"] = buildSpec["program_name"] or Path(sys.argv[0]).name.replace(
		".py", ""
	)

	# CUSTOM: this seems like a pretty poor pattern to use...
	if buildSpec["parser"] == ParserType.CUSTOM:
		buildSpec["parser"] = input(
			f"!Custom parser selected! Choose one of: {[x.value for x in ParserType]}"
		)
		if buildSpec["parser"] not in ParserType._value2member_map_:  # noqa: SLF001
			msg = f"!Custom parser must be one of: {[x.value for x in ParserType]}"
			raise RuntimeError(msg)

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

	msg = f"!Parser must be one of: {[x.value for x in ParserType]}"
	raise RuntimeError(msg)


def Click2Gui(
	run_function: Callable[..., Any],
	gui: str | GUIType = "dearpygui",
	theme: str | list[str] = "",
	darkTheme: str | list[str] = "",
	image: str = "",
	program_name: str = "",
	program_description: str = "",
	max_args_shown: int = 5,
	menu: str | dict[str, Any] = "",
	**kwargs: dict[str, Any],
) -> None:
	"""Use this decorator in the function containing the argument parser.
	Serializes data to JSON and launches the Cli2Gui application.

	Args:
	----
		run_function (Callable[..., Any]): The name of the function to call eg.
		gui (str, optional): Override the gui to use. Current options are:
		"dearpygui", "pysimplegui", "pysimpleguiqt","pysimpleguiweb","freesimplegui",
		Defaults to "dearpygui".
		theme (Union[str, list[str]], optional): Set a base24 theme. Can
		also pass a base24 scheme file. eg. one-light.yaml. Defaults to "".
		darkTheme (Union[str, list[str]], optional): Set a base24 dark
		theme variant. Can also pass a base24 scheme file. eg. one-dark.yaml.
		Defaults to "".
		image (str, optional): Set the program icon. File
		extensions can be any that PIL supports. Defaults to "".
		program_name (str, optional): Override the program name.
		Defaults to "".
		program_description (str, optional): Override the program
		description. Defaults to "".
		max_args_shown (int, optional): Maximum number of args shown before
		using a scrollbar. Defaults to 5.
		menu (Union[dict[str, Any]], optional): Add a menu to the program.
		Defaults to "". eg. THIS_DIR = str(Path(__file__).resolve().parent)
		menu={"File": THIS_DIR + "/file.md"}
		**kwargs (dict[Any, Any]): kwargs

	Returns:
	-------
		Any: Runs the application

	"""
	bSpec = BuildSpec(
		run_function=run_function,
		parser=ParserType.CLICK,
		gui=gui,
		theme=theme,
		darkTheme=darkTheme,
		image=image,
		program_name=program_name,
		program_description=program_description,
		max_args_shown=max_args_shown,
		menu=menu,
	)

	buildSpec = createFromParser(
		None, (), kwargs, sys.argv[0], bSpec, **{**locals(), **locals()["kwargs"]}
	)
	return application.run(buildSpec)


def Cli2Gui(
	run_function: Callable[..., Any],
	auto_enable: bool = False,
	parser: str | ParserType = "argparse",
	gui: str | ParserType = "dearpygui",
	theme: str | list[str] = "",
	darkTheme: str | list[str] = "",
	image: str = "",
	program_name: str = "",
	program_description: str = "",
	max_args_shown: int = 5,
	menu: str | dict[str, Any] = "",
) -> Any:
	"""Use this decorator in the function containing the argument parser.
	Serialises data to JSON and launches the Cli2Gui application.

	Args:
	----
		run_function (Callable[..., Any]): The name of the function to call eg.
		auto_enable (bool, optional): Enable the GUI by default. If enabled by
		default requires `--disable-cli2gui`, otherwise requires `--cli2gui`.
		Defaults to False.
		parser (str, optional): Override the parser to use. Current
		options are: "argparse", "getopt", "optparse", "docopt",
		"dephell_argparse". Defaults to "argparse".
		gui (str, optional): Override the gui to use. Current options are:
		"dearpygui", "pysimplegui", "pysimpleguiqt","pysimpleguiweb","freesimplegui",
		Defaults to "dearpygui".
		theme (Union[str, list[str]], optional): Set a base24 theme. Can
		also pass a base24 scheme file. eg. one-light.yaml. Defaults to "".
		darkTheme (Union[str, list[str]], optional): Set a base24 dark
		theme variant. Can also pass a base24 scheme file. eg. one-dark.yaml.
		Defaults to "".
		image (str, optional): Set the program icon. File
		extensions can be any that PIL supports. Defaults to "".
		program_name (str, optional): Override the program name.
		Defaults to "".
		program_description (str, optional): Override the program
		description. Defaults to "".
		max_args_shown (int, optional): Maximum number of args shown before
		using a scrollbar. Defaults to 5.
		menu (Union[dict[str, Any]], optional): Add a menu to the program.
		Defaults to "". eg. THIS_DIR = str(Path(__file__).resolve().parent)
		menu={"File": THIS_DIR + "/file.md"}

	Returns:
	-------
		Any: Runs the application

	"""
	bSpec = BuildSpec(
		run_function=run_function,
		parser=parser,
		gui=gui,
		theme=theme,
		darkTheme=darkTheme,
		image=image,
		program_name=program_name,
		program_description=program_description,
		max_args_shown=max_args_shown,
		menu=menu,
	)

	def build(callingFunction: Callable[..., Any]) -> Callable[..., Any]:
		"""Generate the buildspec and run the GUI.

		Args:
		----
			callingFunction (Callable[..., Any]): The calling function eg.
			ArgumentParser.parse_args

		Returns:
		-------
			Callable[..., Any]: some calling function

		"""

		def runCli2Gui(self: Any, *args: Iterable[Any], **kwargs: dict[str, Any]) -> None:
			"""Run the gui/ application.

			:return None: the gui/ application
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
			"""Replace the inner functions with run_cli2gui. eg. When.
			ArgumentParser.parse_args is called, do run_cli2gui.

			Returns
			-------
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
		def inner(*args: Iterable[Any], **kwargs: dict[Any, Any]) -> Any:
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
