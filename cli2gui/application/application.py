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
import shlex
import logging
import io

# short loglevel names
# https://github.com/python/cpython/blob/677320348728ce058fa3579017e985af74a236d4/Lib/logging/__init__.py#L100
#logging._levelToName = { 0: 'N', 10: 'D', 20: 'I', 30: 'W', 40: 'E', 50: 'C' }
#logging_levels_pretty = ["Debug", "Info", "Warning", "Error", "Critical"]

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
num_history_lines = 100 # aka "scrollback buffer size"
#num_history_lines = 1000 # more = slower, because not optimized

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
					pySimpleGui.Tab(
						'Log',
						widgets.loggingWidget(
							key="-log-",
						),
						#visible=False,
						key='-TabLog-'
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


def init_logger():
	log = logging.getLogger('cli2gui')
	log.setLevel(logging.DEBUG)
	# debug by default. makes it easier for users to report bugs

	log._stderr_handler = logging.StreamHandler() # default stream: sys.stderr
	log.addHandler(log._stderr_handler)

	log._string_stream = io.StringIO()
	log._string_handler = logging.StreamHandler(stream=log._string_stream)
	log.addHandler(log._string_handler)

	log_formatter = logging.Formatter(
		# message format:
		#'%(asctime)s - %(name)s - %(levelname)s - %(message)s',
		#'%(relativeCreatedStr)s %(levelname)s %(message)s',
		'%(asctime)s %(levelname)-5s %(message)s' + "\n", # "-5s" -> align INFO and DEBUG/ERROR messages
		# extra newline: make the log easier to read with wrapped lines
		# time format:
		#"%Y-%m-%d %H:%M:%S",
		"%H:%M:%S",
	)
	[h.setFormatter(log_formatter) for h in log.handlers]

	log.info("cli2gui version 2022.1")
	# TODO get version from pyproject.toml or from installed files

	#log.info("log levels: " + "".join([l[0] for l in logging_levels_pretty]) + " = " + " ".join(logging_levels_pretty))
	# TODO list only the active levels

	#log.info("writing logfile: /path/to/cli2gui.log") # TODO

	# logger test
	if False:
		log.debug('debug message')
		log.info('info message')
		log.warning('warn message')
		log.error('error message')
		log.critical('critical message')

	# make the logger methods behave like print()
	def wrap_log_method(log_method):
		def new_log(*args, **kwargs):
			# https://stackoverflow.com/a/39823534/10440128
			f = io.StringIO()
			print(*args, file=f, end="", **kwargs)
			string = f.getvalue()
			f.close()
			log_method(string)
		return new_log
	log.debug = wrap_log_method(log.debug)
	log.info = wrap_log_method(log.info)
	log.warning = wrap_log_method(log.warning)
	log.error = wrap_log_method(log.error)

	return log


def run(buildSpec: c2gtypes.FullBuildSpec):
	"""Main entry point for the application.

	Args:
		buildSpec (c2gtypes.FullBuildSpec): args that customise the application such as the theme
		or the function to run
	"""

	log = init_logger()

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

	log.removeHandler(log._string_handler)
	window['-log-'].update(log._string_stream.getvalue())
	log._string_stream = None
	log._stderr_handler.setStream(sys.stderr) # use the new sys.stderr

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
	window['-terminal-'].bind("<Button-2>", "+Button-2+", propagate=False) # ClickMiddle
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

	# default prompt (PS1) is too long
	log.debug("set PS1")
	#gui_to_shell_bytes(b"PS1='$ '\r")
	gui_to_shell_bytes(b"PS1='\\n$ '\r") # add newline before prompt
	gui_to_shell_bytes(b"clear\r") # NOTE clear will delete history

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

	#log.info("start thread: read_stdout")
	#threading.Thread(target=read_stdout).start()
	#log.info("start thread: read_stderro")
	#threading.Thread(target=read_stderro).start()

	# ansi terminal emulator
	#pyte_screen = pyte.Screen(terminal_width, terminal_height)
	# based on pyte/examples/history.py
	pyte_screen = pyte.HistoryScreen(terminal_width, terminal_height, history=num_history_lines, ratio=1)
	pyte_screen.set_mode(pyte.modes.LNM) # TODO what is LNM?

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
				#log.info("shell_to_gui_pump: read master_fd = pump from shell_process to GUI:", repr(bytes_))
				if bytes_:
					pyte_stream.feed(bytes_)
					#sys.stdout.write(bytes_) # debug: show output also in terminal # TODO not working?
					#log.debug("bytes_ for pyte", bytes_)
					#window['-terminal-'].update("\n".join(pyte_screen.display)) # send only last page to gui
					# send multiple pages to gui
					# test command: seq 1 100
					# FIXME "Copy" should copy all pages
					#term_text = "\n".join(pyte_screen.display)
					term_lines = pyte_screen.display[:] # copy array
					last_history_position = pyte_screen.history.position
					num_history_pages = int(num_history_lines / terminal_height)
					for _history_idx in range(num_history_pages): # TODO while loop
						pyte_screen.prev_page()
						history_page_lines = last_history_position - pyte_screen.history.position
						#log.info("history_page_lines", history_page_lines)
						#term_text = "\n".join(pyte_screen.display) + "\n" + term_text
						term_lines = pyte_screen.display[0:history_page_lines] + term_lines
						if history_page_lines < terminal_height:
							# last history page
							break
						last_history_position = pyte_screen.history.position
					if False:
						# debug. verbose
						for line_idx, line in enumerate(term_lines):
							log.info(f"{line_idx:4d} {line} ¶")
					window['-terminal-'].update("\n".join(term_lines))

					# set cursor
					# TODO hide cursor in some cases?
					# for example, for terminal games like "ninvaders", a visible cursor is annoying
					#log.info("pyte_screen.cursor", pyte_screen.cursor.y, pyte_screen.cursor.x)
					cursor_y_offset = len(term_lines) - terminal_height
					cursor_y = cursor_y_offset + pyte_screen.cursor.y
					window['-terminal-'].TKText.mark_set(tk.INSERT, f"{(cursor_y + 1)}.{pyte_screen.cursor.x}")

			if master_fd in error_list:
				# TODO remove?
				log.info("shell_to_gui_pump: error master_fd")

	#log.info("start thread: shell_to_gui_pump")
	threading.Thread(target=shell_to_gui_pump).start()


	log.info("starting the main event loop")
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

			#log.debug(f"event = {event}")
			#log.debug(f"values = {values}")

			if event == "-terminal-+Key+":
				terminal = window['-terminal-']
				event = terminal.user_bind_event # event object
				#log.debug("Key", event)
				#log.debug(event) # debug
				# NOTE escape codes: run `showkey -a` in a terminal and press keys, to find escape codes
				if event.state == 0:
					# no modifiers
					if event.keycode == 112:
						# prev page = page up
						log.debug("PageUp")
						gui_to_shell_bytes(b"\033[5~")
						continue
					if event.keycode == 117:
						# next page = page down
						log.debug("PageDown")
						gui_to_shell_bytes(b"\033[6~")
						continue
				if event.state == 4: # Control
					if event.char == "+": # Ctrl +
						log.debug("Ctrl-+ = increase font size")
						# TODO
						continue
					if event.char == "-": # Ctrl -
						log.debug("Ctrl-- = decrease font size")
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
						# FIXME copy should copy the full history
						# FIXME copy should copy the unwrapped lines
						#lines = pyte_screen.display # only one page
						lines = window['-terminal-'].get().split("\n")
						text_stripped = ("".join([line.rstrip() + "\n" for line in lines])).strip() + "\n"
						pySimpleGui.clipboard_set(text_stripped)
						continue
					if event.keysym == "A":
						log.debug("Ctrl-Shift-a = select all")
						# TODO select all
						continue
				# default: send to shell
				gui_to_shell_string(event.char)
				continue

			if event == "Copy": # rightclick copy
				# TODO get selection. quickfix: copy full terminal
				# rstrip all lines = remove useless whitespace
				# FIXME copy should copy the full history
				# FIXME copy should copy the unwrapped lines
				#lines = pyte_screen.display # only one page
				lines = window['-terminal-'].get().split("\n")
				text_stripped = ("".join([line.rstrip() + "\n" for line in lines])).strip() + "\n"
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
				log.debug("+BackSpace+")
				gui_to_shell_bytes(b"\x08")
				continue

			if event == "-terminal-+Tab+":
				gui_to_shell_bytes(b"\t")
				continue

			if event == "-terminal-+Up+":
				log.debug("+Up+")
				gui_to_shell_bytes(b"\033OA")
				continue

			if event == "-terminal-+Down+":
				log.debug("+Down+")
				gui_to_shell_bytes(b"\033OB")
				continue

			# TODO also send "Ctrl Right" and "Ctrl Left"
			if event == "-terminal-+Right+":
				log.debug("+Right+")
				gui_to_shell_bytes(b"\033OC")
				continue

			if event == "-terminal-+Left+":
				log.debug("+Left+")
				gui_to_shell_bytes(b"\033OD")
				continue


			if event == "-terminal-+Button-1+": # ClickLeft
				# focus only. dont move cursor
				# TODO when text is selected (click drag release),
				# then single-click should unselect and move cursor back
				# TODO when the "right click menu" is open, close it
				log.debug("+Button-1+")
				window['-terminal-'].set_focus()
				continue

			if event == "-terminal-+Button-2+": # ClickMiddle
				log.debug("+Button-2+ -> ignore")
				# on linux, this is "paste from primary selection"
				# probably this would confuse windows users
				continue

			if event == "Run":
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
						log.debug(f"build arguments")
						args = argFormat(args, buildSpec["parser"]) # FIXME FileNotFoundError(2, 'No such file or directory')
						if not buildSpec["run_function"]:
							return args

						log.debug("sys.argv", sys.argv)
						# TODO build list of arguments -> my work on Gooey?
						# TODO shlex = escape arguments for shell
						# TODO run this on start of cli2gui as santiy check -> throw early
						argv0_mode = os.stat(sys.argv[0]).st_mode & 0o777 # filter last 3 digits
						log.debug(f"argv[0] mode {oct(argv0_mode)} & 0o111 = {oct(argv0_mode & 0o111)}")
						argv0_is_exe = (os.stat(sys.argv[0]).st_mode & 0o111) == 0o111

						window['-TabOutput-'].select()

						if argv0_is_exe:
							log.debug("argv is exe")
							# simple
							gui_to_shell_string(f"""{sys.argv[0]} --help\r""") # test
						else:
							# TODO what would python do?
							# -> setup.py -> entry_points, console_scripts -> bash wrapper calling "python -m ..."
							log.debug("argv0 is python script or module")
							# argv0 is python script or module
							# goal:
							# PYTHONPATH="$PYTHONPATH:/home/user/src/nixos/milahu--nixos-packages/nur-packages/pkgs/autosub-by-abhirooptalasila/src/Cli2Gui" python3 -m cli2gui.cli2gui-demo
							log.debug("sys.executable", sys.executable)
							argv0 = sys.argv[0]
							python_exe = sys.executable
							module_dir = os.path.dirname(argv0)
							parts = list(os.path.split(module_dir))
							module_dir = None
							module_name = None
							while parts:
								log.debug("module root candidate", "/".join(parts + ["__init__.py"]))
								if os.path.exists("/".join(parts + ["__init__.py"])):
									log.debug("module root candidate exists")
									module_dir = "/".join(parts[0:-1])
									module_name = parts[-1]
									break
								parts.pop()
							if module_name:
								#argv_str = "--help"
								module_name += "." + os.path.basename(argv0)[:-3] # -3 = remove .py
								log.debug("module_dir", module_dir)
								log.debug("module_name", module_name)
								log.debug("values", values)
								argv_list = ["--file", values["file"]]
								argv_str = shlex.join(argv_list)
								# wrap the module call in a shell function
								sh_function_name = os.path.basename(argv0)
								if sh_function_name in {"main.py", "__main__.py", "__init__.py", "cli.py", "gui.py", "run.py", "index.py", "default.py"}:
									# use a better name
									sh_function_name = os.path.dirname(argv0) + "/" + sh_function_name

								sh_function = "\r".join([
									sh_function_name + "() {",
									f'  PYTHONPATH="$PYTHONPATH:{module_dir}" {python_exe} -m {module_name} "$@"',
									"}",
								]) + "\r"
								gui_to_shell_string(sh_function)
								gui_to_shell_string("clear\r") # hide the function declaration # NOTE clear will delete history
								log.info("run command in shell:", f"{sh_function_name} {argv_str}")
								gui_to_shell_string(f"{sh_function_name} {argv_str}\r") # run command
							else:
								log.info(f"FIXME could not find module_dir and module_name from argv0 = {argv0}")

						# old code: call the function directly
						# problem: no process control (Ctrl c), no real terminal (just output)
						if False:
							log.info(f"args = {args}")
							buildSpec["run_function"](args)
							# TODO(milahu) send stdout and stderr to the GUI terminal
							log.info(f"run_function done")
				except Exception as exception:  # pylint: disable=broad-except
					log.info(repr(exception))

	except BaseException as e:
		# note: BaseException includes *all* exceptions,
		# also GeneratorExit, KeyboardInterrupt, SystemExit
		# -> python exceptions class hierarchy
		raise e
	finally:
		shell_process_exit = True
