# Optparse2json

[Cli2gui Index](../../README.md#cli2gui-index) /
[Cli2gui](../index.md#cli2gui) /
[Tojson](./index.md#tojson) /
Optparse2json

> Auto-generated documentation for [cli2gui.tojson.optparse2json](../../../../cli2gui/tojson/optparse2json.py) module.

- [Optparse2json](#optparse2json)
  - [actionToJson](#actiontojson)
  - [categorize](#categorize)
  - [convert](#convert)
  - [extractGroups](#extractgroups)
  - [extractOptions](#extractoptions)

## actionToJson

[Show source in optparse2json.py:40](../../../../cli2gui/tojson/optparse2json.py#L40)

Generate json for an action and set the widget - used by the application.

#### Signature

```python
def actionToJson(action: optparse.Option, widget: str) -> c2gtypes.Item:
    ...
```



## categorize

[Show source in optparse2json.py:53](../../../../cli2gui/tojson/optparse2json.py#L53)

Catergorise each action and generate json.

#### Signature

```python
def categorize(actions: list[optparse.Option]):
    ...
```



## convert

[Show source in optparse2json.py:68](../../../../cli2gui/tojson/optparse2json.py#L68)

Convert argparse to a dict.

#### Arguments

- `parser` *optparse.OptionParser* - optparse parser

#### Returns

- `c2gtypes.ParserRep` - dictionary representing parser object

#### Signature

```python
def convert(parser: optparse.OptionParser) -> c2gtypes.ParserRep:
    ...
```



## extractGroups

[Show source in optparse2json.py:28](../../../../cli2gui/tojson/optparse2json.py#L28)

Get the actions as json for each item and group under the parser.

#### Signature

```python
def extractGroups(parser: optparse.OptionParser) -> c2gtypes.Group:
    ...
```



## extractOptions

[Show source in optparse2json.py:14](../../../../cli2gui/tojson/optparse2json.py#L14)

Get the actions as json for each item under a group.

#### Signature

```python
def extractOptions(optionGroup: optparse.OptionGroup) -> c2gtypes.Group:
    ...
```


