"""Functions to create args from pysimplegui values.
"""
from __future__ import annotations

import argparse
from typing import Any


def argparseFormat(values: dict[str, Any]) -> argparse.Namespace:
	"""Format args for argparse."""
	args = {}
	for key in values:
		if key[-1] == "#":  # File
			args[key[:-1]] = open(values[key], "r", encoding="utf-8")
		elif isinstance(values[key], str) and len(values[key]) == 0:  # Empty strings are None
			args[key] = None
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
		if not callable(key) and len(values[key]) > 0:
			args.extend([key, values[key]])
	return args


def argFormat(values: dict[str, Any], argumentParser: str) -> Any:
	"""Format the args for the desired parser.

	Args:
		values (dict[str, Any]): values from simple gui
		argumentParser (str): argument parser to use

	Returns:
		Any: args
	"""
	formattedArgs = None
	if argumentParser in ["argparse", "dephell_argparse"]:
		formattedArgs = argparseFormat(values)
	elif argumentParser == "optparse":
		formattedArgs = optparseFormat(values)
	elif argumentParser == "getopt":
		formattedArgs = getoptFormat(values)
	elif argumentParser == "docopt":
		formattedArgs = docoptFormat(values)
	elif argumentParser == "click":
		formattedArgs = clickFormat(values)
	return formattedArgs
