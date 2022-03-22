# C2gtypes

> Auto-generated documentation for [cli2gui.c2gtypes](../../../cli2gui/c2gtypes.py) module.

Types for cli2gui.

- [Cli2gui](../README.md#cli2gui-index) / [Modules](../MODULES.md#cli2gui-modules) / [Cli2gui](index.md#cli2gui) / C2gtypes
    - [BuildSpec](#buildspec)
    - [FullBuildSpec](#fullbuildspec)
    - [GUIType](#guitype)
    - [Group](#group)
    - [Item](#item)
    - [ParserRep](#parserrep)
    - [ParserType](#parsertype)

## BuildSpec

[[find in source code]](../../../cli2gui/c2gtypes.py#L15)

```python
dataclass
class BuildSpec(TypedDict):
```

Representation for the BuildSpec.

## FullBuildSpec

[[find in source code]](../../../cli2gui/c2gtypes.py#L62)

```python
dataclass
class FullBuildSpec(TypedDict):
```

Representation for the FullBuildSpec (BuildSpec + ParserRep).

## GUIType

[[find in source code]](../../../cli2gui/c2gtypes.py#L103)

```python
class GUIType(str, Enum):
```

Supported gui types.

DEFAULT = "pysimplegui"
WEB = "pysimpleguiweb"
QT = "pysimpleguiqt"

## Group

[[find in source code]](../../../cli2gui/c2gtypes.py#L45)

```python
dataclass
class Group(TypedDict):
```

Representation for an argument group.

## Item

[[find in source code]](../../../cli2gui/c2gtypes.py#L32)

```python
dataclass
class Item(TypedDict):
```

Representation for an arg_item.

## ParserRep

[[find in source code]](../../../cli2gui/c2gtypes.py#L54)

```python
dataclass
class ParserRep(TypedDict):
```

Representation for a parser.

## ParserType

[[find in source code]](../../../cli2gui/c2gtypes.py#L81)

```python
class ParserType(str, Enum):
```

Supported parser types.

OPTPARSE = "optparse"
ARGPARSE = "argparse"
DEPHELL_ARGPARSE = "dephell_argparse"
DOCOPT = "docopt"
GETOPT = "getopt"
CLICK = "click"
CUSTOM = "input()"  # this seems like a pretty poor pattern to use
