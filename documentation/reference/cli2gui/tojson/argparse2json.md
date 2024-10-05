# Argparse2json

[Cli2gui Index](../../README.md#cli2gui-index) / [Cli2gui](../index.md#cli2gui) / [Tojson](./index.md#tojson) / Argparse2json

> Auto-generated documentation for [cli2gui.tojson.argparse2json](../../../../cli2gui/tojson/argparse2json.py) module.

- [Argparse2json](#argparse2json)
  - [ArgparseGroup](#argparsegroup)
  - [actionToJson](#actiontojson)
  - [buildRadioGroup](#buildradiogroup)
  - [categorizeGroups](#categorizegroups)
  - [categorizeItems](#categorizeitems)
  - [chooseName](#choosename)
  - [containsActions](#containsactions)
  - [convert](#convert)
  - [extractRawGroups](#extractrawgroups)
  - [isDefaultProgname](#isdefaultprogname)
  - [iterParsers](#iterparsers)
  - [process](#process)
  - [reapplyMutexGroups](#reapplymutexgroups)
  - [stripEmpty](#stripempty)

## ArgparseGroup

[Show source in argparse2json.py:26](../../../../cli2gui/tojson/argparse2json.py#L26)

Class to represent an ArgparseGroup.

#### Signature

```python
class ArgparseGroup(TypedDict): ...
```



## actionToJson

[Show source in argparse2json.py:111](../../../../cli2gui/tojson/argparse2json.py#L111)

Generate json for an action and set the widget - used by the application.

#### Signature

```python
def actionToJson(action: argparse.Action, widget: ItemType) -> Item: ...
```

#### See also

- [ItemType](../types.md#itemtype)
- [Item](../types.md#item)



## buildRadioGroup

[Show source in argparse2json.py:125](../../../../cli2gui/tojson/argparse2json.py#L125)

Create a radio group for a mutex group of arguments.

#### Signature

```python
def buildRadioGroup(mutexGroup: _MutuallyExclusiveGroup) -> Item: ...
```

#### See also

- [Item](../types.md#item)



## categorizeGroups

[Show source in argparse2json.py:164](../../../../cli2gui/tojson/argparse2json.py#L164)

Categorize the parser groups and arg_items.

#### Signature

```python
def categorizeGroups(groups: list[ArgparseGroup]) -> list[Group]: ...
```

#### See also

- [ArgparseGroup](#argparsegroup)
- [Group](../types.md#group)



## categorizeItems

[Show source in argparse2json.py:139](../../../../cli2gui/tojson/argparse2json.py#L139)

Catergorise each action and generate json.

#### Signature

```python
def categorizeItems(actions: list[argparse.Action]) -> Generator[Item, None, None]: ...
```

#### See also

- [Item](../types.md#item)



## chooseName

[Show source in argparse2json.py:55](../../../../cli2gui/tojson/argparse2json.py#L55)

Get the program name.

#### Signature

```python
def chooseName(name: str, subparser: argparse.ArgumentParser) -> str: ...
```



## containsActions

[Show source in argparse2json.py:60](../../../../cli2gui/tojson/argparse2json.py#L60)

Check if any actions(a) are present in actions(b).

#### Signature

```python
def containsActions(
    actionA: list[argparse.Action], actionB: list[argparse.Action]
) -> set[argparse.Action]: ...
```



## convert

[Show source in argparse2json.py:191](../../../../cli2gui/tojson/argparse2json.py#L191)

Convert argparse to a dict.

#### Arguments

----
 - `parser` *argparse.ArgumentParser* - argparse parser

#### Returns

-------
 - `ParserRep` - dictionary representing parser object

#### Signature

```python
def convert(parser: argparse.ArgumentParser) -> ParserRep: ...
```

#### See also

- [ParserRep](../types.md#parserrep)



## extractRawGroups

[Show source in argparse2json.py:99](../../../../cli2gui/tojson/argparse2json.py#L99)

Recursively extract argument groups and associated actions from ParserGroup objects.

#### Signature

```python
def extractRawGroups(actionGroup: argparse._ArgumentGroup) -> ArgparseGroup: ...
```

#### See also

- [ArgparseGroup](#argparsegroup)



## isDefaultProgname

[Show source in argparse2json.py:50](../../../../cli2gui/tojson/argparse2json.py#L50)

Identify if the passed name is the default program name.

#### Signature

```python
def isDefaultProgname(name: str, subparser: argparse.ArgumentParser) -> bool: ...
```



## iterParsers

[Show source in argparse2json.py:34](../../../../cli2gui/tojson/argparse2json.py#L34)

Iterate over name, parser pairs.

#### Signature

```python
def iterParsers(
    parser: argparse.ArgumentParser,
) -> list[tuple[str, argparse.ArgumentParser]]: ...
```



## process

[Show source in argparse2json.py:181](../../../../cli2gui/tojson/argparse2json.py#L181)

Reapply the mutex groups and then categorize them and the arg_items under the parser.

#### Signature

```python
def process(parser: argparse.ArgumentParser) -> list[Group]: ...
```

#### See also

- [Group](../types.md#group)



## reapplyMutexGroups

[Show source in argparse2json.py:67](../../../../cli2gui/tojson/argparse2json.py#L67)

_argparse stores mutually exclusive groups independently.
of all other groups. So, they must be manually re-combined
with the groups/subgroups to which they were originally declared
in order to have them appear in the correct location in the UI.

Order is attempted to be preserved by inserting the MutexGroup
into the _actions list at the first occurrence of any item
where the two groups intersect.

#### Signature

```python
def reapplyMutexGroups(
    mutexGroups: list[argparse._MutuallyExclusiveGroup], actionGroups: list[Any]
) -> list[Any]: ...
```



## stripEmpty

[Show source in argparse2json.py:176](../../../../cli2gui/tojson/argparse2json.py#L176)

Remove groups where group['arg_items'] is false.

#### Signature

```python
def stripEmpty(groups: list[ArgparseGroup]) -> list[ArgparseGroup]: ...
```

#### See also

- [ArgparseGroup](#argparsegroup)