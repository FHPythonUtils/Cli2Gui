"""Application here uses PySimpleGUI.
"""
# pylint: disable=import-outside-toplevel
from __future__ import annotations

# TODO? https://github.com/syldium/pyterminal

# TODO unused parts of the window should be grabbable (click + move = move window)

# TODO switch tabs by scrolling (this should be a feature of pysimplegui)

# TODO make the window easier to kill. currently i need *two* kill signals

# TODO window should always fit on screen. currently the window grows larger than screen
# when there are too many options. should have vertical-scroll, like Gooey.
# scrollale columns: https://github.com/PySimpleGUI/PySimpleGUI/issues/1779
## unbind mouse-wheel from combobox
#window['Combobox'].TKCombo.unbind_class("TCombobox", "<MouseWheel>")

# TODO? responsive layout https://github.com/PySimpleGUI/PySimpleGUI/issues/4597
# https://github.com/PySimpleGUI/PySimpleGUI/issues/3921

# TODO fix title + subtitle
# should expand to full width

# FIXME "nano" editor is broken -> bug in pyte?
# bug: enter does not produce a new line
# maybe we must send \r\n not \n

# TODO terminal colors
# color test programs:
#   msgcat --color=test
#   colors=256; for (( n=0;n<colors;n++ )) do printf "$(tput setaf $n)%3s$(tput sgr0) " $n; (( (n+3)%6==0 )) && echo; done
#   colors=256; for (( n=0;n<colors;n++ )) do printf "$(tput setaf $n)%3s$(tput sgr0) " $n; (( (n+1)%16==0 )) && echo; done

# FIXME "nyancat" program is not working
# i only see:
# You have nyaned for 2 seconds!
# You have nyaned for 14 seconds!
# You have nyaned for 22 seconds!
# ...

# TODO use camelCase for all vars

import json
import sys
from pathlib import Path
from typing import Any
import subprocess
import threading
import os
import select
import pty

import tkinter as tk
import pyte # terminal emulator. render terminal output to visible characters

try:
	from getostheme import isDarkMode
except ImportError:
	isDarkMode = lambda: True
import yaml

#from PySimpleGUI import Element, Window
from .PySimpleGUI import Element, Window # local version

from .. import c2gtypes
from .pysimplegui2args import argFormat
from .widgets import Widgets

# TODO(milahu) better ...
terminal_width = 80
terminal_height = 24

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
	# default: pysimplegui
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
	args_layout: list[list[Element]],
	widgets: Widgets,
):
	"""Add arg_items and groups to the args_layout list.

	Args:
		section (c2gtypes.Group): contents/ section containing name, arg_items
		and groups
		args_layout (list[list[Element]]): list of widgets to
		add to the program window
		widgets (Widgets): widgets object used to generate widgets to add to
		args_layout

	Returns:
		list: updated args_layout
	"""
	args_layout.append([widgets.label(widgets.stringTitlecase(section["name"], " "), 14)])
	for item in section["arg_items"]:
		# TODO(milahu) use class to switch
		# class x:
		#   def RadioGroup(item):
		#     return ...
		#   def Bool(item):
		#     return ...
		#   def Default(item):
		#     return ...
		# if hasattr(x, "RadioGroup"):
		#   handler = getattr(x, "RadioGroup")
		# else:
		#   handler = x.Default
		if item["type"] == "RadioGroup":
			rGroup = item["_other"]["radio"]
			for rElement in rGroup:
				args_layout.append(
					widgets.helpFlagWidget(
						rElement["display_name"],
						rElement["commands"],
						rElement["help"],
						rElement["dest"],
					)
				)
		elif item["type"] == "Bool":
			args_layout.append(
				widgets.helpFlagWidget(
					item["display_name"], item["commands"], item["help"], item["dest"]
				)
			)
		elif item["type"] == "File":
			args_layout.append(
				widgets.helpFileWidget(
					item["display_name"], item["commands"], item["help"], item["dest"]
				)
			)
		elif item["type"] == "Dropdown":
			args_layout.append(
				widgets.helpDropdownWidget(
					item["display_name"],
					item["commands"],
					item["help"],
					item["dest"],
					item["choices"],
				)
			)
		else:
			args_layout.append(
				widgets.helpTextWidget(
					item["display_name"], item["commands"], item["help"], item["dest"]
				)
			)
	for group in section["groups"]:
		args_layout = addItemsAndGroups(group, args_layout, widgets)
	return args_layout


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

	args_layout = []
	for section in buildSpec["widgets"]:
		args_layout = addItemsAndGroups(section, args_layout, widgets) # magic here

	# Set the layout
	# NOTE(milahu) one big array : )
	layout: list[list[Element]] = \
	[
		[
			pySimpleGui.Menu([["Menu", menu]], tearoff=True)
			if isinstance(menu, list)
			else [],
		],
		[
			widgets.title(str(buildSpec["program_name"]), buildSpec["image"]),
		],
		[
			widgets.label(
				widgets.stringSentencecase(
					buildSpec["program_description"] or
					buildSpec["parser_description"]
				)
			)
		],
		[
			pySimpleGui.TabGroup(
				[[
					pySimpleGui.Tab(
						'Input',
						(
							args_layout
							#if buildSpec["gui"] == "pysimplegui" or len(args_layout) < buildSpec["max_args_shown"]
							if False # debug: always use column
							else [[
								pySimpleGui.Column(
									args_layout,
									size=(
										850,
										buildSpec["max_args_shown"]
										* 4.5
										* (widgets.sizes["help_text_size"] + widgets.sizes["text_size"]),
									),
									pad=(0, 0),
									scrollable=True,
									vertical_scroll_only=True,
									expand_x=True,
									expand_y=True,
								)
							]]
						),
						#font='Courier 15',
						key='-TabInput-',
					),
					pySimpleGui.Tab(
						'Output',
						widgets.ansiTerminalWidget(
							key="-terminal-",
							size=(terminal_width, terminal_height)
						),
						#visible=False,
						key='-TabOutput-'
					),
				]],
				enable_events=True,
				key='-TABGROUP-',
			),
		],
		[
			widgets.button("Run"), widgets.button("Exit"),
		],
	]
	return layout


