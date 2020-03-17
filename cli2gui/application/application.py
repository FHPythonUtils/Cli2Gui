"""Application here uses PySimpleGUI
"""
import sys
import yaml
import getostheme

from cli2gui.application.pysimplegui2args import argFormat
from cli2gui.application.widgets import Widgets

def get_yaml_dict(yaml_file):
	"""Return a yaml_dict from reading yaml_file. If yaml_file is empty or
	doesn't exist, return an empty dict instead."""
	try:
		with open(yaml_file, "r") as file_:
			yaml_dict = yaml.safe_load(file_.read()) or {}
		return yaml_dict
	except FileNotFoundError:
		return {}

def themeFromFile(theme):
	"""Set the base24 theme from a base24 scheme.yaml to the application

	Args:
		theme (str): path to file

	Returns:
		str[]: theme to set
	"""
	schemeDictTheme = get_yaml_dict(theme)
	return ["#"+schemeDictTheme["base{:02X}".format(x)] for x in range(0, 24)]


def setBase24Theme(theme, darkTheme, sg):
	"""Set the base24 theme to the application

	Args:
		theme (dict): base24 theme
		darkTheme (dict): dark theme variant
	"""
	if isinstance(theme, str):
		theme = themeFromFile(theme)
	if isinstance(darkTheme, str):
		theme = themeFromFile(darkTheme)
	if theme is None:
		BASE24 = {"oneDark": ["#282c34", "#3f4451", "#4f5666", "#545862", "#9196a1",
		"#abb2bf", "#e6e6e6", "#ffffff", "#e06c75", "#d19a66", "#e5c07b",
		"#98c379", "#56b6c2", "#61afef", "#c678dd", "#be5046", "#21252b",
		"#181a1f", "#ff7b86", "#efb074", "#b1e18b", "#63d4e0", "#67cdff",
		"#e48bff",],
		"oneLight": ["#e7e7e9", "#dfdfe1", "#cacace", "#a0a1a7", "#696c77",
		"#383a42", "#202227", "#090a0b", "#ca1243", "#c18401", "#febb2a",
		"#50a14f", "#0184bc", "#4078f2", "#a626a4", "#986801", "#f0f0f1",
		"#fafafa", "#ec2258", "#f4a701", "#6db76c", "#01a7ef", "#709af5",
		"#d02fcd",]
		}
		theme = "oneDark" if getostheme.isDarkMode() else "oneLight"
		base24_theme = BASE24[theme]
	elif darkTheme is None:
		base24_theme = theme
	else:
		base24_theme = darkTheme if getostheme.isDarkMode() else theme
	accent = {"red": 8, "blue": 13, "green": 11, "purple": 14}
	sg.LOOK_AND_FEEL_TABLE['theme'] = {'BACKGROUND': base24_theme[16],
		'TEXT': base24_theme[6], 'INPUT': base24_theme[17], 'TEXT_INPUT': base24_theme[6],
		'SCROLL': base24_theme[17], 'BUTTON': (base24_theme[6], base24_theme[0]),
		'PROGRESS': (base24_theme[accent["purple"]], base24_theme[0]), 'BORDER': 0,
		'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
	}
	sg.theme("theme")


def setupWidgets(gui, sizes, sg):
	"""Set the widget sizes to the application

	Args:
		sizes (dict): dict containing the sizes
	"""
	widgetSizes = sizes
	if sizes is None:
		if gui in ["pysimpleguiqt", "pysimpleguiweb"]:
			widgetSizes = {
				"title_size": 28,
				"label_size": (600, None),
				"input_size": (30, 1),
				"button":(10, 1),
				"padding":(5, 10),
				"helpText_size": 14,
				"text_size": 11
			}
		else:
			widgetSizes = {
				"title_size": 28,
				"label_size": (30, None),
				"input_size": (30, 1),
				"button":(10, 1),
				"padding":(5, 10),
				"helpText_size": 14,
				"text_size": 11
			}
	return Widgets(widgetSizes, sg)


