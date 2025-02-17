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

[Show source in types.py:14](../../../cli2gui/types.py#L14)

Representation for the BuildSpec.

#### Signature

```python
class BuildSpec: ...
```



## FullBuildSpec

[Show source in types.py:80](../../../cli2gui/types.py#L80)

Representation for the FullBuildSpec (BuildSpec + ParserRep).

#### Signature

```python
class FullBuildSpec: ...
```



## GUIType

[Show source in types.py:120](../../../cli2gui/types.py#L120)

Supported gui types.

DEFAULT = "pysimplegui"
WEB = "pysimpleguiweb"
QT = "pysimpleguiqt"
FSG = "freesimplegui"

#### Signature

```python
class GUIType(str, Enum): ...
```



## Group

[Show source in types.py:63](../../../cli2gui/types.py#L63)

Representation for an argument group.

#### Signature

```python
class Group: ...
```



## Item

[Show source in types.py:30](../../../cli2gui/types.py#L30)

Representation for an arg_item.

#### Signature

```python
class Item: ...
```



## ItemType

[Show source in types.py:45](../../../cli2gui/types.py#L45)

Enum of ItemTypes.

#### Signature

```python
class ItemType(Enum): ...
```



## ParserRep

[Show source in types.py:72](../../../cli2gui/types.py#L72)

Representation for a parser.

#### Signature

```python
class ParserRep: ...
```



## ParserType

[Show source in types.py:98](../../../cli2gui/types.py#L98)

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