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
    action: tuple[str, str, str, Any, str], widget: str, isPos: bool
) -> c2gtypes.Item:
    ...
```



## categorize

[Show source in docopt2json.py:36](../../../../cli2gui/tojson/docopt2json.py#L36)

Catergorise each action and generate json.

#### Signature

```python
def categorize(
    actions: list[tuple[str, str, str, Any, str]], isPos: bool = False
) -> Iterator[c2gtypes.Item]:
    ...
```



## convert

[Show source in docopt2json.py:114](../../../../cli2gui/tojson/docopt2json.py#L114)

Convert getopt to a dict.

#### Arguments

- `parser` *Any* - docopt parser

#### Returns

- `c2gtypes.ParserRep` - dictionary representing parser object

#### Signature

```python
def convert(parser: Any) -> c2gtypes.ParserRep:
    ...
```



## extract

[Show source in docopt2json.py:48](../../../../cli2gui/tojson/docopt2json.py#L48)

Get the actions as json for the parser.

#### Signature

```python
def extract(parser: Any) -> list[c2gtypes.Group]:
    ...
```



## parse

[Show source in docopt2json.py:73](../../../../cli2gui/tojson/docopt2json.py#L73)

Parse an option help text, adapted from docopt.

#### Signature

```python
def parse(optionDescription: str) -> tuple[str, str, str, Any, str]:
    ...
```



## parseOpt

[Show source in docopt2json.py:91](../../../../cli2gui/tojson/docopt2json.py#L91)

Parse an option help text, adapted from docopt.

#### Signature

```python
def parseOpt(doc: Any) -> list[tuple[str, str, str, Any, str]]:
    ...
```



## parsePos

[Show source in docopt2json.py:103](../../../../cli2gui/tojson/docopt2json.py#L103)

Parse positional arguments from docstring.

#### Signature

```python
def parsePos(doc: Any) -> list[tuple[str, str, str, Any, str]]:
    ...
```



## parseSection

[Show source in docopt2json.py:64](../../../../cli2gui/tojson/docopt2json.py#L64)

Taken from docopt.

#### Signature

```python
def parseSection(name: str, source: Any) -> list[str]:
    ...
```


