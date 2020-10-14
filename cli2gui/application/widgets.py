"""Widgets class holding methods to create widgets in addition to a sizes
attribute that can be overridden to provide the end user with customisation over
the size of the gui
"""
from __future__ import annotations

import io
from typing import Any, Union
import PySimpleGUI as pySimpleGuiType

from PIL import Image, ImageTk


class Widgets():
	"""Widgets class holding methods to create widgets in addition to a sizes
	attribute that can be overridden to provide the end user with customisation
	over the size of the gui
	"""
	def __init__(self, sizes: dict[str, Any], pySimpleGui: Any):
		self.sizes = sizes
		self.pySimpleGui = pySimpleGui

	"""Utility functions that manipulate images and text
	"""
	def getImgData(self, imagePath: Union[str, None], first: bool=False) -> Union[bytes, None]:
		"""Generate image data using PIL """
		if imagePath is None:
			return None
		img = Image.open(imagePath)
		img.thumbnail((self.sizes["title_size"]*3, self.sizes["title_size"]*3))
		if first:                     # tkinter is inactive the first time
			bio = io.BytesIO()
			img.save(bio, format="PNG")
			del img
			return bio.getvalue()
		return ImageTk.PhotoImage(img)
	def stringTitlecase(self, string: Union[str, None], splitStr: str="ALL"):
		'''Convert a string to title case '''
		if string is None:
			return ""
		titleCase = ""
		if len(string) > 0:
			if splitStr == "ALL":
				titleCase = " ".join((part[0].upper() + part[1:]) for part in
				string.replace("-", "_").split("_"))
			else:
				titleCase = " ".join((part[0].upper() + part[1:]) for part in string.split(splitStr))
		return titleCase

	def stringSentencecase(self, string: Union[str, None]) -> str:
		'''Convert a string to sentence case '''
		if string is None:
			return ""
		if len(string) > 0:
			return string[0].upper() + string[1:]
		return ""

	"""Individual widgets
	"""
	def inputText(self, key: str) -> pySimpleGuiType.Element:
		'''Return an input text field '''
		return self.pySimpleGui.InputText(size=self.sizes["input_size"],
		pad=self.sizes["padding"], key=key,
		font=("sans", self.sizes["text_size"]))
	def check(self, key: str) -> pySimpleGuiType.Element:
		'''Return a checkbox '''
		return self.pySimpleGui.Check("", size=self.sizes["input_size"],
		pad=self.sizes["padding"], key=key)
	def button(self, text: str) -> pySimpleGuiType.Element:
		'''Return a button '''
		return self.pySimpleGui.Button(text, size=self.sizes["button"], pad=self.sizes["padding"],
		font=("sans", self.sizes["text_size"]))
	def label(self, text: str, font: int=11) -> pySimpleGuiType.Element:
		'''Return a label '''
		return self.pySimpleGui.Text(text, size=(int(self.sizes["label_size"][0]*11/font),
		self.sizes["label_size"][1]), pad=self.sizes["padding"], font=("sans", font))
	def dropdown(self, key: str, arg_items: list[str]) -> pySimpleGuiType.Element:
		'''Return a dropdown '''
		return self.pySimpleGui.Drop(tuple(arg_items), size=self.sizes["input_size"], pad=self.sizes["padding"],
		key=key)
	def fileBrowser(self, key: str) -> list[pySimpleGuiType.Element]:
		'''Return a fileBrowser button and field '''
		height = self.sizes["input_size"][1]
		width = self.sizes["input_size"][0]
		return [self.pySimpleGui.InputText(size=(width - int(width/3), height),
		pad=(0, self.sizes["padding"][1]), key=key, font=("sans", self.sizes["text_size"])),
		self.pySimpleGui.FileBrowse(key=key+"#", size=(int(width/3), height), pad=(0, self.sizes["padding"][1]))]

	"""Different sized labels
	"""
	def helpArgName(self, displayName: str, commands: list[str]) -> pySimpleGuiType.Element:
		'''Return a label for the arg name '''
		return(self.label("- "+self.stringTitlecase(displayName)+": "+str(commands), 14))
	def helpArgHelp(self, helpText: str) -> pySimpleGuiType.Element:
		'''Return a label for the arg help text '''
		return self.label(self.stringSentencecase(helpText))
	def helpArgNameAndHelp(self, commands: list[str], helpText: str,
	displayName: str) -> pySimpleGuiType.Element:
		'''Return a column containing the argument name and help text'''
		return self.pySimpleGui.Column([[self.helpArgName(displayName, commands)],
		[self.helpArgHelp(helpText)]], pad=(0, 0))
	def title(self, text: str, image: Union[str, None]=None) -> list[pySimpleGuiType.Element]:
		'''Return a set of widgets that make up the application header '''
		programTitle = [self.pySimpleGui.Text(text, pad=self.sizes["padding"],
		font=("sans", self.sizes["title_size"]))]
		if image is not None:
			programTitle = [self.pySimpleGui.Image(data=self.getImgData(image, first=True)),
			self.pySimpleGui.Text(text, pad=self.sizes["padding"], font=("sans", self.sizes["title_size"]))]
		return programTitle

	"""Generate help widget group
	"""
	def helpFlagWidget(self, displayName: str, commands: list[str],
	helpText: str, dest: str) -> list[pySimpleGuiType.Element]:
		'''Return a set of widgets that make up an arg with true/ false'''
		return [self.helpArgNameAndHelp(commands, helpText, displayName),
		self.pySimpleGui.Column([[self.check(dest)]], pad=(0, 0))]
	def helpTextWidget(self, displayName: str, commands: list[str],
	helpText: str, dest: str) -> list[pySimpleGuiType.Element]:
		'''Return a set of widgets that make up an arg with text'''
		return [self.helpArgNameAndHelp(commands, helpText, displayName),
		self.pySimpleGui.Column([[self.inputText(dest)]], pad=(0, 0))]
	def helpFileWidget(self, displayName: str, commands: list[str],
	helpText: str, dest: str) -> list[pySimpleGuiType.Element]:
		'''Return a set of widgets that make up an arg with a file'''
		return [self.helpArgNameAndHelp(commands, helpText, displayName),
		self.pySimpleGui.Column([self.fileBrowser(dest)], pad=(0, 0))]
	def helpDropdownWidget(self, displayName: str, commands: list[str],
	helpText: str, dest: str, choices: list[str]) -> list[pySimpleGuiType.Element]:
		'''Return a set of widgets that make up an arg with a choice'''
		return [self.helpArgNameAndHelp(commands, helpText, displayName),
		self.pySimpleGui.Column([[self.dropdown(dest, choices)]], pad=(0, 0))]
