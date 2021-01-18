# optparse2json

> Auto-generated documentation for [cli2gui.tojson.optparse2json](../../../cli2gui/tojson/optparse2json.py) module.

Generate a dict describing optparse arguments

- [Cli2gui](../../README.md#cli2gui-index) / [Modules](../../README.md#cli2gui-modules) / [cli2gui](../index.md#cli2gui) / [tojson](index.md#tojson) / optparse2json
    - [actionToJson](#actiontojson)
    - [categorize](#categorize)
    - [convert](#convert)
    - [extractGroups](#extractgroups)
    - [extractOptions](#extractoptions)

pylint and pylance both want me to not access protected methods - I know better ;)

## actionToJson

[[find in source code]](../../../cli2gui/tojson/optparse2json.py#L33)

```python
def actionToJson(action: optparse.Option, widget: str) -> c2gtypes.Item:
```

Generate json for an action and set the widget - used by the application

## categorize

[[find in source code]](../../../cli2gui/tojson/optparse2json.py#L47)

```python
def categorize(actions: list[optparse.Option]):
```

Catergorise each action and generate json

## convert

[[find in source code]](../../../cli2gui/tojson/optparse2json.py#L62)

```python
def convert(parser: optparse.OptionParser) -> c2gtypes.ParserRep:
```

Convert argparse to a dict

#### Arguments

- `parser` *optparse.OptionParser* - optparse parser

#### Returns

- `c2gtypes.ParserRep` - dictionary representing parser object

## extractGroups

[[find in source code]](../../../cli2gui/tojson/optparse2json.py#L23)

```python
def extractGroups(parser: optparse.OptionParser) -> c2gtypes.Group:
```

Get the actions as json for each item and group under the parser

## extractOptions

[[find in source code]](../../../cli2gui/tojson/optparse2json.py#L13)

```python
def extractOptions(optionGroup: optparse.OptionParser) -> c2gtypes.Group:
```

Get the actions as json for each item under a group
