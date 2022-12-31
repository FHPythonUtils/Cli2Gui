"""Widgets class holding methods to create widgets in addition to a sizes.
attribute that can be overridden to provide the end user with customisation over
the size of the gui.
"""
from __future__ import annotations

import io
from typing import Any

from PIL import Image, ImageTk
from PySimpleGUI import Element

from cli2gui import types


class Widgets:
	"""Widgets class holding methods to create widgets in addition to a sizes.
	attribute that can be overridden to provide the end user with customisation
	over the size of the gui.
	"""

	def __init__(self, sizes: dict[str, Any], pySimpleGui: Any):
		self.sizes = sizes
		self.pySimpleGui = pySimpleGui

	"""Utility functions that manipulate images and text.
	"""

	def getImgData(self, imagePath: str, first: bool = False) -> bytes:
		"""Generate image data using PIL."""
		img = Image.open(imagePath)
		img.thumbnail((self.sizes["title_size"] * 3, self.sizes["title_size"] * 3))
		if first:  # tkinter is inactive the first time
			bio = io.BytesIO()
			img.save(bio, format="PNG")
			del img
			return bio.getvalue()
		return ImageTk.PhotoImage(img)  # type:ignore

	def stringTitlecase(self, string: str, splitStr: str = "ALL"):
		"""Convert a string to title case."""
		_ = self
		titleCase = ""
		if len(string) > 0:
			if splitStr == "ALL":
				titleCase = " ".join(
					(part[0].upper() + part[1:]) for part in string.replace("-", "_").split("_")
				)
			else:
				titleCase = " ".join(
					(part[0].upper() + part[1:]) for part in string.split(splitStr)
				)
		return titleCase

	def stringSentencecase(self, string: str) -> str:
		"""Convert a string to sentence case."""
		_ = self
		if string:
			return string[0].upper() + string[1:]
		return ""

	"""Individual widgets
	"""

	def inputText(self, key: str, default=None) -> Element:
		"""Return an input text field."""
		return self.pySimpleGui.InputText(
			default,
			size=self.sizes["input_size"],
			pad=self.sizes["padding"],
			key=key,
			font=("sans", self.sizes["text_size"]),
		)

	def spin(self, key: str, default=None) -> Element:
		"""Return an input text field."""
		return self.pySimpleGui.Spin(
			list(range(-50, 51)),
			initial_value=default or 0,
			size=self.sizes["input_size"],
			pad=self.sizes["padding"],
			key=key,
			font=("sans", self.sizes["text_size"]),
		)

	def check(self, key: str, default=None) -> Element:
		"""Return a checkbox."""
		return self.pySimpleGui.Check(
			"", size=self.sizes["input_size"], pad=self.sizes["padding"], key=key, default=default
		)

	def button(self, text: str) -> Element:
		"""Return a button."""
		return self.pySimpleGui.Button(
			text,
			size=self.sizes["button"],
			pad=self.sizes["padding"],
			font=("sans", self.sizes["text_size"]),
		)

	def label(self, text: str, font: int = 11) -> Element:
		"""Return a label."""
		return self.pySimpleGui.Text(
			text,
			size=(
				int(self.sizes["label_size"][0] * 11 / font),
				self.sizes["label_size"][1],
			),
			pad=self.sizes["padding"],
			font=("sans", font),
		)

	def dropdown(self, key: str, argItems: list[str]) -> Element:
		"""Return a dropdown."""
		return self.pySimpleGui.Drop(
			tuple(argItems),
			size=self.sizes["input_size"],
			pad=self.sizes["padding"],
			key=key,
		)

	def fileBrowser(self, key: str, default=None) -> list[Element]:
		"""Return a fileBrowser button and field."""
		height = self.sizes["input_size"][1]
		width = self.sizes["input_size"][0]
		return [
			self.pySimpleGui.InputText(
				default,
				size=(width - int(width / 3), height),
				pad=(0, self.sizes["padding"][1]),
				key=key,
				font=("sans", self.sizes["text_size"]),
			),
			self.pySimpleGui.FileBrowse(
				key=key + "#",
				size=(int(width / 3), height),
				pad=(0, self.sizes["padding"][1]),
			),
		]

	"""Different sized labels
	"""

	def helpArgName(self, displayName: str, commands: list[str]) -> Element:
		"""Return a label for the arg name."""
		return self.label("- " + self.stringTitlecase(displayName) + ": " + str(commands), 14)

	def helpArgHelp(self, helpText: str) -> Element:
		"""Return a label for the arg help text."""
		return self.label(self.stringSentencecase(helpText))

	def helpArgNameAndHelp(self, commands: list[str], helpText: str, displayName: str) -> Element:
		"""Return a column containing the argument name and help text."""
		return self.pySimpleGui.Column(
			[[self.helpArgName(displayName, commands)], [self.helpArgHelp(helpText)]],
			pad=(0, 0),
		)

	def title(self, text: str, image: str = "") -> list[Element]:
		"""Return a set of widgets that make up the application header."""
		programTitle = [
			self.pySimpleGui.Text(
				text, pad=self.sizes["padding"], font=("sans", self.sizes["title_size"])
			)
		]
		if image:
			programTitle = [
				self.pySimpleGui.Image(data=self.getImgData(image, first=True)),
				self.pySimpleGui.Text(
					text,
					pad=self.sizes["padding"],
					font=("sans", self.sizes["title_size"]),
				),
			]
		return programTitle

	"""Generate help widget group
	"""

	def helpFlagWidget(
		self,
		item: types.Item,
	) -> list[Element]:
		"""Return a set of widgets that make up an arg with true/ false."""
		return [
			self.helpArgNameAndHelp(item["commands"], item["help"], item["display_name"]),
			self.pySimpleGui.Column(
				[[self.check(item["dest"], default=item["default"])]], pad=(0, 0)
			),
		]

	def helpTextWidget(
		self,
		item: types.Item,
	) -> list[Element]:
		"""Return a set of widgets that make up an arg with text."""
		return [
			self.helpArgNameAndHelp(item["commands"], item["help"], item["display_name"]),
			self.pySimpleGui.Column(
				[[self.inputText(item["dest"], default=item["default"])]], pad=(0, 0)
			),
		]

	def helpCounterWidget(
		self,
		item: types.Item,
	) -> list[Element]:
		"""Return a set of widgets that make up an arg with text."""
		return [
			self.helpArgNameAndHelp(item["commands"], item["help"], item["display_name"]),
			self.pySimpleGui.Column(
				[[self.spin(item["dest"], default=item["default"])]], pad=(0, 0)
			),
		]

	def helpFileWidget(
		self,
		item: types.Item,
	) -> list[Element]:
		"""Return a set of widgets that make up an arg with a file."""
		return [
			self.helpArgNameAndHelp(item["commands"], item["help"], item["display_name"]),
			self.pySimpleGui.Column([self.fileBrowser(item["dest"], item["default"])], pad=(0, 0)),
		]

	def helpDropdownWidget(
		self,
		item: types.Item,
	) -> list[Element]:
		"""Return a set of widgets that make up an arg with a choice."""
		return [
			self.helpArgNameAndHelp(item["commands"], item["help"], item["display_name"]),
			self.pySimpleGui.Column(
				[[self.dropdown(item["dest"], item["_other"]["choices"])]], pad=(0, 0)
			),
		]

	def addWidgetFromItem(self, item: types.Item) -> list[Element]:
		"""Add a widget from an item (types.Item)"""
		functionMap = {
			types.ItemType.Bool: self.helpFlagWidget,
			types.ItemType.File: self.helpFileWidget,
			types.ItemType.Choice: self.helpDropdownWidget,
			types.ItemType.Int: self.helpCounterWidget,
			types.ItemType.Text: self.helpTextWidget,
		}
		return functionMap[item["type"]](
			item,
		)
