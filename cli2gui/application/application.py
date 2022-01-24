"""Application here uses PySimpleGUI.
"""
# pylint: disable=import-outside-toplevel
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

try:
	from getostheme import isDarkMode
except ImportError:
	isDarkMode = lambda: True
import yaml
from PySimpleGUI import Element, Window

from .. import c2gtypes
from .pysimplegui2args import argFormat
from .widgets import Widgets


def themeFromFile(themeFile: str) -> list[str]:
	"""Set the base24 theme from a base24 scheme.yaml to the application.

	Args:
		themeFile (str): path to file

	Returns:
		list[str]: theme to set
	"""
	schemeDictTheme = yaml.safe_load(Path(themeFile).read_text(encoding="utf-8"))
	return ["#" + schemeDictTheme[f"base{x:02X}"] for x in range(0, 24)]


def setBase24Theme(
	theme: str | list[str],
	darkTheme: str | list[str],
	pySimpleGui: Any,
) -> None:
	"""Set the base24 theme to the application.

	Args:
		theme (Union[str, list[str]]): the light theme
		darkTheme (Union[str, list[str]]): the dark theme
		pySimpleGui (Any): pysimplegui module
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
		theme = themeFromFile(theme)

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
		theme = themeFromFile(darkTheme)

	base24Theme = darkTheme if isDarkMode() else theme
	accent = {"red": 8, "blue": 13, "green": 11, "purple": 14}
	pySimpleGui.LOOK_AND_FEEL_TABLE["theme"] = {
		"BACKGROUND": base24Theme[16],
		"TEXT": base24Theme[6],
		"INPUT": base24Theme[17],
		"TEXT_INPUT": base24Theme[6],
		"SCROLL": base24Theme[17],
		"BUTTON": (base24Theme[6], base24Theme[0]),
		"PROGRESS": (base24Theme[accent["purple"]], base24Theme[0]),
		"BORDER": 0,
		"SLIDER_DEPTH": 0,
		"PROGRESS_DEPTH": 0,
	}
	pySimpleGui.theme("theme")  # type: ignore


def setupWidgets(gui: str, sizes: dict[str, Any], pySimpleGui: Any) -> Widgets:
	"""Set the widget sizes to the application.

	Args:
		gui (str): user selected gui eg. pysimpleguiqt
		sizes (Union[dict[str, Any]]): widget sizes
		pySimpleGui (Any): pysimplegui module

	Returns:
		Widgets: widgets object all set up nicely
	"""
	if sizes:
		return Widgets(sizes, pySimpleGui)
	if gui in ["pysimpleguiqt", "pysimpleguiweb"]:
		return Widgets(
			{
				"title_size": 28,
				"label_size": (600, None),
				"input_size": (30, 1),
				"button": (10, 1),
				"padding": (5, 10),
				"help_text_size": 14,
				"text_size": 11,
			},
			pySimpleGui,
		)
	return Widgets(
		{
			"title_size": 28,
			"label_size": (30, None),
			"input_size": (30, 1),
			"button": (10, 1),
			"padding": (5, 10),
			"help_text_size": 14,
			"text_size": 11,
		},
		pySimpleGui,
	)


def addItemsAndGroups(
	section: c2gtypes.Group,
	argConstruct: list[list[Element]],
	widgets: Widgets,
):
	"""Add arg_items and groups to the argConstruct list.

	Args:
		section (c2gtypes.Group): contents/ section containing name, arg_items
		and groups
		argConstruct (list[list[Element]]): list of widgets to
		add to the program window
		widgets (Widgets): widgets object used to generate widgets to add to
		argConstruct

	Returns:
		list: updated argConstruct
	"""
	argConstruct.append([widgets.label(widgets.stringTitlecase(section["name"], " "), 14)])
	for item in section["arg_items"]:
		if item["type"] == "RadioGroup":
			rGroup = item["_other"]["radio"]
			for rElement in rGroup:
				argConstruct.append(
					widgets.helpFlagWidget(
						rElement["display_name"],
						rElement["commands"],
						rElement["help"],
						rElement["dest"],
					)
				)
		elif item["type"] == "Bool":
			argConstruct.append(
				widgets.helpFlagWidget(
					item["display_name"], item["commands"], item["help"], item["dest"]
				)
			)
		elif item["type"] == "File":
			argConstruct.append(
				widgets.helpFileWidget(
					item["display_name"], item["commands"], item["help"], item["dest"]
				)
			)
		elif item["type"] == "Dropdown":
			argConstruct.append(
				widgets.helpDropdownWidget(
					item["display_name"],
					item["commands"],
					item["help"],
					item["dest"],
					item["choices"],
				)
			)
		else:
			argConstruct.append(
				widgets.helpTextWidget(
					item["display_name"], item["commands"], item["help"], item["dest"]
				)
			)
	for group in section["groups"]:
		argConstruct = addItemsAndGroups(group, argConstruct, widgets)
	return argConstruct


def generatePopup(
	buildSpec: c2gtypes.FullBuildSpec,
	values: dict[Any, Any] | list[Any],
	widgets: Widgets,
	pySimpleGui: Any,
) -> Window:
	"""Create the popup window.

	Args:
		buildSpec (c2gtypes.FullBuildSpec): [description]
		values (Union[dict[Any, Any]): Returned when a button is clicked. Such
		as the menu
		widgets (Widgets): class to build widgets
		pySimpleGui (Any): PySimpleGui class

	Returns:
		pySimpleGui.Window: A PySimpleGui Window
	"""
	maxLines = 30 if buildSpec["gui"] == "pysimpleguiqt" else 200
	try:
		from catpandoc.application import pandoc2plain

		lines: list[str] = pandoc2plain(buildSpec["menu"][values[0]], 80).split("\n")
		if len(lines) > maxLines:
			popupText = "\n".join(lines[:maxLines]) + "\n\nMORE TEXT IN SRC FILE"
		else:
			popupText = "\n".join(lines)
	except:
		popupText = Path(buildSpec["menu"][values[0]]).read_text(encoding="utf-8")
	if buildSpec["gui"] == "pysimplegui":
		popupLayout = [
			widgets.title(values[0]),
			[
				pySimpleGui.Column(
					[
						[
							pySimpleGui.Text(
								text=popupText,
								size=(850, maxLines + 10),
								font=("Courier", widgets.sizes["text_size"]),
							)
						]
					],
					size=(850, 400),
					pad=(0, 0),
					scrollable=True,
					vertical_scroll_only=True,
				)
			],
		]
	else:
		popupLayout = [
			widgets.title(values[0]),
			[
				pySimpleGui.Text(
					text=popupText,
					size=(850, (widgets.sizes["text_size"]) * (2 * maxLines + 10)),
					font=("Courier", widgets.sizes["text_size"]),
				)
			],
		]
	return pySimpleGui.Window(
		values[0],
		popupLayout,
		alpha_channel=0.95,
		icon=widgets.getImgData(buildSpec["image"], first=True) if buildSpec["image"] else None,
	)


def createLayout(
	buildSpec: c2gtypes.FullBuildSpec,
	widgets: Widgets,
	pySimpleGui: Any,
	menu: str | list[str],
) -> list[list[Element]]:
	"""Create the pysimplegui layout from the build spec.

	Args:
		buildSpec (c2gtypes.FullBuildSpec): build spec containing widget
		widgets (Widgets): class to build widgets
		pySimpleGui (Any): version of PySimpleGui to use
		menu (list[str]]): menu data

	Returns:
		list[list[Element]]: list of widgets (layout list)
	"""
	argConstruct = []
	for section in buildSpec["widgets"]:
		argConstruct = addItemsAndGroups(section, argConstruct, widgets)

	# Set the layout
	layout: list[list[Element]] = [[]]
	if isinstance(menu, list):
		layout: list[list[Element]] = [[pySimpleGui.Menu([["Menu", menu]], tearoff=True)]]

	layout.extend(
		[
			widgets.title(str(buildSpec["program_name"]), buildSpec["image"]),
			[
				widgets.label(
					widgets.stringSentencecase(
						buildSpec["program_description"]
						if buildSpec["program_description"]
						else buildSpec["parser_description"]
					)
				)
			],
		]
	)
	if len(argConstruct) > buildSpec["max_args_shown"] and buildSpec["gui"] == "pysimplegui":
		layout.append(
			[
				pySimpleGui.Column(
					argConstruct,
					size=(
						850,
						buildSpec["max_args_shown"]
						* 4.5
						* (widgets.sizes["help_text_size"] + widgets.sizes["text_size"]),
					),
					pad=(0, 0),
					scrollable=True,
					vertical_scroll_only=True,
				)
			]
		)
	else:
		layout.extend(argConstruct)
	layout.append([widgets.button("Run"), widgets.button("Exit")])
	return layout


def run(buildSpec: c2gtypes.FullBuildSpec):
	"""Main entry point for the application.

	Args:
		buildSpec (c2gtypes.FullBuildSpec): args that customise the application such as the theme
		or the function to run
	"""
	import PySimpleGUI as psg  # pylint: disable=reimported

	if buildSpec["gui"] == "pysimpleguiqt":
		import PySimpleGUIQt as psg
	elif buildSpec["gui"] == "pysimpleguiweb":
		import PySimpleGUIWeb as psg
	pySimpleGui: Any = psg  # type: ignore

	# Set the theme
	setBase24Theme(buildSpec["theme"], buildSpec["darkTheme"], pySimpleGui)

	# Set sizes
	widgets: Widgets = setupWidgets(buildSpec["gui"], buildSpec["sizes"], pySimpleGui)

	# Build window from args
	menu = list(buildSpec["menu"]) if buildSpec["menu"] else ""
	layout = createLayout(buildSpec, widgets, pySimpleGui, menu)
	window = pySimpleGui.Window(
		buildSpec["program_name"],
		layout,
		alpha_channel=0.95,
		icon=widgets.getImgData(buildSpec["image"], first=True) if buildSpec["image"] else None,
	)

	# While the application is running
	while True:
		eventAndValues: tuple[Any, dict[Any, Any] | list[Any]] = window.read()  # type: ignore
		event, values = eventAndValues
		if event in (None, "Exit"):
			sys.exit(0)
		try:
			# Create and open the popup window for the menu item
			if values is not None:
				if 0 in values and values[0] is not None:
					popup = generatePopup(buildSpec, values, widgets, pySimpleGui)
					popup.read()  # type: ignore
				args = {}
				for key in values:
					if key != 0:
						args[key] = values[key]
				args = argFormat(args, buildSpec["parser"])
				if not buildSpec["run_function"]:
					return args
				buildSpec["run_function"](args)
		except Exception as exception:  # pylint: disable=broad-except
			print(repr(exception))
