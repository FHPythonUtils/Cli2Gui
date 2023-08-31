# Types

[Cli2gui Index](../README.md#cli2gui-index) /
[Cli2gui](./index.md#cli2gui) /
Types

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

[Show source in types.py:15](../../../cli2gui/types.py#L15)

Representation for the BuildSpec.

#### Signature

```python
class BuildSpec(TypedDict):
    ...
```



## FullBuildSpec

[Show source in types.py:73](../../../cli2gui/types.py#L73)

Representation for the FullBuildSpec (BuildSpec + ParserRep).

#### Signature

```python
class FullBuildSpec(TypedDict):
    ...
```



## GUIType

[Show source in types.py:114](../../../cli2gui/types.py#L114)

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

[Show source in types.py:56](../../../cli2gui/types.py#L56)

Representation for an argument group.

#### Signature

```python
class Group(TypedDict):
    ...
```



## Item

[Show source in types.py:32](../../../cli2gui/types.py#L32)

Representation for an arg_item.

#### Signature

```python
class Item(TypedDict):
    ...
```



## ItemType

[Show source in types.py:44](../../../cli2gui/types.py#L44)

Enum of ItemTypes:

#### Signature

```python
class ItemType(Enum):
    ...
```



## ParserRep

[Show source in types.py:65](../../../cli2gui/types.py#L65)

Representation for a parser.

#### Signature

```python
class ParserRep(TypedDict):
    ...
```



## ParserType

[Show source in types.py:92](../../../cli2gui/types.py#L92)

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