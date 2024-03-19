from __future__ import annotations

from pathlib import Path

try:
	from getostheme import isDarkMode
except ImportError:

	def isDarkMode() -> bool:
		"""Monkeypatch for getostheme.isDarkMode."""
		return True


import yaml


def _themeFromFile(themeFile: str) -> list[str]:
	"""Set the base24 theme from a base24 scheme.yaml to the application.

	Args:
	----
		themeFile (str): path to file

	Returns:
	-------
		list[str]: theme to set

	"""
	schemeDictTheme = yaml.safe_load(Path(themeFile).read_text(encoding="utf-8"))
	return ["#" + schemeDictTheme["palette"][f"base{x:02X}"] for x in range(24)]


def get_base24_theme(
	theme: str | list[str],
	darkTheme: str | list[str],
) -> list[str]:
	"""Set the base24 theme to the application.

	Args:
	----
		theme (Union[str, list[str]]): the light theme
		darkTheme (Union[str, list[str]]): the dark theme

	"""
	# Light theme
	theme = theme or [
		"#e7e7e9",
		"#dfdfe1",
		"#cacace",
		"#a0a1a7",
		"#696c77",
		"#383a42",
		"#202227",
		"#090a0b",
		"#ca1243",
		"#c18401",
		"#febb2a",
		"#50a14f",
		"#0184bc",
		"#4078f2",
		"#a626a4",
		"#986801",
		"#f0f0f1",
		"#fafafa",
		"#ec2258",
		"#f4a701",
		"#6db76c",
		"#01a7ef",
		"#709af5",
		"#d02fcd",
	]
	if isinstance(theme, str):
		theme = _themeFromFile(theme)

	# Dark theme
	darkTheme = darkTheme or [
		"#282c34",
		"#3f4451",
		"#4f5666",
		"#545862",
		"#9196a1",
		"#abb2bf",
		"#e6e6e6",
		"#ffffff",
		"#e06c75",
		"#d19a66",
		"#e5c07b",
		"#98c379",
		"#56b6c2",
		"#61afef",
		"#c678dd",
		"#be5046",
		"#21252b",
		"#181a1f",
		"#ff7b86",
		"#efb074",
		"#b1e18b",
		"#63d4e0",
		"#67cdff",
		"#e48bff",
	]
	if isinstance(darkTheme, str):
		darkTheme = _themeFromFile(darkTheme)

	return darkTheme if isDarkMode() else theme


def stringTitlecase(string: str, splitStr: str = "ALL") -> str:
	"""Convert a string to title case."""

	titleCase = ""
	if len(string) > 0:
		if splitStr == "ALL":
			titleCase = " ".join(
				(part[0].upper() + part[1:]) for part in string.replace("-", "_").split("_")
			)
		else:
			titleCase = " ".join((part[0].upper() + part[1:]) for part in string.split(splitStr))
	return titleCase


def stringSentencecase(string: str) -> str:
	"""Convert a string to sentence case."""

	if string:
		return string[0].upper() + string[1:]
	return ""


def read_file(file_path: str, maxLines: int = 200) -> str:
	"""Get the contents of a file path, attempt to parse with catpandoc..pandoc2plain.

	:param str file_path: path to the file (absolute recommended)
	:return str: file contents
	"""
	try:
		from catpandoc.application import pandoc2plain

		lines = pandoc2plain(file_path, 80).split("\n")
	except ImportError:
		lines = Path(file_path).read_text(encoding="utf-8").split("\n")

	if len(lines) > maxLines:
		popupText = "\n".join(lines[:maxLines]) + "\n\nMORE TEXT IN SRC FILE"
	else:
		popupText = "\n".join(lines)

	return popupText
