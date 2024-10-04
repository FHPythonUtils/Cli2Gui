from __future__ import annotations

import io
import logging
from typing import TYPE_CHECKING, Any, Callable

from PIL import Image, ImageTk

from cli2gui import types
from cli2gui.gui import helpers
from cli2gui.gui.abstract_gui import AbstractGUI

if TYPE_CHECKING:
	import FreeSimpleGUI as gui_lib


class PySimpleGUIWrapper(AbstractGUI):
	"""Wrapper class for PySimpleGUI."""

	def __init__(self, base24Theme: list[str], psg_lib: str) -> None:
		super().__init__()

		if psg_lib == "pysimplegui":
			import PySimpleGUI as gui_lib
		elif psg_lib == "pysimpleguiqt":
			import PySimpleGUIQt as gui_lib
		elif psg_lib == "pysimpleguiweb":
			import PySimpleGUIWeb as gui_lib
		else:
			import FreeSimpleGUI as gui_lib

		self.sg = gui_lib
		self.psg_lib = psg_lib
		self.sizes = {
			"title_size": 18,
			"label_size": (30, None),
			"input_size": (30, 1),
			"button": (10, 1),
			"padding": (5, 10),
			"help_text_size": 14,
			"text_size": 11,
		}

		if psg_lib not in ["pysimplegui", "freesimplegui"]:
			self.sizes = {
				"title_size": 18,
				"label_size": (600, None),
				"input_size": (30, 1),
				"button": (10, 1),
				"padding": (5, 10),
				"help_text_size": 14,
				"text_size": 11,
			}
		accent = {"red": 8, "blue": 13, "green": 11, "purple": 14}
		self.sg.LOOK_AND_FEEL_TABLE["theme"] = {
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
		self.sg.theme("theme")

	def _inputText(self, key: str, default: str | None = None) -> gui_lib.Element:
		"""Return an input text field."""
		return self.sg.InputText(
			default or "",
			size=self.sizes["input_size"],
			pad=self.sizes["padding"],
			key=key,
			font=("sans", self.sizes["text_size"]),
		)

	def _spin(self, key: str, default: str | None = None) -> gui_lib.Element:
		"""Return an input text field."""
		return self.sg.Spin(
			list(range(-50, 51)),
			initial_value=default or 0,
			size=self.sizes["input_size"],
			pad=self.sizes["padding"],
			key=key,
			font=("sans", self.sizes["text_size"]),
		)

	def _check(self, key: str, default: str | None = None) -> gui_lib.Element:
		"""Return a checkbox."""
		return self.sg.Check(
			"",
			size=self.sizes["input_size"],
			pad=self.sizes["padding"],
			key=key,
			default=bool(default or ""),
		)

	def _button(self, text: str) -> gui_lib.Element:
		"""Return a button."""
		return self.sg.Button(
			text,
			size=self.sizes["button"],
			pad=self.sizes["padding"],
			font=("sans", self.sizes["text_size"]),
		)

	def _label(self, text: str, font: int = 11) -> gui_lib.Element:
		"""Return a label."""
		return self.sg.Text(
			text,
			size=(
				int(self.sizes["label_size"][0] * 11 / font),
				self.sizes["label_size"][1],
			),
			pad=self.sizes["padding"],
			font=("sans", font),
		)

	def _dropdown(self, key: str, argItems: list[str]) -> gui_lib.Element:
		"""Return a dropdown."""
		return self.sg.Drop(
			tuple(argItems),
			size=self.sizes["input_size"],
			pad=self.sizes["padding"],
			key=key,
		)

	def _fileBrowser(self, key: str, default: str | None = None) -> list[gui_lib.Element]:
		"""Return a fileBrowser button and field."""
		height = self.sizes["input_size"][1]
		width = self.sizes["input_size"][0]
		fb: list[gui_lib.Element] = [
			self.sg.InputText(
				default or "",
				size=(width - int(width / 3), height),
				pad=(0, self.sizes["padding"][1]),
				key=key,
				font=("sans", self.sizes["text_size"]),
			),
			self.sg.FileBrowse(
				key=key + "#",
				size=(int(width / 3), height),
				pad=(0, self.sizes["padding"][1]),
			),
		]
		return fb

	"""Different sized labels
	"""

	def _helpArgName(self, displayName: str, commands: list[str]) -> gui_lib.Element:
		"""Return a label for the arg name."""
		return self._label("- " + helpers.stringTitlecase(displayName) + ": " + str(commands), 14)

	def _helpArgHelp(self, helpText: str) -> gui_lib.Element:
		"""Return a label for the arg help text."""
		return self._label(helpers.stringSentencecase(helpText))

	def _helpArgNameAndHelp(
		self, commands: list[str], helpText: str, displayName: str
	) -> gui_lib.Element:
		"""Return a column containing the argument name and help text."""
		return self.sg.Column(
			[[self._helpArgName(displayName, commands)], [self._helpArgHelp(helpText)]],
			pad=(0, 0),
		)

	def _title(self, text: str, image: str = "") -> list[gui_lib.Element]:
		"""Return a set of self that make up the application header."""
		programTitle: list[gui_lib.Element] = [
			self.sg.Text(text, pad=self.sizes["padding"], font=("sans", self.sizes["title_size"]))
		]
		if image:
			programTitle = [
				self.sg.Image(data=self.getImgData(image, first=True)),
				self.sg.Text(
					text,
					pad=self.sizes["padding"],
					font=("sans", self.sizes["title_size"]),
				),
			]
		return programTitle

	"""Generate help widget group
	"""

	def _helpFlagWidget(
		self,
		item: types.Item,
	) -> list[gui_lib.Element]:
		"""Return a set of self that make up an arg with true/ false."""
		return [
			self._helpArgNameAndHelp(item["commands"], item["help"], item["display_name"]),
			self.sg.Column([[self._check(item["dest"], default=item["default"])]], pad=(0, 0)),
		]

	def _helpTextWidget(
		self,
		item: types.Item,
	) -> list[gui_lib.Element]:
		"""Return a set of self that make up an arg with text."""
		return [
			self._helpArgNameAndHelp(item["commands"], item["help"], item["display_name"]),
			self.sg.Column([[self._inputText(item["dest"], default=item["default"])]], pad=(0, 0)),
		]

	def _helpCounterWidget(
		self,
		item: types.Item,
	) -> list[gui_lib.Element]:
		"""Return a set of self that make up an arg with text."""
		return [
			self._helpArgNameAndHelp(item["commands"], item["help"], item["display_name"]),
			self.sg.Column([[self._spin(item["dest"], default=item["default"])]], pad=(0, 0)),
		]

	def _helpFileWidget(
		self,
		item: types.Item,
	) -> list[gui_lib.Element]:
		"""Return a set of self that make up an arg with a file."""
		return [
			self._helpArgNameAndHelp(item["commands"], item["help"], item["display_name"]),
			self.sg.Column([self._fileBrowser(item["dest"], item["default"])], pad=(0, 0)),
		]

	def _helpDropdownWidget(
		self,
		item: types.Item,
	) -> list[gui_lib.Element]:
		"""Return a set of self that make up an arg with a choice."""
		return [
			self._helpArgNameAndHelp(item["commands"], item["help"], item["display_name"]),
			self.sg.Column(
				[[self._dropdown(item["dest"], item["additional_properties"]["choices"])]],
				pad=(0, 0),
			),
		]

	def addWidgetFromItem(self, item: types.Item) -> list[gui_lib.Element]:
		"""Select a widget based on the item type.

		:param types.Item item: the item
		"""
		functionMap = {
			types.ItemType.Bool: self._helpFlagWidget,
			types.ItemType.File: self._helpFileWidget,
			types.ItemType.Choice: self._helpDropdownWidget,
			types.ItemType.Int: self._helpCounterWidget,
			types.ItemType.Text: self._helpTextWidget,
		}
		if item["type"] in functionMap:
			return functionMap[item["type"]](
				item,
			)
		return []

	def generatePopup(
		self,
		buildSpec: types.FullBuildSpec,
		values: dict[Any, Any] | list[gui_lib.Element],
	) -> gui_lib.Window:
		"""Create the popup window.

		Args:
		----
			buildSpec (types.FullBuildSpec): [description]
			values (Union[dict[Any, Any]): Returned when a button is clicked. Such
			as the menu

		Returns:
		-------
			Window: A PySimpleGui Window

		"""
		maxLines = 30 if self.psg_lib == "pysimpleguiqt" else 200
		popupText = helpers.read_file(buildSpec["menu"][values[0]], maxLines)

		if self.psg_lib == "pysimplegui":
			popupLayout = [
				self._title(values[0]),
				[
					self.sg.Column(
						[
							[
								self.sg.Text(
									text=popupText,
									size=(850, maxLines + 10),
									font=("Courier", self.sizes["text_size"]),
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
				self._title(values[0]),
				[
					self.sg.Text(
						text=popupText,
						size=(850, (self.sizes["text_size"]) * (2 * maxLines + 10)),
						font=("Courier", self.sizes["text_size"]),
					)
				],
			]
		return self.sg.Window(
			values[0],
			popupLayout,
			alpha_channel=0.95,
			icon=self.getImgData(buildSpec["image"], first=True) if buildSpec["image"] else None,
		)

	def addItemsAndGroups(
		self,
		section: types.Group,
	) -> list[list[gui_lib.Element]]:
		"""Items and groups and return a list of psg Elements.

		:param types.Group section: section with a name to display and items
		:return list[list[Element]]: updated argConstruct

		"""

		argConstruct: list[list[gui_lib.Element]] = []

		argConstruct.append([self._label(helpers.stringTitlecase(section["name"], " "), 14)])
		for item in section["arg_items"]:
			if item["type"] == types.ItemType.RadioGroup:
				rGroup = item["additional_properties"]["radio"]
				for rElement in rGroup:
					argConstruct.append(self.addWidgetFromItem(rElement))
			else:
				argConstruct.append(self.addWidgetFromItem(item))
		for group in section["groups"]:
			argConstruct.extend(self.addItemsAndGroups(group))
		return argConstruct

	def createLayout(
		self,
		buildSpec: types.FullBuildSpec,
		menu: str | list[str],
	) -> list[list[gui_lib.Element]]:
		"""Create the pysimplegui layout from the build spec.

		Args:
		----
			buildSpec (types.FullBuildSpec): build spec containing widget
			self (self): class to build self


		Returns:
		-------
			list[list[gui_lib.Element]]: list of self (layout list)

		"""
		argConstruct = []
		for widget in buildSpec["widgets"]:
			argConstruct.extend(self.addItemsAndGroups(widget))

		# Set the layout
		layout: list[list[gui_lib.Element]] = [[]]
		if isinstance(menu, list):
			layout: list[list[gui_lib.Element]] = [[self.sg.Menu([["Open", menu]], tearoff=True)]]

		layout.extend(
			[
				self._title(str(buildSpec["program_name"]), buildSpec["image"]),
				[
					self._label(
						helpers.stringSentencecase(
							buildSpec["program_description"]
							if buildSpec["program_description"]
							else buildSpec["parser_description"]
						)
					)
				],
			]
		)
		if len(argConstruct) > buildSpec["max_args_shown"] and self.psg_lib in ("pysimplegui", "freesimplegui"):
			layout.append(
				[
					self.sg.Column(
						argConstruct,
						size=(
							850,
							min(
								max(
									280,
									buildSpec["max_args_shown"]
									* 3.5
									* (self.sizes["help_text_size"] + self.sizes["text_size"]),
								),
								700,
							),
						),
						pad=(0, 0),
						scrollable=True,
						vertical_scroll_only=True,
					)
				]
			)
		else:
			layout.extend(argConstruct)
		layout.append([self._button("Run"), self._button("Exit")])
		return layout

	def main(
		self,
		buildSpec: types.FullBuildSpec,
		quit_callback: Callable[[], None],
		run_callback: Callable[[dict[str, Any]], None],
	) -> None:
		"""Run the gui (psg) with a given buildSpec, quit_callback, and run_callback.

		:param types.FullBuildSpec buildSpec: Full cli parse/ build spec
		:param Callable[[], None] quit_callback: generic callable used to quit
		:param Callable[[dict[str, Any]], None] run_callback: generic callable used to run
		"""
		menu = list(buildSpec["menu"]) if buildSpec["menu"] else ""

		layout = self.createLayout(buildSpec=buildSpec, menu=menu)

		# Build window from args
		window = self.sg.Window(
			buildSpec["program_name"],
			layout,
			alpha_channel=0.95,
			icon=self.getImgData(buildSpec["image"], first=True) if buildSpec["image"] else None,
		)

		# While the application is running
		while True:
			eventAndValues: tuple[Any, dict[Any, Any] | list[gui_lib.Element]] = window.read()
			event, values = eventAndValues
			if event in (None, "Exit"):
				quit_callback()
			try:
				# Create and open the popup window for the menu item
				if values is not None:
					if 0 in values and values[0] is not None:
						popup = self.generatePopup(buildSpec, values)
						popup.read()
					args = {}
					for key in values:
						if key != 0:
							args[key] = values[key]
					run_callback(args)

			except Exception:
				logging.exception("Something went wrong: ")

	def getImgData(self, imagePath: str, *, first: bool = False) -> bytes:
		"""Generate image data using PIL."""
		img = Image.open(imagePath)
		img.thumbnail((self.sizes["title_size"] * 3, self.sizes["title_size"] * 3))
		if first:  # tkinter is inactive the first time
			bio = io.BytesIO()
			img.save(bio, format="PNG")
			del img
			return bio.getvalue()
		return ImageTk.PhotoImage(img)  # type:ignore[type-error]
