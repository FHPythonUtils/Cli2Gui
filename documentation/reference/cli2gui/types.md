# Types

[Cli2gui Index](../README.md#cli2gui-index) / [Cli2gui](./index.md#cli2gui) / Types

> Auto-generated documentation for [cli2gui.types](../../../cli2gui/types.py) module.

- [Types](#types)
  - [BuildSpec](#buildspec)
  - [FullBuildSpec](#fullbuildspec)
  - [GUIType](#guitype)
  - [Group](#group)
  - [Item](#item)
  - [ItemType](#itemtype)
  - [ParserRep](#parserrep)
  - [ParserType](#parsertype)

## BuildSpec

[Show source in types.py:13](../../../cli2gui/types.py#L13)

Representation for the BuildSpec.

#### Signature

```python
class BuildSpec(TypedDict): ...
```



## FullBuildSpec

[Show source in types.py:71](../../../cli2gui/types.py#L71)

Representation for the FullBuildSpec (BuildSpec + ParserRep).

#### Signature

```python
class FullBuildSpec(TypedDict): ...
```



## GUIType

[Show source in types.py:112](../../../cli2gui/types.py#L112)

Supported gui types.

DEFAULT = "pysimplegui"
WEB = "pysimpleguiweb"
QT = "pysimpleguiqt"

#### Signature

```python
class GUIType(str, Enum): ...
```



## Group

[Show source in types.py:54](../../../cli2gui/types.py#L54)

Representation for an argument group.

#### Signature

```python
class Group(TypedDict): ...
```



## Item

[Show source in types.py:30](../../../cli2gui/types.py#L30)

Representation for an arg_item.

#### Signature

```python
class Item(TypedDict): ...
```



## ItemType

[Show source in types.py:42](../../../cli2gui/types.py#L42)

Enum of ItemTypes.

#### Signature

```python
class ItemType(Enum): ...
```



## ParserRep

[Show source in types.py:63](../../../cli2gui/types.py#L63)

Representation for a parser.

#### Signature

```python
class ParserRep(TypedDict): ...
```



## ParserType

[Show source in types.py:90](../../../cli2gui/types.py#L90)

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
class ParserType(str, Enum): ...
```