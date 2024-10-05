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

[Show source in optparse2json.py:40](../../../../cli2gui/tojson/optparse2json.py#L40)

Generate json for an action and set the widget - used by the application.

#### Signature

```python
def actionToJson(action: optparse.Option, widget: ItemType) -> Item: ...
```

#### See also

- [ItemType](../types.md#itemtype)
- [Item](../types.md#item)



## categorize

[Show source in optparse2json.py:58](../../../../cli2gui/tojson/optparse2json.py#L58)

Catergorise each action and generate json.

#### Signature

```python
def categorize(actions: list[optparse.Option]) -> Generator[Item, None, None]: ...
```

#### See also

- [Item](../types.md#item)



## convert

[Show source in optparse2json.py:73](../../../../cli2gui/tojson/optparse2json.py#L73)

Convert argparse to a dict.

#### Arguments

----
 - `parser` *optparse.OptionParser* - optparse parser

#### Returns

-------
 - `ParserRep` - dictionary representing parser object

#### Signature

```python
def convert(parser: optparse.OptionParser) -> ParserRep: ...
```

#### See also

- [ParserRep](../types.md#parserrep)



## extractGroups

[Show source in optparse2json.py:28](../../../../cli2gui/tojson/optparse2json.py#L28)

Get the actions as json for each item and group under the parser.

#### Signature

```python
def extractGroups(parser: optparse.OptionParser) -> Group: ...
```

#### See also

- [Group](../types.md#group)



## extractOptions

[Show source in optparse2json.py:15](../../../../cli2gui/tojson/optparse2json.py#L15)

Get the actions as json for each item under a group.

#### Signature

```python
def extractOptions(optionGroup: optparse.OptionGroup) -> Group: ...
```

#### See also

- [Group](../types.md#group)