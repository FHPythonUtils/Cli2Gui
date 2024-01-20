# Optparse2json

[Cli2gui Index](../../README.md#cli2gui-index) / [Cli2gui](../index.md#cli2gui) / [Tojson](./index.md#tojson) / Optparse2json

> Auto-generated documentation for [cli2gui.tojson.optparse2json](../../../../cli2gui/tojson/optparse2json.py) module.

- [Optparse2json](#optparse2json)
  - [actionToJson](#actiontojson)
  - [categorize](#categorize)
  - [convert](#convert)
  - [extractGroups](#extractgroups)
  - [extractOptions](#extractoptions)

## actionToJson

[Show source in optparse2json.py:41](../../../../cli2gui/tojson/optparse2json.py#L41)

Generate json for an action and set the widget - used by the application.

#### Signature

```python
def actionToJson(action: optparse.Option, widget: types.ItemType) -> types.Item: ...
```



## categorize

[Show source in optparse2json.py:59](../../../../cli2gui/tojson/optparse2json.py#L59)

Catergorise each action and generate json.

#### Signature

```python
def categorize(actions: list[optparse.Option]) -> Generator[types.Item, None, None]: ...
```



## convert

[Show source in optparse2json.py:74](../../../../cli2gui/tojson/optparse2json.py#L74)

Convert argparse to a dict.

#### Arguments

----
 - `parser` *optparse.OptionParser* - optparse parser

#### Returns

-------
 - `types.ParserRep` - dictionary representing parser object

#### Signature

```python
def convert(parser: optparse.OptionParser) -> types.ParserRep: ...
```



## extractGroups

[Show source in optparse2json.py:29](../../../../cli2gui/tojson/optparse2json.py#L29)

Get the actions as json for each item and group under the parser.

#### Signature

```python
def extractGroups(parser: optparse.OptionParser) -> types.Group: ...
```



## extractOptions

[Show source in optparse2json.py:15](../../../../cli2gui/tojson/optparse2json.py#L15)

Get the actions as json for each item under a group.

#### Signature

```python
def extractOptions(optionGroup: optparse.OptionGroup) -> types.Group: ...
```