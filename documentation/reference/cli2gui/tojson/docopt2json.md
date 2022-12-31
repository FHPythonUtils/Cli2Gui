# Docopt2json

[Cli2gui Index](../../README.md#cli2gui-index) /
[Cli2gui](../index.md#cli2gui) /
[Tojson](./index.md#tojson) /
Docopt2json

> Auto-generated documentation for [cli2gui.tojson.docopt2json](../../../../cli2gui/tojson/docopt2json.py) module.

- [Docopt2json](#docopt2json)
  - [actionToJson](#actiontojson)
  - [categorize](#categorize)
  - [convert](#convert)
  - [extract](#extract)
  - [parse](#parse)
  - [parseOpt](#parseopt)
  - [parsePos](#parsepos)
  - [parseSection](#parsesection)

## actionToJson

[Show source in docopt2json.py:11](../../../../cli2gui/tojson/docopt2json.py#L11)

Generate json for an action and set the widget - used by the application.

#### Signature

```python
def actionToJson(
    action: tuple[str, str, int, Any, str], widget: types.ItemType, isPos: bool
) -> types.Item:
    ...
```



## categorize

[Show source in docopt2json.py:39](../../../../cli2gui/tojson/docopt2json.py#L39)

Catergorise each action and generate json.

Each action is in the form (short, long, argcount, value, help_message)

#### Signature

```python
def categorize(
    actions: list[tuple[str, str, int, Any, str]], isPos: bool = False
) -> Iterator[types.Item]:
    ...
```



## convert

[Show source in docopt2json.py:123](../../../../cli2gui/tojson/docopt2json.py#L123)

Convert getopt to a dict.

#### Arguments

- `parser` *Any* - docopt parser

#### Returns

- `types.ParserRep` - dictionary representing parser object

#### Signature

```python
def convert(parser: Any) -> types.ParserRep:
    ...
```



## extract

[Show source in docopt2json.py:57](../../../../cli2gui/tojson/docopt2json.py#L57)

Get the actions as json for the parser.

#### Signature

```python
def extract(parser: Any) -> list[types.Group]:
    ...
```



## parse

[Show source in docopt2json.py:82](../../../../cli2gui/tojson/docopt2json.py#L82)

Parse an option help text, adapted from docopt.

#### Signature

```python
def parse(optionDescription: str) -> tuple[str, str, int, Any, str]:
    ...
```



## parseOpt

[Show source in docopt2json.py:100](../../../../cli2gui/tojson/docopt2json.py#L100)

Parse an option help text, adapted from docopt.

#### Signature

```python
def parseOpt(doc: Any) -> list[tuple[str, str, int, Any, str]]:
    ...
```



## parsePos

[Show source in docopt2json.py:112](../../../../cli2gui/tojson/docopt2json.py#L112)

Parse positional arguments from docstring.

#### Signature

```python
def parsePos(doc: Any) -> list[tuple[str, str]]:
    ...
```



## parseSection

[Show source in docopt2json.py:73](../../../../cli2gui/tojson/docopt2json.py#L73)

Taken from docopt.

#### Signature

```python
def parseSection(name: str, source: Any) -> list[str]:
    ...
```


