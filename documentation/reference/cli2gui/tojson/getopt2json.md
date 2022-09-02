# Getopt2json

[Cli2gui Index](../../README.md#cli2gui-index) /
[Cli2gui](../index.md#cli2gui) /
[Tojson](./index.md#tojson) /
Getopt2json

> Auto-generated documentation for [cli2gui.tojson.getopt2json](../../../../cli2gui/tojson/getopt2json.py) module.

- [Getopt2json](#getopt2json)
  - [actionToJson](#actiontojson)
  - [catLong](#catlong)
  - [catShort](#catshort)
  - [convert](#convert)
  - [process](#process)

## actionToJson

[Show source in getopt2json.py:11](../../../../cli2gui/tojson/getopt2json.py#L11)

Convert an arg to json, behave in the same way as argparse hence the large...

amount of duplication.

#### Signature

```python
def actionToJson(action: str, widget: str, short: bool = True) -> c2gtypes.Item:
    ...
```



## catLong

[Show source in getopt2json.py:27](../../../../cli2gui/tojson/getopt2json.py#L27)

Categorize long args.

#### Signature

```python
def catLong(actions: list[str]):
    ...
```



## catShort

[Show source in getopt2json.py:37](../../../../cli2gui/tojson/getopt2json.py#L37)

Categorize short args.

#### Signature

```python
def catShort(actions: list[str]):
    ...
```



## convert

[Show source in getopt2json.py:69](../../../../cli2gui/tojson/getopt2json.py#L69)

Convert getopt to a dict.

#### Arguments

parser (tuple[list[str], list[str]]): getopt parser

#### Returns

- `c2gtypes.ParserRep` - dictionary representing parser object

#### Signature

```python
def convert(parser: tuple[list[str], list[str]]) -> c2gtypes.ParserRep:
    ...
```



## process

[Show source in getopt2json.py:54](../../../../cli2gui/tojson/getopt2json.py#L54)

Generate a group (or section).

#### Signature

```python
def process(
    group: list[str],
    groupName: str,
    categorize: Callable[[list[str]], Generator[c2gtypes.Item, None, None]],
) -> list[c2gtypes.Group]:
    ...
```


