"""Application here uses PySimpleGUI
"""
# pylint: disable=import-outside-toplevel
from __future__ import annotations
from typing import Union, Any

import sys
import json
from PySimpleGUI.PySimpleGUI import Element
import yaml
import getostheme
import pypandoc
from catpandoc import pandoc2plain, processpandoc

import PySimpleGUI as pySimpleGuiType
from cli2gui.application.pysimplegui2args import argFormat
from cli2gui.application.widgets import Widgets
from cli2gui import c2gtypes



def getYamlDict(yamlFileName: str) -> dict[str, str]:
	"""Return a yaml_dict from reading yaml_file. If yaml_file is empty or
	doesn't exist, return an empty dict instead."""
	try:
		with open(yamlFileName, "r", encoding="utf-8") as yamlFile:
			yamlDict = yaml.safe_load(yamlFile.read()) or {}
		return yamlDict
	except FileNotFoundError:
		return {}


def themeFromFile(theme: str) -> list[str]:
	"""Set the base24 theme from a base24 scheme.yaml to the application

	Args:
		theme (str): path to file

	Returns:
		list[str]: theme to set
	"""
	schemeDictTheme = getYamlDict(theme)
	return ["#" + schemeDictTheme["base{:02X}".format(x)] for x in range(0, 24)]


def setBase24Theme(theme: Union[str, list[str], None], darkTheme: Union[str,
list[str], None], pySimpleGui: Any) -> None:
	"""Set the base24 theme to the application

	Args:
		theme (Union[str, list[str], None]): the light theme
		darkTheme (Union[str, list[str], None]): the dark theme
		pySimpleGui (Any): pysimplegui module
	"""
	if isinstance(theme, str):
		theme = themeFromFile(theme)
	if isinstance(darkTheme, str):
		theme = themeFromFile(darkTheme)
	if theme is None:
		base24 = {
		"oneDark": [
		"#282c34", "#3f4451", "#4f5666", "#545862", "#9196a1", "#abb2bf", "#e6e6e6",
		"#ffffff", "#e06c75", "#d19a66", "#e5c07b", "#98c379", "#56b6c2", "#61afef",
		"#c678dd", "#be5046", "#21252b", "#181a1f", "#ff7b86", "#efb074", "#b1e18b",
		"#63d4e0", "#67cdff", "#e48bff", ], "oneLight": [
		"#e7e7e9", "#dfdfe1", "#cacace", "#a0a1a7", "#696c77", "#383a42", "#202227",
		"#090a0b", "#ca1243", "#c18401", "#febb2a", "#50a14f", "#0184bc", "#4078f2",
		"#a626a4", "#986801", "#f0f0f1", "#fafafa", "#ec2258", "#f4a701", "#6db76c",
		"#01a7ef", "#709af5", "#d02fcd", ]}
		theme = "oneDark" if getostheme.isDarkMode() else "oneLight"
		base24Theme = base24[theme]
	elif darkTheme is None:
		base24Theme = theme
	else:
		base24Theme = darkTheme if getostheme.isDarkMode() else theme
	accent = {"red": 8, "blue": 13, "green": 11, "purple": 14}
	pySimpleGui.LOOK_AND_FEEL_TABLE['theme'] = {
	'BACKGROUND': base24Theme[16], 'TEXT': base24Theme[6],
	'INPUT': base24Theme[17], 'TEXT_INPUT': base24Theme[6],
	'SCROLL': base24Theme[17], 'BUTTON': (base24Theme[6],
	base24Theme[0]), 'PROGRESS': (base24Theme[accent["purple"]],
	base24Theme[0]), 'BORDER': 0, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0, }
	pySimpleGui.theme("theme") # type: ignore


