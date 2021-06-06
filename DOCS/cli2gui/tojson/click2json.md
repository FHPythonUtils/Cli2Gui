# click2json

> Auto-generated documentation for [cli2gui.tojson.click2json](../../../cli2gui/tojson/click2json.py) module.

Generate a dict describing optparse arguments.

- [Cli2gui](../../README.md#cli2gui-index) / [Modules](../../README.md#cli2gui-modules) / [cli2gui](../index.md#cli2gui) / [tojson](index.md#tojson) / click2json
    - [actionToJson](#actiontojson)
    - [categorize](#categorize)
    - [categorizeCommand](#categorizecommand)
    - [convert](#convert)
    - [extract](#extract)

## actionToJson

[[find in source code]](../../../cli2gui/tojson/click2json.py#L34)

```python
def actionToJson(action: Any, widget: str) -> c2gtypes.Item:
```

Generate json for an action and set the widget - used by the application.

## categorize

[[find in source code]](../../../cli2gui/tojson/click2json.py#L52)

```python
def categorize(actions: list[Any]) -> Generator[(c2gtypes.Item, None, None)]:
```

Catergorise each action and generate json.

## categorizeCommand

[[find in source code]](../../../cli2gui/tojson/click2json.py#L58)

```python
def categorizeCommand(
    actions: list[Any],
) -> Generator[(c2gtypes.Item, None, None)]:
```

Catergorise each action and generate json.

## convert

[[find in source code]](../../../cli2gui/tojson/click2json.py#L64)

```python
def convert(parser: Any) -> c2gtypes.ParserRep:
```

Convert click to a dict.

#### Arguments

- `parser` *click.core.Command* - click parser

#### Returns

- `c2gtypes.ParserRep` - dictionary representing parser object

## extract

[[find in source code]](../../../cli2gui/tojson/click2json.py#L10)

```python
def extract(parser: Any) -> list[c2gtypes.Group]:
```

Get the actions as json for the parser.
