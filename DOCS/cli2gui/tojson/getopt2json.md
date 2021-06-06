# getopt2json

> Auto-generated documentation for [cli2gui.tojson.getopt2json](../../../cli2gui/tojson/getopt2json.py) module.

Generate a dict for getopt.

- [Cli2gui](../../README.md#cli2gui-index) / [Modules](../../README.md#cli2gui-modules) / [cli2gui](../index.md#cli2gui) / [tojson](index.md#tojson) / getopt2json
    - [actionToJson](#actiontojson)
    - [catLong](#catlong)
    - [catShort](#catshort)
    - [convert](#convert)
    - [process](#process)

## actionToJson

[[find in source code]](../../../cli2gui/tojson/getopt2json.py#L11)

```python
def actionToJson(
    action: str,
    widget: str,
    short: bool = True,
) -> c2gtypes.Item:
```

Convert an arg to json, behave in the same way as argparse hence the large...

amount of duplication.

## catLong

[[find in source code]](../../../cli2gui/tojson/getopt2json.py#L27)

```python
def catLong(actions: list[str]):
```

Categorize long args.

## catShort

[[find in source code]](../../../cli2gui/tojson/getopt2json.py#L37)

```python
def catShort(actions: list[str]):
```

Categorize short args.

## convert

[[find in source code]](../../../cli2gui/tojson/getopt2json.py#L69)

```python
def convert(parser: tuple[(list[str], list[str])]) -> c2gtypes.ParserRep:
```

Convert getopt to a dict.

#### Arguments

parser (tuple[list[str], list[str]]): getopt parser

#### Returns

- `c2gtypes.ParserRep` - dictionary representing parser object

## process

[[find in source code]](../../../cli2gui/tojson/getopt2json.py#L54)

```python
def process(
    group: list[str],
    groupName: str,
    categorize: Callable[([list[str]], Generator[(c2gtypes.Item, None, None)])],
) -> list[c2gtypes.Group]:
```

Generate a group (or section).
