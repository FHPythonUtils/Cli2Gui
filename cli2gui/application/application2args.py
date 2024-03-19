"""Functions to create args from key/value pairs.
"""
from __future__ import annotations

import argparse
from typing import Any

from cli2gui.types import ParserType


def argparseFormat(values: dict[str, Any]) -> argparse.Namespace:
	"""Format args for argparse."""
	args = {}
	for key in values:
		# Empty strings and paths
		if isinstance(values[key], str) and len(values[key]) == 0:
			args[key] = None
		# Paths end in '#', set the base key (used by argparse)
		elif key[-1] == "#":  # File
			args[key[:-1]] = open(values[key], encoding="utf-8")
		else:
			args[key] = values[key]
	return argparse.Namespace(**args)


def optparseFormat(values: dict[str, Any]) -> dict[str, Any]:
	"""Format args for optparse."""
	args = {}
	for key in values:
		args[key] = values[key] if values[key] else None
	return args


def getoptFormat(values: dict[str, Any]) -> tuple[list[Any], list[Any]]:
	"""Format args for getopt."""
	return ([(key, values[key]) for key in values if values[key]], [])


def docoptFormat(values: dict[str, Any]) -> dict[str, Any]:
	"""Format args for docopt."""
	args = {}
	for key in values:
		args[key] = (
			values[key] if not (isinstance(values[key], str) and len(values[key]) == 0) else None
		)
	return args


def clickFormat(values: dict[str, Any]) -> list[Any]:
	"""Format args for click."""
	args = []
	for key in values:
		val = str(values[key])
		if not callable(key) and len(val) > 0:
			args.extend([key, val])
	return args


def argFormat(values: dict[str, Any], argumentParser: str | ParserType) -> Any:
	"""Format the args for the desired parser.

	Args:
	----
		values (dict[str, Any]): values from simple gui
		argumentParser (str): argument parser to use

	Returns:
	-------
		Any: args

	"""
	formattedArgs = None
	convertMap = {
		ParserType.OPTPARSE: optparseFormat,
		ParserType.ARGPARSE: argparseFormat,
		ParserType.DEPHELL_ARGPARSE: argparseFormat,
		ParserType.DOCOPT: docoptFormat,
		ParserType.GETOPT: getoptFormat,
		ParserType.CLICK: clickFormat,
	}
	if argumentParser in convertMap:
		return convertMap[argumentParser](values)
	return formattedArgs
