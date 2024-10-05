# Docopt2json

[Cli2gui Index](../../README.md#cli2gui-index) / [Cli2gui](../index.md#cli2gui) / [Tojson](./index.md#tojson) / Docopt2json

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
    action: tuple[str, str, int, Any, str], widget: ItemType, isPos: bool
) -> Item: ...
```

#### See also

- [ItemType](../types.md#itemtype)
- [Item](../types.md#item)



## categorize

[Show source in docopt2json.py:37](../../../../cli2gui/tojson/docopt2json.py#L37)

Catergorise each action and generate json.

Each action is in the form (short, long, argcount, value, help_message)

#### Signature

```python
def categorize(
    actions: list[tuple[str, str, int, Any, str]], isPos: bool = False
) -> Iterator[Item]: ...
```

#### See also

- [Item](../types.md#item)



## convert

[Show source in docopt2json.py:117](../../../../cli2gui/tojson/docopt2json.py#L117)

Convert getopt to a dict.

#### Arguments

----
 - `parser` *Any* - docopt parser

#### Returns

-------
 - `ParserRep` - dictionary representing parser object

#### Signature

```python
def convert(parser: Any) -> ParserRep: ...
```

#### See also

- [ParserRep](../types.md#parserrep)



## extract

[Show source in docopt2json.py:55](../../../../cli2gui/tojson/docopt2json.py#L55)

Get the actions as json for the parser.

#### Signature

```python
def extract(parser: Any) -> list[Group]: ...
```

#### See also

- [Group](../types.md#group)



## parse

[Show source in docopt2json.py:76](../../../../cli2gui/tojson/docopt2json.py#L76)

Parse an option help text, adapted from docopt.

#### Signature

```python
def parse(optionDescription: str) -> tuple[str, str, int, Any, str]: ...
```



## parseOpt

[Show source in docopt2json.py:94](../../../../cli2gui/tojson/docopt2json.py#L94)

Parse an option help text, adapted from docopt.

#### Signature

```python
def parseOpt(doc: Any) -> list[tuple[str, str, int, Any, str]]: ...
```



## parsePos

[Show source in docopt2json.py:106](../../../../cli2gui/tojson/docopt2json.py#L106)

Parse positional arguments from docstring.

#### Signature

```python
def parsePos(doc: str) -> list[tuple[str, str]]: ...
```



## parseSection

[Show source in docopt2json.py:67](../../../../cli2gui/tojson/docopt2json.py#L67)

Taken from docopt.

#### Signature

```python
def parseSection(name: str, source: str) -> list[str]: ...
```