"""Types for cli2gui
"""

from __future__ import annotations
from collections.abc import Callable
from typing import Union, Any
import typing



class BuildSpec(typing.TypedDict):
	""" representation for the BuildSpec """
	run_function: Union[Callable[..., Any], None]
	parser: str
	gui: str
	theme: Union[str, list[str], None]
	darkTheme: Union[str, list[str], None]
	sizes: Union[dict[str, Any], None]
	image: Union[str, None]
	program_name: Union[str, None]
	program_description: Union[str, None]
	max_args_shown:	int
	menu: Union[dict[str, Any], None]


class Item(typing.TypedDict):
	""" representation for an arg_item """
	type: str
	display_name: str
	help: str
	commands: list[Any]
	choices: Union[list[Any], list[str]]
	dest: str
	_other: dict[Any, Any]


class Group(typing.TypedDict):
	""" representation for an argument group """
	name: str
	arg_items: list[Item]
	groups: Union[list[Group], list[Any]]


class ParserRep(typing.TypedDict):
	""" representation for a parser """
	parser_description: Union[str, None]
	widgets: list[Group]


class FullBuildSpec(typing.TypedDict):
	""" representation for the FullBuildSpec (BuildSpec + ParserRep) """
	run_function: Union[Callable[..., Any], None]
	parser: str
	gui: str
	theme: Union[str, list[str], None]
	darkTheme: Union[str, list[str], None]
	sizes: Union[dict[str, Any], None]
	image: Union[str, None]
	program_name: Union[str, None]
	program_description: Union[str, None]
	max_args_shown:	int
	menu: Union[dict[str, Any], None]
	parser_description: str
	widgets: list[Widgets]