def run(buildSpec: c2gtypes.FullBuildSpec):
	"""Main entry point for the application.

	Args:
		buildSpec (c2gtypes.FullBuildSpec): args that customise the application such as the theme
		or the function to run
	"""

	#import PySimpleGUI as psg  # pylint: disable=reimported
	from . import PySimpleGUI as psg  # pylint: disable=reimported # debug: local version
	# TODO(milahu) rename psg to pySimpleGui

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

	layout = createLayout(buildSpec, widgets, pySimpleGui, menu) # magic here

	window = pySimpleGui.Window(
		buildSpec["program_name"],
		layout,
		alpha_channel=0.95,
		icon=widgets.getImgData(buildSpec["image"], first=True) if buildSpec["image"] else None,
		finalize=True, # enable .bind()
	)

	# based on https://github.com/Saadmairaj/tkterminal/blob/master/tkterminal/terminal.py
	# https://stackoverflow.com/questions/64680384/pysimplegui-displaying-console-output-in-gui
	# https://github.com/FHPythonUtils/Cli2Gui/issues/8 # virtual terminal
	# https://gist.github.com/thomasballinger/7979808 # Using a pseudo-terminal to interact with interactive Python in a subprocess

	window['-terminal-'].bind("<Return>", "+Return+", propagate=False)
	#window['-terminal-'].bind("<Key>", "+Key+")
	window['-terminal-'].bind("<Key>", "+Key+", propagate=False) # dont propagate. Ctrl-c would be copy, Ctrl-v would be paste
	# TODO handle arrow keys, pos1, end
	#window['-terminal-'].bind("<KeyRelease>", "+KeyRelease+")
	window['-terminal-'].bind("<BackSpace>", "+BackSpace+", propagate=False) # Element.bind(propagate=x) requires https://github.com/PySimpleGUI/PySimpleGUI/pull/5315
	window['-terminal-'].bind("<Tab>", "+Tab+", propagate=False) # Element.bind(propagate=x) requires https://github.com/PySimpleGUI/PySimpleGUI/pull/5315
	window['-terminal-'].bind("<Command-k>", "+Command-k+")
	window['-terminal-'].bind("<Command-c>", "+Command-c+")

	window['-terminal-'].bind("<Left>", "+Left+", propagate=False)
	window['-terminal-'].bind("<Right>", "+Right+", propagate=False)
	window['-terminal-'].bind("<Up>", "+Up+", propagate=False)
	window['-terminal-'].bind("<Down>", "+Down+", propagate=False)

	# pointer events (mouse events)
	#window['-terminal-'].bind("<Enter>", "+Enter+") # mouse enter
	window['-terminal-'].bind("<Button-1>", "+Button-1+", propagate=False) # ClickLeft
	#window['-terminal-'].bind("<Button-2>", "+Button-2+") # ClickMiddle
	#window['-terminal-'].bind("<Button-3>", "+Button-3+") # ClickRight

	# https://stackoverflow.com/questions/41542960/run-interactive-bash-with-popen-and-a-dedicated-tty-python
	# https://stackoverflow.com/questions/22194774/interaction-between-python-script-and-linux-shell
	# https://stackoverflow.com/questions/9673730/interacting-with-bash-from-python
	# https://stackoverflow.com/questions/59164314/how-can-i-create-a-small-idle-like-python-shell-in-tkinter

	#shell_output = None
	#shell_input = None
	#if True:
	command = 'bash'
	#command = ["/usr/bin/env", "bash", "-i"],
	# command = 'docker run -it --rm centos /bin/bash'.split()
	# save original tty setting then set it to raw mode

	# open pseudo-terminal to interact with subprocess
	master_fd, slave_fd = pty.openpty()

	def gui_to_shell_string(string):
		#gui_to_shell_stream.write(string) # no
		bytes_ = string.encode("utf8")
		os.write(master_fd, bytes_)

	def gui_to_shell_bytes(bytes_):
		os.write(master_fd, bytes_)

	# use os.setsid() make it run in a new process group, or bash job control will not be enabled
	shell_env = os.environ.copy() # this seems to fix darkmode. weird.
	shell_process = subprocess.Popen(
		command,
		preexec_fn=os.setsid,
		stdin=slave_fd,
		stdout=slave_fd,
		stderr=slave_fd,
		universal_newlines=True,
		env=shell_env,
		encoding="utf8",
		close_fds=True,
	)

	#shell_output = os.fdopen(master_fd, 'rb')
	#shell_input = os.fdopen(master_fd, 'wb')

	# default PS1 is too long
	print("set PS1")
	#gui_to_shell_bytes(b"PS1='\\n$ '\n")
	gui_to_shell_bytes(b"PS1='$ '\n") # FIXME not working?
	gui_to_shell_bytes(b"clear\n")

	# simpler than select.select()
	# better? worse?
	# select.select is not available on windows (windows can select only network-sockets, not files)
	# https://github.com/syldium/pyterminal/blob/45968f20f7f29d2cd1d05c8afaa646c983d913b6/pyterminal/CmdProcessor.py#L89
	def read_stdout():
		while True:
			if shell_process_exit or shell_process.poll() != None:
				break
			#msg = shell_process.stdout.readline()
			msg = shell_process.stdout.read()
			#print("stdout: ", msg, end="")
			window['-terminal-'].print(msg, end="")

	def read_stderro():
		while True:
			if shell_process_exit or shell_process.poll() != None:
				break
			#msg = shell_process.stderr.readline()
			#msg = shell_process.stderr.read()
			#print("stdout: ", msg, end="")
			window['-terminal-'].print(msg, end="")

	#print("start thread: read_stdout")
	#threading.Thread(target=read_stdout).start()
	#print("start thread: read_stderro")
	#threading.Thread(target=read_stderro).start()

	# ansi terminal emulator
	pyte_screen = pyte.Screen(terminal_width, terminal_height)
	pyte_stream = pyte.ByteStream(pyte_screen)
	#pyte_stream.feed(b"asdf")

	def shell_to_gui_pump():
		# https://docs.python.org/3/library/select.html#select.select
		# select ready files
		# FIXME select is not portable
		# on windows, select only works with network sockets, not with files
		while True:
			read_list, _write_list, error_list = select.select([ master_fd ], [], [])
			if master_fd in read_list:
				# pump from shell_process to GUI
				bytes_ = os.read(master_fd, 10240)
				#print("shell_to_gui_pump: read master_fd = pump from shell_process to GUI:", repr(bytes_))
				if bytes_:
					pyte_stream.feed(bytes_)
					print("bytes_ for pyte", bytes_)
					window['-terminal-'].update("\n".join(pyte_screen.display))
					# set cursor
					# TODO hide cursor in some cases?
					# for example, for terminal games like "ninvaders", a visible cursor is annoying
					#print("pyte_screen.cursor", pyte_screen.cursor.y, pyte_screen.cursor.x)
					window['-terminal-'].TKText.mark_set(tk.INSERT, f"{(pyte_screen.cursor.y + 1)}.{pyte_screen.cursor.x}")

			if master_fd in error_list:
				# TODO remove?
				print("shell_to_gui_pump: error master_fd")

	print("start thread: shell_to_gui_pump")
	threading.Thread(target=shell_to_gui_pump).start()



	# buffer. old code
	terminal_input = ""
	terminal_input_cursor_index = 0

	print("starting the main event loop")
	# While the application is running
	try:
		while True:
			eventAndValues: tuple[Any, dict[Any, Any] | list[Any]] = window.read()  # type: ignore
			# TODO(milahu) rename event to eventName
			event, values = eventAndValues

			# TODO refactor. replace all the if-s with dictionary/class of handler functions

			if event in (None, "Exit"):
				shell_process_exit = True
				# restore tty settings back
				shell_process.kill()
				sys.exit(0)

			#print(f"event = {event}") # debug
			#print(f"values = {values}") # verbose

			if event == "-terminal-+Key+":
				terminal = window['-terminal-']
				event = terminal.user_bind_event # event object
				#print(event) # debug
				if event.state == 4: # Control
					if event.char == "+": # Ctrl +
						print("Ctrl-+ = increase font size")
						# TODO
						continue
					if event.char == "-": # Ctrl -
						print("Ctrl-- = decrease font size")
						# TODO
						continue
				if event.state == 5: # Control Shift
					# note: event.keysym != event.char
					if event.keysym == "V": # Ctrl Shift v = paste
						gui_to_shell_string(pySimpleGui.clipboard_get())
						continue
					if event.keysym == "C": # Ctrl Shift c = copy
						# TODO get selection. quickfix: copy full terminal
						# rstrip all lines
                        # similar to pySimpleGui.Multiline(rstrip=True)
						text_stripped = ("".join([line.rstrip() + "\n" for line in pyte_screen.display])).strip() + "\n"
						pySimpleGui.clipboard_set(text_stripped)
						continue
					if event.keysym == "A":
						print("Ctrl-Shift-a = select all")
						# TODO select all
						continue
				# default: send to shell
				gui_to_shell_string(event.char)
				continue

			if event == "Copy": # rightclick copy
				# TODO get selection. quickfix: copy full terminal
				# rstrip all lines = remove useless whitespace
				text_stripped = ("".join([line.rstrip() + "\n" for line in pyte_screen.display])).strip() + "\n"
				pySimpleGui.clipboard_set(text_stripped)
				continue

			if event == "Paste": # rightclick paste
				gui_to_shell_string(pySimpleGui.clipboard_get())
				continue

			# TODO(milahu) maybe remove? handled by eventName == "-terminal-+Key+"?
			if event == "-terminal-+Return+":
				gui_to_shell_bytes(b"\r")
				continue

			if event == "-terminal-+BackSpace+":
				print("+BackSpace+")
				gui_to_shell_bytes(b"\x08")
				continue

			if event == "-terminal-+Tab+":
				gui_to_shell_bytes(b"\t")
				continue

			if event == "-terminal-+Up+":
				print("+Up+")
				# FIXME Up/Down are not working in "less"
				gui_to_shell_bytes(b"\033[A")
				continue

			if event == "-terminal-+Down+":
				print("+Down+")
				# FIXME Up/Down are not working in "less"
				gui_to_shell_bytes(b"\033[B")
				continue

			if event == "-terminal-+Right+":
				print("+Right+")
				# FIXME Left/Right are not working in "ninvaders" game
				gui_to_shell_bytes(b"\033[C")
				continue

			if event == "-terminal-+Left+":
				print("+Left+")
				gui_to_shell_bytes(b"\033[D")
				# FIXME Left/Right are not working in "ninvaders" game
				continue

			if event == "-terminal-+Button-1+": # ClickLeft
				# focus only. dont move cursor
				# TODO when text is selected (click drag release),
				# then single-click should unselect and move cursor back
				print("+Button-1+")
				window['-terminal-'].set_focus()
				continue

			continue # debug: dont handle the "Start" event = dont run the "run_function"

			# TODO add condition.
			if event == "+TODO+":
				try:
					# Create and open the popup window for the menu item
					if values is not None:
						print(f"try block")
						if 0 in values and values[0] is not None:
							print(f"try block 2")
							popup = generatePopup(buildSpec, values, widgets, pySimpleGui)
							print(f"try block 3")
							popup.read()  # type: ignore
							print(f"try block 4")
						print(f"try block 5")
						args = {}
						for key in values:
							if key != 0:
								args[key] = values[key]
						print(f"try block 6")
						args = argFormat(args, buildSpec["parser"]) # FIXME FileNotFoundError(2, 'No such file or directory')
						print(f"try block 7")
						if not buildSpec["run_function"]:
							print(f"try block 8")
							return args
						print(f"try block 9")
						print(f"args = {args}")
						buildSpec["run_function"](args)
						# TODO(milahu) send stdout and stderr to the GUI terminal
				except Exception as exception:  # pylint: disable=broad-except
					print(repr(exception))
					# TODO(milahu) send errors to GUI

	finally:
		shell_process_exit = True
