"""Functions to create args from key/value pairs.
"""
from __future__ import annotations

import argparse
import optparse
from pathlib import Path
from typing import Any

from cli2gui.types import SEP, ParserType


def processValue(key: str, value: str) -> tuple[str, Any]:
	if SEP not in key:
		return key, value or None
	key, _type = key.split(SEP, maxsplit=1)
	if len(str(value)) == 0 or value is None:
		return key, None
	if _type == "ItemType.Bool":
		return key, bool(value)
	if _type == "ItemType.File":
		return key, open(value, encoding="utf-8")
	if _type == "ItemType.Path":
		return key, Path(value)
	if _type == "ItemType.Int":
		return key, int(value)
	if _type == "ItemType.Text":
		return key, value
	if _type == "ItemType.Float":
		return key, float(value)
	if _type == "ItemType.List":
		return key, value
	if _type == "ItemType.Tuple":
		return key, value
	if _type == "ItemType.DateTime":
		return key, value

	return key, value


def argparseFormat(values: dict[str, Any]) -> argparse.Namespace:
	"""Format args for argparse."""
	args = {}
	for key in values:
		cleankey, value = processValue(key, values[key])
		args[cleankey] = value
	return argparse.Namespace(**args)


def optparseFormat(values: dict[str, Any]) -> tuple[optparse.Values, list[str]]:
	"""Format args for optparse."""
	args = {}
	for key in values:
		cleankey, value = processValue(key, values[key])
		args[cleankey] = value
	return (optparse.Values(args), [])


def getoptFormat(values: dict[str, Any]) -> tuple[list[Any], list[Any]]:
	"""Format args for getopt."""
	return ([processValue(key, values[key]) for key in values if values[key]], [])


def docoptFormat(values: dict[str, Any]) -> dict[str, Any]:
	"""Format args for docopt."""
	import docopt

	args = {}
	for key in values:
		cleankey, value = processValue(key, values[key])
		args[cleankey] = value
	return docopt.Dict(args)


def clickFormat(values: dict[str, Any]) -> list[Any]:
	"""Format args for click."""
	args = []
	for key in values:
		val = str(values[key])
		if not callable(key) and len(val) > 0:
			cleankey, value = processValue(key, values[key])
			args.extend([cleankey, value])
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
	return None
