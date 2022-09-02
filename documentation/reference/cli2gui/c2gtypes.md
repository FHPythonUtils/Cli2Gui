# C2gtypes

[Cli2gui Index](../README.md#cli2gui-index) /
[Cli2gui](./index.md#cli2gui) /
C2gtypes

> Auto-generated documentation for [cli2gui.c2gtypes](../../../cli2gui/c2gtypes.py) module.

- [C2gtypes](#c2gtypes)
  - [BuildSpec](#buildspec)
  - [FullBuildSpec](#fullbuildspec)
  - [GUIType](#guitype)
  - [Group](#group)
  - [Item](#item)
  - [ParserRep](#parserrep)
  - [ParserType](#parsertype)

## BuildSpec

[Show source in c2gtypes.py:15](../../../cli2gui/c2gtypes.py#L15)

Representation for the BuildSpec.

#### Signature

```python
class BuildSpec(TypedDict):
    ...
```



## FullBuildSpec

[Show source in c2gtypes.py:62](../../../cli2gui/c2gtypes.py#L62)

Representation for the FullBuildSpec (BuildSpec + ParserRep).

#### Signature

```python
class FullBuildSpec(TypedDict):
    ...
```



## GUIType

[Show source in c2gtypes.py:103](../../../cli2gui/c2gtypes.py#L103)

Supported gui types.

DEFAULT = "pysimplegui"
WEB = "pysimpleguiweb"
QT = "pysimpleguiqt"

#### Signature

```python
class GUIType(str, Enum):
    ...
```



## Group

[Show source in c2gtypes.py:45](../../../cli2gui/c2gtypes.py#L45)

Representation for an argument group.

#### Signature

```python
class Group(TypedDict):
    ...
```



## Item

[Show source in c2gtypes.py:32](../../../cli2gui/c2gtypes.py#L32)

Representation for an arg_item.

#### Signature

```python
class Item(TypedDict):
    ...
```



## ParserRep

[Show source in c2gtypes.py:54](../../../cli2gui/c2gtypes.py#L54)

Representation for a parser.

#### Signature

```python
class ParserRep(TypedDict):
    ...
```



## ParserType

[Show source in c2gtypes.py:81](../../../cli2gui/c2gtypes.py#L81)

Supported parser types.

OPTPARSE = "optparse"
ARGPARSE = "argparse"
DEPHELL_ARGPARSE = "dephell_argparse"
DOCOPT = "docopt"
GETOPT = "getopt"
CLICK = "click"
CUSTOM = "input()"  # this seems like a pretty poor pattern to use

#### Signature

```python
class ParserType(str, Enum):
    ...
```


