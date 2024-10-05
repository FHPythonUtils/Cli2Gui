# Click2json

[Cli2gui Index](../../README.md#cli2gui-index) / [Cli2gui](../index.md#cli2gui) / [Tojson](./index.md#tojson) / Click2json

> Auto-generated documentation for [cli2gui.tojson.click2json](../../../../cli2gui/tojson/click2json.py) module.

- [Click2json](#click2json)
  - [actionToJson](#actiontojson)
  - [categorize](#categorize)
  - [convert](#convert)
  - [extract](#extract)

## actionToJson

[Show source in click2json.py:29](../../../../cli2gui/tojson/click2json.py#L29)

Generate json for an action and set the widget - used by the application.

#### Signature

```python
def actionToJson(action: Any, widget: ItemType, other: dict | None = None) -> Item: ...
```

#### See also

- [ItemType](../types.md#itemtype)
- [Item](../types.md#item)



## categorize

[Show source in click2json.py:47](../../../../cli2gui/tojson/click2json.py#L47)

Catergorise each action and generate json.

#### Signature

```python
def categorize(actions: list[Any]) -> Generator[Item, None, None]: ...
```

#### See also

- [Item](../types.md#item)



## convert

[Show source in click2json.py:66](../../../../cli2gui/tojson/click2json.py#L66)

Convert click to a dict.

#### Arguments

----
 - `parser` *click.core.Command* - click parser

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

[Show source in click2json.py:11](../../../../cli2gui/tojson/click2json.py#L11)

Get the actions as json for the parser.

#### Signature

```python
def extract(parser: Any) -> list[Group]: ...
```

#### See also

- [Group](../types.md#group)