def setupWidgets(gui: str, sizes: Union[dict[str, Any], None],
pySimpleGui: Any) -> Widgets:
	"""Set the widget sizes to the application

	Args:
		gui (str): user selected gui eg. pysimpleguiqt
		sizes (Union[dict[str, Any], None]): widget sizes
		pySimpleGui (Any): pysimplegui module

	Returns:
		Widgets: widgets object all set up nicely
	"""
	if sizes is None:
		if gui in ["pysimpleguiqt", "pysimpleguiweb"]:
			return Widgets( {
			"title_size": 28, "label_size": (600, None), "input_size": (30,
			1), "button": (10, 1), "padding": (5, 10), "help_text_size": 14,
			"text_size": 11}, pySimpleGui)
		return Widgets( {
			"title_size": 28, "label_size": (30, None), "input_size": (30,
			1), "button": (10, 1), "padding": (5, 10), "help_text_size": 14,
			"text_size": 11}, pySimpleGui)
	return Widgets(sizes, pySimpleGui)


def addItemsAndGroups(section: c2gtypes.Group,
argConstruct: list[list[pySimpleGuiType.Element]], widgets: Widgets):
	"""Add arg_items and groups to the argConstruct list

	Args:
		section (c2gtypes.Group): contents/ section containing name, arg_items
		and groups
		argConstruct (list[list[pySimpleGuiType.Element]]): list of widgets to
		add to the program window
		widgets (Widgets): widgets object used to generate widgets to add to
		argConstruct

	Returns:
		list: updated argConstruct
	"""
	argConstruct.append([
	widgets.label(widgets.stringTitlecase(section["name"], " "), 14)])
	for item in section["arg_items"]:
		if item["type"] == "Group":
			rGroup = item["radio"]
			for rElement in rGroup:
				argConstruct.append(
				widgets.helpFlagWidget(rElement['display_name'], rElement['commands'],
				rElement['help'], rElement['dest']))
		elif item["type"] == "Bool":
			argConstruct.append(
			widgets.helpFlagWidget(item['display_name'], item['commands'], item['help'],
			item['dest']))
		elif item["type"] == "File":
			argConstruct.append(
			widgets.helpFileWidget(item['display_name'], item['commands'], item['help'],
			item['dest']))
		elif item["type"] == "Dropdown":
			argConstruct.append(
			widgets.helpDropdownWidget(item['display_name'], item['commands'],
			item['help'], item['dest'], item["choices"]))
		else:
			argConstruct.append(
			widgets.helpTextWidget(item['display_name'], item['commands'], item['help'],
			item['dest']))
	for group in section["groups"]:
		argConstruct = addItemsAndGroups(group, argConstruct, widgets)
	return argConstruct


def generatePopup(buildSpec: c2gtypes.FullBuildSpec, values: Union[dict[Any, Any],
list[Any]], widgets: Widgets,
pySimpleGui: Any) -> pySimpleGuiType.Window:
	"""Create the popup window

	Args:
		buildSpec (c2gtypes.FullBuildSpec): [description]
		values (Union[dict[Any, Any]): Returned when a button is clicked. Such
		as the menu
		widgets (Widgets): class to build widgets
		pySimpleGui (Any): PySimpleGui class

	Returns:
		pySimpleGui.Window: A PySimpleGui Window
	"""
	output = json.loads(
	pypandoc.convert_file(buildSpec["menu"][values[0]], 'json')) # type: ignore
	pandoc = pandoc2plain.Pandoc2Plain()
	for block in output["blocks"]:
		processpandoc.processBlock(block, pandoc)
	lines: list[str] = str(pandoc.genOutput()).split("\n")
	maxLines = 30 if buildSpec["gui"] == "pysimpleguiqt" else 200
	if len(lines) > maxLines:
		popupText = "\n".join(lines[:maxLines]) + "\n\nMORE TEXT IN SRC FILE"
	else:
		popupText = "\n".join(lines)
	if buildSpec["gui"] == "pysimplegui":
		popupLayout = [
		widgets.title(values[0]),
		[
		pySimpleGui.Column([[
		pySimpleGui.Text(text=popupText, size=(850, maxLines + 10),
		font=("Courier", widgets.sizes["text_size"]))]], size=(850, 400), pad=(0, 0),
		scrollable=True, vertical_scroll_only=True)]]
	else:
		popupLayout = [
		widgets.title(values[0]),
		[
		pySimpleGui
		.Text(text=popupText, size=(850, (widgets.sizes["text_size"]) *
		(2*maxLines + 10)), font=("Courier", widgets.sizes["text_size"]))]]
	return pySimpleGui.Window(
	values[0], popupLayout, alpha_channel=.95, icon=widgets.getImgData(
	buildSpec["image"], first=True) if buildSpec["image"] else None)


