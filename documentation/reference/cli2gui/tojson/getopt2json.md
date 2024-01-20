# Getopt2json

[Cli2gui Index](../../README.md#cli2gui-index) / [Cli2gui](../index.md#cli2gui) / [Tojson](./index.md#tojson) / Getopt2json

> Auto-generated documentation for [cli2gui.tojson.getopt2json](../../../../cli2gui/tojson/getopt2json.py) module.

- [Getopt2json](#getopt2json)
  - [actionToJson](#actiontojson)
  - [catLong](#catlong)
  - [catShort](#catshort)
  - [convert](#convert)
  - [process](#process)

## actionToJson

[Show source in getopt2json.py:13](../../../../cli2gui/tojson/getopt2json.py#L13)

Convert an arg to json, behave in the same way as argparse hence the large
amount of duplication.

#### Signature

```python
def actionToJson(
    action: str, widget: types.ItemType, short: bool = True
) -> types.Item: ...
```



## catLong

[Show source in getopt2json.py:28](../../../../cli2gui/tojson/getopt2json.py#L28)

Categorize long args.

#### Signature

```python
def catLong(actions: list[str]) -> Generator[types.Item, None, None]: ...
```



## catShort

[Show source in getopt2json.py:38](../../../../cli2gui/tojson/getopt2json.py#L38)

Categorize short args.

#### Signature

```python
def catShort(actions: list[str]) -> Generator[types.Item, None, None]: ...
```



## convert

[Show source in getopt2json.py:70](../../../../cli2gui/tojson/getopt2json.py#L70)

Convert getopt to a dict.

#### Arguments

----
 parser (tuple[list[str], list[str]]): getopt parser

#### Returns

-------
 - `types.ParserRep` - dictionary representing parser object

#### Signature

```python
def convert(parser: tuple[list[str], list[str]]) -> types.ParserRep: ...
```



## process

[Show source in getopt2json.py:55](../../../../cli2gui/tojson/getopt2json.py#L55)

Generate a group (or section).

#### Signature

```python
def process(
    group: list[str],
    groupName: str,
    categorize: Callable[[list[str]], Generator[types.Item, None, None]],
) -> list[types.Group]: ...
```