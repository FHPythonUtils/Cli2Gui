# Data Structures

The easiest way to understand the data structures would be to clone the repo
and add print statements.

For instance, in the case of *parser*2json. To understand the structure of the
JSON object add a print to application/application.py and run an example. See
below for an example for `buildSpec["widgets"]`:

```python
def createLayout(buildSpec, widgets):
	"""Create the pysimple gui layout from the build spec
	[...]

	Returns:
		list: list of widgets (layout list)
	"""
	# Add print ⬇️
	print(buildSpec["widgets"])

	sections = []
	for widget in buildSpec["widgets"]:
		[...]
```

Following the above and running `python3.8 test/argparse/advanced.py --cli2gui`
will print

```python
[{'name': 'positional arguments', 'arg_items': [{'type': 'TextBox',
'display_name': 'positional', 'help': 'positional arg', 'commands': [],
'choices': [], 'dest': 'positional', '_other': {}}, {'type': 'File',
'display_name': 'positional-file', 'help': 'positional arg for a file',
'commands': [], 'choices': [], 'dest': 'positional-file', '_other': {}}],
'groups': []}, {'name': 'optional arguments', 'arg_items': [{'type': 'TextBox',
'display_name': 'optional', 'help': 'optional arg', 'commands': ['--optional'],
'choices': [], 'dest': 'optional', '_other': {}}, {'type': 'Bool',
'display_name': 'store_true', 'help': 'optional arg store true', 'commands':
['--store-true'], 'choices': [], 'dest': 'store_true', '_other': {}}, {'type':
'Bool', 'display_name': 'store_false', 'help': 'optional arg store false',
'commands': ['--store-false'], 'choices': [], 'dest': 'store_false', '_other':
{}}, {'type': 'TextBox', 'display_name': 'store', 'help': 'optional arg store',
'commands': ['--store'], 'choices': [], 'dest': 'store', '_other': {}},
{'type': 'Counter', 'display_name': 'count', 'help': 'optional arg count',
'commands': ['--count'], 'choices': [], 'dest': 'count', '_other': {}}, {'type':
'Dropdown', 'display_name': 'choices', 'help': 'optional arg store with choices',
'commands': ['--choices'], 'choices': ['choice1', 'choice2'], 'dest': 'choices',
'_other': {}}], 'groups': []}, {'name': 'choose one of the following',
'arg_items': [{'type': 'Group', 'commands': [['--mxg-true'], ['--mxg-false'],
['--mxg'], ['--mxg-count'], ['--mxg-choices']], 'radio': [{'type': 'Bool',
'display_name': 'mxg_true', 'help': 'mutually exclusive arg store true',
'commands': ['--mxg-true'], 'choices': [], 'dest': 'mxg_true', '_other': {}},
{'type': 'Bool', 'display_name': 'mxg_false', 'help':
'mutually exclusive arg store false', 'commands': ['--mxg-false'], 'choices': [],
'dest': 'mxg_false', '_other': {}}, {'type': 'TextBox', 'display_name': 'mxg',
'help': 'mutually exclusive arg store', 'commands': ['--mxg'], 'choices': [],
'dest': 'mxg', '_other': {}}, {'type': 'Counter', 'display_name': 'mxg_count',
'help': 'mutually exclusive arg count', 'commands': ['--mxg-count'], 'choices':
[], 'dest': 'mxg_count', '_other': {}}, {'type': 'Dropdown', 'display_name':
'mxg_choices', 'help': 'mutually exclusive arg store with choices', 'commands':
['--mxg-choices'], 'choices': ['choice1', 'choice2'], 'dest': 'mxg_choices',
'_other': {}}]}], 'groups': []}]
```

The rest of the document includes documentation on several data structures. Note
that this may be more outdated than using the aforementioned method (as this
will have to be updated as features are added and code is streamlined)

## buildSpec

Contains the initial data set by the end user

```python
class BuildSpec(typing.TypedDict):
	"""Representation for the BuildSpec."""
	run_function: Callable[..., Any]
	parser: str
	gui: str
	theme: Union[str, list[str]]
	darkTheme: Union[str, list[str]]
	sizes: Union[dict[str, Any]]
	image: str
	program_name: str
	program_description: str
	max_args_shown:	int
	menu: Union[dict[str, Any]]
```

## fullBuildSpec

Contains all the data needed to build the GUI such as the theme, name,
description and so on.

```python
class FullBuildSpec(typing.TypedDict):
	"""Representation for the FullBuildSpec (BuildSpec + ParserRep)."""
	run_function: Callable[..., Any]
	parser: str
	gui: str
	theme: Union[str, list[str]]
	darkTheme: Union[str, list[str]]
	sizes: Union[dict[str, Any]]
	image: str
	program_name: str
	program_description: str
	max_args_shown:	int
	menu: Union[dict[str, Any]]
	parser_description: str
	widgets: list[Widgets]
```

## parserRep

Each *parser*2json.py provides a JSON object that is used to build the GUI.

```python
class ParserRep(typing.TypedDict):
	"""Representation for a parser."""
	parser_description: str
	widgets: list[Group]
```

```python
class Group(typing.TypedDict):
	""" representation for an argument group."""
	name: str
	arg_items: list[Item]
	groups: list[Group, list[Any]]
```

```python
class Item(typing.TypedDict):
	""" representation for an arg_item."""
	type: str
	display_name: str
	help: str
	commands: list[Any]
	choices: list[Any, list[str]]
	dest: str
	_other: dict[Any, Any]
```
