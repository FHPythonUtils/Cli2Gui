# docopt2json

> Auto-generated documentation for [cli2gui.tojson.docopt2json](../../../cli2gui/tojson/docopt2json.py) module.

Generate a dict for docopt

- [Cli2gui](../../README.md#cli2gui-index) / [Modules](../../README.md#cli2gui-modules) / [cli2gui](../index.md#cli2gui) / [tojson](index.md#tojson) / docopt2json
    - [actionToJson](#actiontojson)
    - [categorize](#categorize)
    - [convert](#convert)
    - [extract](#extract)
    - [parse](#parse)
    - [parseOpt](#parseopt)
    - [parsePos](#parsepos)
    - [parseSection](#parsesection)

## actionToJson

[[find in source code]](../../../cli2gui/tojson/docopt2json.py#L10)

```python
def actionToJson(
    action: tuple[(str, str, str, Any, str)],
    widget: str,
    isPos: bool,
) -> c2gtypes.Item:
```

Generate json for an action and set the widget - used by the application

## categorize

[[find in source code]](../../../cli2gui/tojson/docopt2json.py#L37)

```python
def categorize(
    actions: list[tuple[(str, str, str, Any, str)]],
    isPos: bool = False,
) -> Iterator[c2gtypes.Item]:
```

Catergorise each action and generate json

## convert

[[find in source code]](../../../cli2gui/tojson/docopt2json.py#L106)

```python
def convert(parser: Any) -> c2gtypes.ParserRep:
```

Convert getopt to a dict

#### Arguments

- `parser` *Any* - docopt parser

#### Returns

- `c2gtypes.ParserRep` - dictionary representing parser object

## extract

[[find in source code]](../../../cli2gui/tojson/docopt2json.py#L46)

```python
def extract(parser: Any) -> list[c2gtypes.Group]:
```

Get the actions as json for the parser

## parse

[[find in source code]](../../../cli2gui/tojson/docopt2json.py#L67)

```python
def parse(optionDescription: str) -> tuple[(str, str, str, Any, str)]:
```

Parse an option help text, adapted from docopt

## parseOpt

[[find in source code]](../../../cli2gui/tojson/docopt2json.py#L85)

```python
def parseOpt(doc: Any) -> list[tuple[(str, str, str, Any, str)]]:
```

Parse an option help text, adapted from docopt

## parsePos

[[find in source code]](../../../cli2gui/tojson/docopt2json.py#L97)

```python
def parsePos(doc: Any) -> list[tuple[(str, str, str, Any, str)]]:
```

Parse positional arguments from docstring

## parseSection

[[find in source code]](../../../cli2gui/tojson/docopt2json.py#L60)

```python
def parseSection(name: str, source: Any) -> list[str]:
```

Taken from docopt
