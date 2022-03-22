# Argparse2json

> Auto-generated documentation for [cli2gui.tojson.argparse2json](../../../../cli2gui/tojson/argparse2json.py) module.

Generate a dict describing argparse arguments...

- [Cli2gui](../../README.md#cli2gui-index) / [Modules](../../MODULES.md#cli2gui-modules) / [Cli2gui](../index.md#cli2gui) / [Tojson](index.md#tojson) / Argparse2json
    - [ArgparseGroup](#argparsegroup)
    - [actionToJson](#actiontojson)
    - [buildRadioGroup](#buildradiogroup)
    - [categorizeGroups](#categorizegroups)
    - [catergorizeItems](#catergorizeitems)
    - [chooseName](#choosename)
    - [containsActions](#containsactions)
    - [convert](#convert)
    - [extractRawGroups](#extractrawgroups)
    - [isDefaultProgname](#isdefaultprogname)
    - [iterParsers](#iterparsers)
    - [process](#process)
    - [reapplyMutexGroups](#reapplymutexgroups)
    - [stripEmpty](#stripempty)

pylint and pylance both want me to not access protected methods - I know better ;)

## ArgparseGroup

[[find in source code]](../../../../cli2gui/tojson/argparse2json.py#L26)

```python
class ArgparseGroup(TypedDict):
```

Class to represent an ArgparseGroup

## actionToJson

[[find in source code]](../../../../cli2gui/tojson/argparse2json.py#L107)

```python
def actionToJson(action: argparse.Action, widget: str) -> c2gtypes.Item:
```

Generate json for an action and set the widget - used by the application.

## buildRadioGroup

[[find in source code]](../../../../cli2gui/tojson/argparse2json.py#L120)

```python
def buildRadioGroup(mutexGroup: _MutuallyExclusiveGroup):
```

Create a radio group for a mutex group of arguments.

## categorizeGroups

[[find in source code]](../../../../cli2gui/tojson/argparse2json.py#L149)

```python
def categorizeGroups(groups: list[ArgparseGroup]) -> list[c2gtypes.Group]:
```

Categorize the parser groups and arg_items.

#### See also

- [ArgparseGroup](#argparsegroup)

## catergorizeItems

[[find in source code]](../../../../cli2gui/tojson/argparse2json.py#L130)

```python
def catergorizeItems(
    actions: list[argparse.Action],
) -> Generator[c2gtypes.Item, None, None]:
```

Catergorise each action and generate json.

## chooseName

[[find in source code]](../../../../cli2gui/tojson/argparse2json.py#L53)

```python
def chooseName(name: str, subparser: argparse.ArgumentParser) -> str:
```

Get the program name.

## containsActions

[[find in source code]](../../../../cli2gui/tojson/argparse2json.py#L58)

```python
def containsActions(
    actionA: list[argparse.Action],
    actionB: list[argparse.Action],
):
```

Check if any actions(a) are present in actions(b).

## convert

[[find in source code]](../../../../cli2gui/tojson/argparse2json.py#L176)

```python
def convert(parser: argparse.ArgumentParser) -> c2gtypes.ParserRep:
```

Convert argparse to a dict.

#### Arguments

- `parser` *argparse.ArgumentParser* - argparse parser

#### Returns

- `c2gtypes.ParserRep` - dictionary representing parser object

## extractRawGroups

[[find in source code]](../../../../cli2gui/tojson/argparse2json.py#L95)

```python
def extractRawGroups(actionGroup: argparse._ArgumentGroup) -> ArgparseGroup:
```

Recursively extract argument groups and associated actions from ParserGroup objects.

#### See also

- [ArgparseGroup](#argparsegroup)

## isDefaultProgname

[[find in source code]](../../../../cli2gui/tojson/argparse2json.py#L48)

```python
def isDefaultProgname(name: str, subparser: argparse.ArgumentParser) -> bool:
```

Identify if the passed name is the default program name.

## iterParsers

[[find in source code]](../../../../cli2gui/tojson/argparse2json.py#L34)

```python
def iterParsers(
    parser: argparse.ArgumentParser,
) -> list[tuple[str, argparse.ArgumentParser]]:
```

Iterate over name, parser pairs.

## process

[[find in source code]](../../../../cli2gui/tojson/argparse2json.py#L166)

```python
def process(parser: argparse.ArgumentParser) -> list[c2gtypes.Group]:
```

Reapply the mutex groups and then categorize them and the arg_items under the parser.

## reapplyMutexGroups

[[find in source code]](../../../../cli2gui/tojson/argparse2json.py#L63)

```python
def reapplyMutexGroups(
    mutexGroups: list[argparse._MutuallyExclusiveGroup],
    actionGroups: list[Any],
):
```

_argparse stores mutually exclusive groups independently...

of all other groups. So, they must be manually re-combined
with the groups/subgroups to which they were originally declared
in order to have them appear in the correct location in the UI.

Order is attempted to be preserved by inserting the MutexGroup
into the _actions list at the first occurrence of any item
where the two groups intersect.

## stripEmpty

[[find in source code]](../../../../cli2gui/tojson/argparse2json.py#L161)

```python
def stripEmpty(groups: list[ArgparseGroup]):
```

Remove groups where group['arg_items'] is false.

#### See also

- [ArgparseGroup](#argparsegroup)
