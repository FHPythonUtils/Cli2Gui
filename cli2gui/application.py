"""Application here uses PySimpleGUI
"""
import sys
import argparse
import io
import PySimpleGUI as sg
import getostheme
from PIL import Image, ImageTk

BASE = {}

def get_img_data(f, first=False):
	"""Generate image data using PIL """
	img = Image.open(f)
	img.thumbnail((BASE["title_size"]*3, BASE["title_size"]*3))
	if first:                     # tkinter is inactive the first time
		bio = io.BytesIO()
		img.save(bio, format="PNG")
		del img
		return bio.getvalue()
	return ImageTk.PhotoImage(img)

def stringTitlecase(string, splitStr="_"):
	'''Convert a string to title case '''
	try:
		return " ".join((part[0].upper() + part[1:]) for part in string.split(splitStr))
	except IndexError:
		return ""

def stringSentencecase(string):
	'''Convert a string to sentence case '''
	try:
		return string[0].upper() + string[1:]
	except IndexError:
		return ""

def inputText(key):
	'''Return an input text field '''
	return sg.InputText(size=BASE["input_size"], pad=BASE["padding"], key=key,
	font=("sans", BASE["text_size"]))

def check(key):
	'''Return a checkbox '''
	return sg.Check("", size=BASE["input_size"], pad=BASE["padding"], key=key)

def label(text, font=11):
	'''Return a label '''
	return sg.Text(text, size=(int(BASE["label_size"][0]*11/font),
	BASE["label_size"][1]), pad=BASE["padding"], font=("sans", font))

def helpArgName(dest, commands):
	'''Return a label for the arg name '''
	return(label("- "+stringTitlecase(dest)+": "+str(commands), 14))

def helpArgHelp(helpText):
	'''Return a label for the arg help text '''
	return label(stringSentencecase(helpText))

def title(text, image=None):
	'''Return a set of widgets that make up the application header '''
	if image is not None:
		return [sg.Image(data=get_img_data(image, first=True)), sg.Text(text, pad=BASE["padding"], font=("sans", BASE["title_size"]))]
	else:
		return [sg.Text(text, pad=BASE["padding"], font=("sans", BASE["title_size"]))]


def helpFlagWidget(commands, helpText, dest):
	'''Return a set of widgets that make up an arg with true/ false'''
	return [sg.Column([[helpArgName(dest, commands)], [helpArgHelp(helpText)]],	pad=(0, 0)),
	sg.Column([[check(dest)]], pad=(0, 0))]

def helpCounterWidget():
	'''Return a set of widgets that make up an arg with int/ count'''


def helpTextWidget(commands, helpText, dest):
	'''Return a set of widgets that make up an arg with text'''
	return [sg.Column([[helpArgName(dest, commands)], [helpArgHelp(helpText)]],	pad=(0, 0)),
	sg.Column([[inputText(dest)]], pad=(0, 0))]

def button(text):
	'''Return a button '''
	return sg.Button(text, size=BASE["button"], pad=BASE["padding"], font=("sans", BASE["text_size"]))


def setBase24Theme(theme, darkTheme):
	"""Set the base24 theme to set to the application

	Args:
		theme (dict): base24 theme
		darkTheme (dict): dark theme variant
	"""
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


def setSizes(sizes):
	"""Set the widget sizes to the application

	Args:
		sizes (dict): dict containing the sizes
	"""
	global BASE
	if sizes is None:
		BASE = {
			"title_size": 28,
			"label_size": (30, None),
			"input_size": (30, 1),
			"button":(10, 1),
			"padding":(5, 10),
			"helpText_size": 14,
			"text_size": 11
		}
	else:
		BASE = sizes


def run(build_spec):
	"""Main entry point for the application

	Args:
		build_spec (dict): args that customise the application such as the theme
		or the function to run
	"""
	# Set the theme
	setBase24Theme(build_spec["theme"], build_spec["darkTheme"])

	# Set sizes
	setSizes(build_spec["sizes"])

	# Build window from args
	sections = []
	for widget in build_spec["widgets"]:
		sectionToExtend = widget["contents"]
		if len(sectionToExtend) > 0:
			sections.extend(sectionToExtend)

	argConstruct = []
	for section in sections:
		argConstruct.append([label(stringTitlecase(section["name"], " "), 14)])
		for item in section["items"]:
			if item["type"] == "RadioGroup":
				rGroup = item["data"]["widgets"]
				for rElement in rGroup:
					argConstruct.append(helpFlagWidget(rElement["data"]['commands'],
					rElement["data"]['help'], rElement["data"]['dest']))
			elif item["type"] == "Bool":
				argConstruct.append(helpFlagWidget(item["data"]['commands'],
				item["data"]['help'], item["data"]['dest']))
			else:
				argConstruct.append(helpTextWidget(item["data"]['commands'],
				item["data"]['help'], item["data"]['dest']))

	# Set the layout
	layout = [
		title(build_spec["program_name"], build_spec["image"]),
		[label(stringSentencecase(build_spec["program_description"]))]
	]
	if len(argConstruct) > build_spec["max_args_shown"]:
		layout.append([sg.Column(argConstruct, size=(850, build_spec["max_args_shown"]* 5 *
		(BASE["helpText_size"] + BASE["text_size"])), pad=(0, 0), scrollable=True,
		vertical_scroll_only=True)])
	else:
		layout.extend(argConstruct)
	layout.append([button('Run'), button('Exit')])
	window = sg.Window(build_spec["program_name"], layout, alpha_channel=.95,
	icon=get_img_data(build_spec["image"], first=True))

	# While the application is running
	argparser = build_spec["argparser"]
	while True:
		event, values = window.read()
		if event in (None, 'Exit'):
			sys.exit(0)
		try:
			if argparser == "argparse":
				args = argparse.Namespace(**values)
			elif argparser == "optparse":
				# TODO
				pass
			elif argparser == "getopt":
				args = [(key, values[key]) for key in values if values[key]]
			build_spec["run_function"](args)
		except Exception as e:
			print(repr(e))

	window.close()
