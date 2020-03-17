"""Widgets class holding methods to create widgets in addition to a sizes
attribute that can be overridden to provide the end user with customisation over
the size of the gui
"""
import io

from PIL import Image, ImageTk


class Widgets():
	"""Widgets class holding methods to create widgets in addition to a sizes
	attribute that can be overridden to provide the end user with customisation
	over the size of the gui
	"""
	def __init__(self, sizes, sg):
		self.SIZES = sizes
		self.sg = sg

	"""Utility functions that manipulate images and text
	"""
	def get_img_data(self, f, first=False):
		"""Generate image data using PIL """
		img = Image.open(f)
		img.thumbnail((self.SIZES["title_size"]*3, self.SIZES["title_size"]*3))
		if first:                     # tkinter is inactive the first time
			bio = io.BytesIO()
			img.save(bio, format="PNG")
			del img
			return bio.getvalue()
		return ImageTk.PhotoImage(img)
	def stringTitlecase(self, string, splitStr="ALL"):
		'''Convert a string to title case '''
		titleCase = ""
		try:
			if splitStr == "ALL":
				titleCase = " ".join((part[0].upper() + part[1:]) for part in
				string.replace("-", "_").split("_"))
			else:
				titleCase = " ".join((part[0].upper() + part[1:]) for part in string.split(splitStr))
		except (IndexError, TypeError):
			titleCase = ""
		return titleCase

	def stringSentencecase(self, string):
		'''Convert a string to sentence case '''
		try:
			return string[0].upper() + string[1:]
		except (IndexError, TypeError):
			return ""

	"""Individual widgets
	"""
	def inputText(self, key):
		'''Return an input text field '''
		return self.sg.InputText(size=self.SIZES["input_size"], pad=self.SIZES["padding"], key=key,
		font=("sans", self.SIZES["text_size"]))
	def check(self, key):
		'''Return a checkbox '''
		return self.sg.Check("", size=self.SIZES["input_size"], pad=self.SIZES["padding"], key=key)
	def button(self, text):
		'''Return a button '''
		return self.sg.Button(text, size=self.SIZES["button"], pad=self.SIZES["padding"],
		font=("sans", self.SIZES["text_size"]))
	def label(self, text, font=11):
		'''Return a label '''
		return self.sg.Text(text, size=(int(self.SIZES["label_size"][0]*11/font),
		self.SIZES["label_size"][1]), pad=self.SIZES["padding"], font=("sans", font))
	def dropdown(self, key, items):
		'''Return a dropdown '''
		return self.sg.Drop(tuple(items), size=self.SIZES["input_size"], pad=self.SIZES["padding"],
		key=key)
	def fileBrowser(self, key):
		'''Return a fileBrowser button and field '''
		height = self.SIZES["input_size"][1]
		width = self.SIZES["input_size"][0]
		return [self.sg.InputText(size=(width - int(width/3), height),
		pad=(0, self.SIZES["padding"][1]), key=key, font=("sans", self.SIZES["text_size"])),
		self.sg.FileBrowse(key=key+"#", size=(int(width/3), height), pad=(0, self.SIZES["padding"][1]))]

	"""Different sized labels
	"""
	def helpArgName(self, display_name, commands):
		'''Return a label for the arg name '''
		return(self.label("- "+self.stringTitlecase(display_name)+": "+str(commands), 14))
	def helpArgHelp(self, helpText):
		'''Return a label for the arg help text '''
		return self.label(self.stringSentencecase(helpText))
	def helpArgNameAndHelp(self, commands, helpText, display_name):
		'''Return a column containing the argument name and help text'''
		return self.sg.Column([[self.helpArgName(display_name, commands)],
		[self.helpArgHelp(helpText)]], pad=(0, 0))
	def title(self, text, image=None):
		'''Return a set of widgets that make up the application header '''
		programTitle = [self.sg.Text(text, pad=self.SIZES["padding"],
		font=("sans", self.SIZES["title_size"]))]
		if image is not None:
			programTitle = [self.sg.Image(data=self.get_img_data(image, first=True)),
			self.sg.Text(text, pad=self.SIZES["padding"], font=("sans", self.SIZES["title_size"]))]
		return programTitle

	"""Generate help widget group
	"""
	def helpFlagWidget(self, display_name, commands, helpText, dest):
		'''Return a set of widgets that make up an arg with true/ false'''
		return [self.helpArgNameAndHelp(commands, helpText, display_name),
		self.sg.Column([[self.check(dest)]], pad=(0, 0))]
	def helpTextWidget(self, display_name, commands, helpText, dest):
		'''Return a set of widgets that make up an arg with text'''
		return [self.helpArgNameAndHelp(commands, helpText, display_name),
		self.sg.Column([[self.inputText(dest)]], pad=(0, 0))]
	def helpFileWidget(self, display_name, commands, helpText, dest):
		'''Return a set of widgets that make up an arg with a file'''
		return [self.helpArgNameAndHelp(commands, helpText, display_name),
		self.sg.Column([self.fileBrowser(dest)], pad=(0, 0))]
	def helpDropdownWidget(self, display_name, commands, helpText, dest, choices):
		'''Return a set of widgets that make up an arg with a choice'''
		return [self.helpArgNameAndHelp(commands, helpText, display_name),
		self.sg.Column([[self.dropdown(dest, choices)]], pad=(0, 0))]