def createLayout(buildSpec: c2gtypes.FullBuildSpec, widgets: Widgets,
pySimpleGui: Any, menu: Union[list[str], None]) -> list[list[Element]]:
	"""Create the pysimplegui layout from the build spec

	Args:
		build_spec (c2gtypes.FullBuildSpec): build spec containing widget
		descriptions, program name, description etc.
		widgets (Widgets): class to build widgets

	Returns:
		list[list[Element]]: list of widgets (layout list)
	"""
	argConstruct = []
	for section in buildSpec["widgets"]:
		argConstruct = addItemsAndGroups(section, argConstruct, widgets)

	# Set the layout
	layout: list[list[pySimpleGuiType.Element]] = [[
	pySimpleGui.Menu([['Menu', menu], ], tearoff=True)]] if menu is not None else []
	layout.extend([
	widgets.title(str(buildSpec["program_name"]), buildSpec["image"]),
	[
	widgets.label(
	widgets.stringSentencecase(buildSpec["program_description"]
	if buildSpec["program_description"] is not None else
	buildSpec["parser_description"]))]])
	if len(argConstruct) > buildSpec["max_args_shown"] and buildSpec["gui"] == "pysimplegui":
		layout.append([
		pySimpleGui.Column(
		argConstruct, size=(850, buildSpec["max_args_shown"] * 4.5 *
		(widgets.sizes["help_text_size"] + widgets.sizes["text_size"])), pad=(0, 0),
		scrollable=True, vertical_scroll_only=True)])
	else:
		layout.extend(argConstruct)
	layout.append([widgets.button('Run'), widgets.button('Exit')])
	return layout


def run(buildSpec: c2gtypes.FullBuildSpec):
	"""Main entry point for the application

	Args:
		buildSpec (c2gtypes.FullBuildSpec): args that customise the application such as the theme
		or the function to run
	"""
	import PySimpleGUI as psg # pylint: disable=reimported
	if buildSpec["gui"] == "pysimpleguiqt":
		import PySimpleGUIQt as psg
	elif buildSpec["gui"] == "pysimpleguiweb":
		import PySimpleGUIWeb as psg
	pySimpleGui: Any = psg # type: ignore

	# Set the theme
	setBase24Theme(buildSpec["theme"], buildSpec["darkTheme"], pySimpleGui)

	# Set sizes
	widgets: Widgets = setupWidgets(buildSpec["gui"], buildSpec["sizes"],
	pySimpleGui)

	# Build window from args
	menu = list(buildSpec["menu"]) if buildSpec["menu"] is not None else None
	layout = createLayout(buildSpec, widgets, pySimpleGui, menu)
	window = pySimpleGui.Window(
	buildSpec["program_name"], layout, alpha_channel=.95, icon=widgets.getImgData(
	buildSpec["image"], first=True) if buildSpec["image"] else None)

	# While the application is running
	while True:
		eventAndValues: tuple[Any, Union[dict[Any, Any], list[Any],
		None]] = window.read() #type: ignore
		event, values = eventAndValues
		if event in (None, 'Exit'):
			sys.exit(0)
		try:
			# Create and open the popup window for the menu item
			if values is not None:
				if 0 in values and values[0] is not None:
					popup = generatePopup(buildSpec, values, widgets, pySimpleGui)
					popup.read() # type: ignore
				args = {}
				for key in values:
					if key != 0:
						args[key] = values[key]
				args = argFormat(args, buildSpec["parser"])
				if buildSpec["run_function"] is None:
					return args
				buildSpec["run_function"](args)
		except Exception as exception: # pylint: disable=broad-except
			print(repr(exception))