def addItemsAndGroups(section, argConstruct, widgets):
	"""Add items and groups to the argConstruct list

	Args:
		section (dict): contents/ section containing name, items and groups
		argConstruct (list): list of widgets to add to the program window
		widgets (obj): widgets object used to generate widgets to add to
		argConstruct

	Returns:
		list: updated argConstruct
	"""
	argConstruct.append([widgets.label(widgets.stringTitlecase(section["name"], " "), 14)])
	for item in section["items"]:
		itemData = item["data"]
		if item["type"] == "Group":
			rGroup = itemData["widgets"]
			for rElement in rGroup:
				rElementData = rElement["data"]
				argConstruct.append(widgets.helpFlagWidget(rElementData['display_name'],
				rElementData['commands'], rElementData['help'], rElementData['dest']))
		elif item["type"] == "Bool":
			argConstruct.append(widgets.helpFlagWidget(itemData['display_name'], itemData['commands'],
			itemData['help'], itemData['dest']))
		elif item["type"] == "File":
			argConstruct.append(widgets.helpFileWidget(itemData['display_name'], itemData['commands'],
			itemData['help'], itemData['dest']))
		elif item["type"] == "Dropdown":
			argConstruct.append(widgets.helpDropdownWidget(itemData['display_name'], itemData['commands'],
			itemData['help'], itemData['dest'], itemData["choices"]))
		else:
			argConstruct.append(widgets.helpTextWidget(itemData['display_name'], itemData['commands'],
			itemData['help'], itemData['dest']))
	for group in section["groups"]:
		argConstruct = addItemsAndGroups(group, argConstruct, widgets)
	return argConstruct


def createLayout(build_spec, widgets, sg):
	"""Create the pysimplegui layout from the build spec

	Args:
		build_spec (dict): build spec containing widget descriptions, program
		name, description etc.
		widgets (Widget): class to build widgets

	Returns:
		list: list of widgets (layout list)
	"""

	sections = []
	for widget in build_spec["widgets"]:
		sectionToExtend = widget["contents"]
		if len(sectionToExtend) > 0:
			if isinstance(sectionToExtend, dict):
				sections.append(sectionToExtend)
			else:
				sections.extend(sectionToExtend)

	argConstruct = []
	for section in sections:
		argConstruct = addItemsAndGroups(section, argConstruct, widgets)

	# Set the layout
	layout = [
		widgets.title(build_spec["program_name"], build_spec["image"]),
		[widgets.label(widgets.stringSentencecase(build_spec["program_description"]
		if build_spec["program_description"] is not None else build_spec["parser_description"]))]
	]
	if len(argConstruct) > build_spec["max_args_shown"] and build_spec["gui"] == "pysimplegui":
		layout.append([sg.Column(argConstruct, size=(850, build_spec["max_args_shown"]* 4.5 *
		(widgets.SIZES["helpText_size"] + widgets.SIZES["text_size"])), pad=(0, 0), scrollable=True,
		vertical_scroll_only=True)])
	else:
		layout.extend(argConstruct)
	layout.append([widgets.button('Run'), widgets.button('Exit')])
	return layout


def run(build_spec):
	"""Main entry point for the application

	Args:
		build_spec (dict): args that customise the application such as the theme
		or the function to run
	"""
	if build_spec["gui"] == "pysimpleguiqt":
		import PySimpleGUIQt as sg
	elif build_spec["gui"] == "pysimpleguiweb":
		import PySimpleGUIWeb as sg
	else:
		import PySimpleGUI as sg

	# Set the theme
	setBase24Theme(build_spec["theme"], build_spec["darkTheme"], sg)

	# Set sizes
	widgets = setupWidgets(build_spec["gui"], build_spec["sizes"], sg)

	# Build window from args
	layout = createLayout(build_spec, widgets, sg)
	window = sg.Window(build_spec["program_name"], layout, alpha_channel=.95,
	icon=widgets.get_img_data(build_spec["image"], first=True) if build_spec["image"] else None)


	# While the application is running
	while True:
		event, values = window.read()
		if event in (None, 'Exit'):
			sys.exit(0)
		try:
			args = argFormat(values, build_spec["parser"])
			if build_spec["run_function"] is None:
				return args
			build_spec["run_function"](args)
		except Exception as e:
			print(repr(e))

	window.close()
