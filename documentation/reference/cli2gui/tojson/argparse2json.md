# Argparse2json

[Cli2gui Index](../../README.md#cli2gui-index) /
[Cli2gui](../index.md#cli2gui) /
[Tojson](./index.md#tojson) /
Argparse2json

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

[Show source in argparse2json.py:25](../../../../cli2gui/tojson/argparse2json.py#L25)

Class to represent an ArgparseGroup

#### Signature

```python
class ArgparseGroup(TypedDict):
    ...
```



## actionToJson

[Show source in argparse2json.py:107](../../../../cli2gui/tojson/argparse2json.py#L107)

Generate json for an action and set the widget - used by the application.

#### Signature

```python
def actionToJson(action: argparse.Action, widget: types.ItemType) -> types.Item:
    ...
```



## buildRadioGroup

[Show source in argparse2json.py:121](../../../../cli2gui/tojson/argparse2json.py#L121)

Create a radio group for a mutex group of arguments.

#### Signature

```python
def buildRadioGroup(mutexGroup: _MutuallyExclusiveGroup) -> types.Item:
    ...
```



## categorizeGroups

[Show source in argparse2json.py:150](../../../../cli2gui/tojson/argparse2json.py#L150)

Categorize the parser groups and arg_items.

#### Signature

```python
def categorizeGroups(groups: list[ArgparseGroup]) -> list[types.Group]:
    ...
```

#### See also

- [ArgparseGroup](#argparsegroup)



## categorizeItems

[Show source in argparse2json.py:131](../../../../cli2gui/tojson/argparse2json.py#L131)

Catergorise each action and generate json.

#### Signature

```python
def categorizeItems(actions: list[argparse.Action]) -> Generator[types.Item, None, None]:
    ...
```



## chooseName

[Show source in argparse2json.py:54](../../../../cli2gui/tojson/argparse2json.py#L54)

Get the program name.

#### Signature

```python
def chooseName(name: str, subparser: argparse.ArgumentParser) -> str:
    ...
```



## containsActions

[Show source in argparse2json.py:59](../../../../cli2gui/tojson/argparse2json.py#L59)

Check if any actions(a) are present in actions(b).

#### Signature

```python
def containsActions(actionA: list[argparse.Action], actionB: list[argparse.Action]):
    ...
```



## convert

[Show source in argparse2json.py:177](../../../../cli2gui/tojson/argparse2json.py#L177)

Convert argparse to a dict.

#### Arguments

- `parser` *argparse.ArgumentParser* - argparse parser

#### Returns

- `types.ParserRep` - dictionary representing parser object

#### Signature

```python
def convert(parser: argparse.ArgumentParser) -> types.ParserRep:
    ...
```



## extractRawGroups

[Show source in argparse2json.py:95](../../../../cli2gui/tojson/argparse2json.py#L95)

Recursively extract argument groups and associated actions from ParserGroup objects.

#### Signature

```python
def extractRawGroups(actionGroup: argparse._ArgumentGroup) -> ArgparseGroup:
    ...
```

#### See also

- [ArgparseGroup](#argparsegroup)



## isDefaultProgname

[Show source in argparse2json.py:49](../../../../cli2gui/tojson/argparse2json.py#L49)

Identify if the passed name is the default program name.

#### Signature

```python
def isDefaultProgname(name: str, subparser: argparse.ArgumentParser) -> bool:
    ...
```



## iterParsers

[Show source in argparse2json.py:33](../../../../cli2gui/tojson/argparse2json.py#L33)

Iterate over name, parser pairs.

#### Signature

```python
def iterParsers(
    parser: argparse.ArgumentParser,
) -> list[tuple[str, argparse.ArgumentParser]]:
    ...
```



## process

[Show source in argparse2json.py:167](../../../../cli2gui/tojson/argparse2json.py#L167)

Reapply the mutex groups and then categorize them and the arg_items under the parser.

#### Signature

```python
def process(parser: argparse.ArgumentParser) -> list[types.Group]:
    ...
```



## reapplyMutexGroups

[Show source in argparse2json.py:64](../../../../cli2gui/tojson/argparse2json.py#L64)

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
):
    ...
```



## stripEmpty

[Show source in argparse2json.py:162](../../../../cli2gui/tojson/argparse2json.py#L162)

Remove groups where group['arg_items'] is false.

#### Signature

```python
def stripEmpty(groups: list[ArgparseGroup]):
    ...
```

#### See also

- [ArgparseGroup](#argparsegroup)