"""Convert a pandoc string to plaintext
"""
import art
import re
import emoji

def toPlaintext(inline):
	"""Convert an inline or block to plain text

	Args:
		inline (dict): An inline holds various types such as 'Space', 'Bold'
		and other Inlines

	Returns:
		string: plain text
	"""
	if inline["t"] == "Space":
		return " "
	if inline["t"] == "Str":
		# text
		return emoji.emojize(inline["c"])
	if inline["t"] in ["Emph", "Strong", "Strikeout", "Superscript", "Subscript", "SmallCaps"]:
		# inline[]
		text = []
		for newInline in inline["c"]:
			text.append(toPlaintext(newInline))
		return "".join(text)
	if inline["t"] == "Quoted":
		# quotetype, inline[]
		text = []
		for newInline in inline["c"][1]:
			text.append("\'" + toPlaintext(newInline) + "\'")
		return "".join(text)
	if inline["t"] == "Code":
		return " │" + inline["c"][1] + " │ "
	if inline["t"] in ["Plain", "Para"]:
		# inline[]
		text = []
		for newInline in inline["c"]:
			text.append(toPlaintext(newInline))
		return "".join(text)
	if inline["t"] in ["SoftBreak", "LineBreak"]:
		return "\n"
	if inline["t"] == "Link":
		return inline["c"][2][0]
	if inline["t"] == "RawInline":
		return inline["c"][1]
	print(inline)



def processRaw(content, pandoc2):
	"""Process raw data - this might be html

	Args:
		content ([string, string]): content type and content data
		pandoc2 (object): pandoc2XYZ object formatter
	"""
	if content[0] in ["html"]:
		if content[1].startswith("<img"):
			pandoc2.catImage(re.findall(r"src=\"(.*?)\"", content[1])[0])
		elif content[1].startswith("<!--"):
			pass
		else:
			pandoc2.print(content)
	else:
		pandoc2.print(content)

def processInline(inline, pandoc2):
	"""Do stuff for an inline object

	Args:
		inline (dict): An inline holds various types such as 'Space', 'Bold'
		and other Inlines
		pandoc2 (object): pandoc2XYZ object formatter
	"""
	if inline["t"] == "Str":
		# text
		pandoc2.print(emoji.emojize(inline["c"]), end="")
	if inline["t"] == "Emph":
		# inline[]
		pandoc2.emph(inline["c"])
	if inline["t"] == "Strong":
		# inline[]
		pandoc2.strong(inline["c"])
	if inline["t"] == "Strikeout":
		# inline[]
		pandoc2.strikeout(inline["c"])
	if inline["t"] == "Superscript":
		# inline[]
		pandoc2.superscript(inline["c"])
	if inline["t"] == "Subscript":
		# inline[]
		pandoc2.subscript(inline["c"])
	if inline["t"] == "SmallCaps":
		# inline[]
		pandoc2.smallCaps(inline["c"])
	if inline["t"] == "Quoted":
		# quotetype, inline[]
		pandoc2.quoted(inline["c"])
	if inline["t"] == "Cite":
		# citation[], inline[]
		pandoc2.cite(inline["c"])
	if inline["t"] == "Code":
		# attributes, text
		pandoc2.code(inline["c"])
	if inline["t"] == "Space":
		pandoc2.space()
	if inline["t"] == "SoftBreak":
		pandoc2.newline()
	if inline["t"] == "LineBreak":
		pandoc2.newline()
	if inline["t"] == "Math":
		# mathtype, text
		pandoc2.math(inline["c"])
	if inline["t"] == "RawInline":
		# format, text
		processRaw(inline["c"], pandoc2)
	if inline["t"] == "Link":
		# attr, inline[], text
		pandoc2.link(inline["c"])
	if inline["t"] == "Image":
		# attr, inline[], text
		pandoc2.image(inline["c"])
	if inline["t"] == "Note":
		# block[]
		pandoc2.note(inline["c"])
	if inline["t"] == "Span":
		# attr, inline[]
		pandoc2.span(inline["c"])

