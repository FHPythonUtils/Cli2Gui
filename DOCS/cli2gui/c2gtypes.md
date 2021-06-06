# c2gtypes

> Auto-generated documentation for [cli2gui.c2gtypes](../../cli2gui/c2gtypes.py) module.

Types for cli2gui.

- [Cli2gui](../README.md#cli2gui-index) / [Modules](../README.md#cli2gui-modules) / [cli2gui](index.md#cli2gui) / c2gtypes
    - [BuildSpec](#buildspec)
    - [FullBuildSpec](#fullbuildspec)
    - [Group](#group)
    - [Item](#item)
    - [ParserRep](#parserrep)

## BuildSpec

[[find in source code]](../../cli2gui/c2gtypes.py#L10)

```python
class BuildSpec(TypedDict):
```

Representation for the BuildSpec.

## FullBuildSpec

[[find in source code]](../../cli2gui/c2gtypes.py#L53)

```python
class FullBuildSpec(TypedDict):
```

Representation for the FullBuildSpec (BuildSpec + ParserRep).

## Group

[[find in source code]](../../cli2gui/c2gtypes.py#L38)

```python
class Group(TypedDict):
```

Representation for an argument group.

## Item

[[find in source code]](../../cli2gui/c2gtypes.py#L26)

```python
class Item(TypedDict):
```

Representation for an arg_item.

## ParserRep

[[find in source code]](../../cli2gui/c2gtypes.py#L46)

```python
class ParserRep(TypedDict):
```

Representation for a parser.