def processBlock(block, pandoc2):
	"""Do stuff for an block object

	Args:
		block (dict): An block holds various types such as 'Para', 'Table'
		pandoc2 (object): pandoc2XYZ object formatter
	"""
	if block["t"] == "Plain":
		# inline[]
		for inline in block["c"]:
			processInline(inline, pandoc2)
	if block["t"] == "Para":
		# inline[]
		for inline in block["c"]:
			processInline(inline, pandoc2)
	if block["t"] == "LineBlock":
		# inline[][]
		pandoc2.lineBlock(block["c"])
	if block["t"] == "CodeBlock":
		# language, text
		pandoc2.codeBlock(block["c"])
	if block["t"] == "RawBlock":
		# type, text
		processRaw(block["c"], pandoc2)
	if block["t"] == "BlockQuote":
		# block[]
		pandoc2.blockQuote(block["c"])
	if block["t"] == "OrderedList":
		# attributes, block[][]
		pandoc2.orderedList(block["c"])
	if block["t"] == "BulletList":
		# block[][]
		pandoc2.bulletList(block["c"])
	if block["t"] == "DefinitionList":
		# [key, value] key=inline[] value=block[]
		pandoc2.definitionList(block["c"])
	if block["t"] == "Header":
		# int, attr, inline[]
		pandoc2.header(block["c"])
	if block["t"] == "HorizontalRule":
		pandoc2.hr()
	if block["t"] == "Table":
		# inline[], alignment[], double[], tablecell[], tablecell[][]
		# ignore. align, ignore, tableHead, tableBody
		pandoc2.table(block["c"])
	if block["t"] == "Div":
		# attr, block[]
		for newBlock in block["c"][1]:
			processBlock(newBlock, pandoc2)
	if block["t"] == "Null":
		pass


class Pandoc2Plain():
	"""Convert a pandoc string to plaintext
	"""
	def __init__(self, width=80, padding=0):
		self.content = []
		self.width = width - padding * 2
		self.padding = padding


	#########################################
	# UTIL
	#########################################

	def newline(self):
		'''newline '''
		self.print()

	def catImage(self, content):
		'''catImage '''
		self.print(content)


	def print(self, *args, end="\n"):
		'''Define a custom print method that has a very similar signature
		to the inbuilt print method '''
		self.content.append(" ".join([str(text) for text in args]) + end)

	def genOutput(self):
		'''Generate output '''
		lines = "".join(self.content).split("\n")
		out = []
		for line in lines:
			out.append(" " * self.padding + line)
		return "\n".join(out)

	#########################################
	# BLOCK
	#########################################

	def header(self, content):
		'''Process a header '''
		self.print("\n", end="")
		concatContent = ""
		if content[0] > 3:
			for part in content[-1]:
				processInline(part, self)
		else:
			concatContent = "".join([toPlaintext(part) for part in content[-1]])
			if any(char in concatContent for char in ["q", "y", "p", "g", "j"]):
				limit = 1
			else:
				limit = 2
			if content[0] == 1:
				if len(concatContent) > self.width / 7:
					concatContent = concatContent[:int(self.width / 7)]
				self.print("\n".join(art.text2art(concatContent, "swan").split("\n")[2:-limit-1]))
				self.print("▀"*self.width)
			if content[0] == 2:
				if len(concatContent) > self.width / 5:
					concatContent = concatContent[:int(self.width / 5)]
				self.print("\n".join(art.text2art(concatContent, "thin").split("\n")[1:-limit]))
				self.print("━"*self.width)
			if content[0] == 3:
				if len(concatContent) > self.width / 3:
					concatContent = concatContent[:int(self.width / 3)]
				self.print("\n".join(art.text2art(concatContent, "cygnet").split("\n")[1:-limit]))
				self.print("─"*self.width)

	def codeBlock(self, content):
		'''Process a code block  '''
		self.print("\n │ ", end="")
		self.print("\n │ ".join(content[1].split("\n")))

	def definitionList(self, content):
		'''Process a definition list '''
		for definition in content:
			#for definition in definitionBlock:
			self.newline()
			for part in definition[0]:
				processInline(part, self)
			self.print("\t:\t:\t", end="")
			for part in definition[1]:
				for partB in part:
					processBlock(partB, self)


	def orderedList(self, content):
		'''Process an ordered list '''
		for index, bullet in enumerate(content[1]):
			self.print("\n", index+1, end=". ")
			for point in bullet:
				if point["t"] in ["BulletList"]:
					self.print(" > ", end="")
				processBlock(point, self)

	def bulletList(self, content):
		'''Process a bulleted list '''
		for bullet in content:
			for point in bullet:
				if point["t"] not in ["BulletList"]:
					self.print("\n- ", end="")
				else:
					self.print(" > ", end="")
				processBlock(point, self)

	def table(self, content):
		'''Process a table '''
		# inline[], alignment[], double[], tablecell[], tablecell[][]
		# ignore. align, ignore, tableHead, tableBody
		colWidth = str(int(self.width/len(content[1]))-1)
		alignment = {"AlignLeft": "{:<"+colWidth+"."+colWidth+"}",
		"AlignCenter": "{:^"+colWidth+"."+colWidth+"}",
		"AlignRight": "{:>"+colWidth+"."+colWidth+"}",
		"AlignDefault": "{:<"+colWidth+"."+colWidth+"}"}
		self.print()
		self.print("│", end="")
		for index, tableHead in enumerate(content[3]):
			headContent = "".join([toPlaintext(headPart) for headPart in tableHead])
			self.print((alignment[content[1][index]["t"]]).format(headContent) + "│", end="")
		self.print("\n│", end="")
		for index, _ in enumerate(content[1]):
			self.print((alignment[content[1][index]["t"]]).format("─"*self.width) + "┤", end="")
		for tableRow in content[4]:
			self.print("\n│", end="")
			for index, tableCol in enumerate(tableRow):
				colContent = "".join([toPlaintext(colPart) for colPart in tableCol])
				self.print((alignment[content[1][index]["t"]]).format(colContent) + "│", end="")
		self.print()


	def blockQuote(self, content):
		'''Process a block quote '''
		print("\n ┃ ", end="")
		print("\n ┃ ".join([toPlaintext(block).split("\n") for block in content][0]))


	#########################################
	# INLINE
	#########################################

	def space(self):
		'''Process a space '''
		self.print(" ", end="")

	def emph(self, content):
		'''Process emphasized text '''
		for newInline in content:
			self.print("_", end="")
			processInline(newInline, self)
			self.print("_", end="")

	def strong(self, content):
		'''Process strong (bold) text '''
		for newInline in content:
			self.print("*", end="")
			processInline(newInline, self)
			self.print("*", end="")

	def strikeout(self, content):
		'''Process strikeout (crossed out) text '''
		for newInline in content:
			self.print("-", end="")
			processInline(newInline, self)
			self.print("-", end="")

	def superscript(self, content):
		'''Process superscript text '''
		for newInline in content:
			processInline(newInline, self)

	def subscript(self, content):
		'''Process subscript text '''
		for newInline in content:
			processInline(newInline, self)

	def smallCaps(self, content):
		'''Process small caps text '''
		for newInline in content:
			processInline(newInline, self)

	def quoted(self, content):
		'''Process quoted text '''
		for newInline in content[1]:
			self.print("\'", end="")
			processInline(newInline, self)
			self.print("\'", end="")

	def code(self, content):
		'''Process code '''
		self.print(" │" + content[1], end="│ ")

	def math(self, content):
		'''Process math '''
		self.print("Math: " + content[1])


	def note(self, content):
		'''Process a note '''
		for block in content:
			processBlock(block, self)


	def span(self, content):
		'''Process a span '''
		for newInline in content[1]:
			processInline(newInline, self)


	def image(self, content):
		'''Process an image '''
		self.catImage(content[-1][0])

	def link(self, content):
		'''Process a link '''
		for part in content[1]:
			processInline(part, self)
		self.print(" -> " + content[2][0], end="")

	def hr(self):
		'''Process a hr '''
		self.print("─"*self.width)
