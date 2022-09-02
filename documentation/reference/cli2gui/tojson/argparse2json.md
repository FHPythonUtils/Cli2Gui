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

## ArgparseGroup

[Show source in argparse2json.py:26](../../../../cli2gui/tojson/argparse2json.py#L26)

Class to represent an ArgparseGroup

#### Signature

```python
class ArgparseGroup(TypedDict):
    ...
```



## actionToJson

[Show source in argparse2json.py:109](../../../../cli2gui/tojson/argparse2json.py#L109)

Generate json for an action and set the widget - used by the application.

#### Signature

```python
def actionToJson(action: argparse.Action, widget: str) -> c2gtypes.Item:
    ...
```



## buildRadioGroup

[Show source in argparse2json.py:122](../../../../cli2gui/tojson/argparse2json.py#L122)

Create a radio group for a mutex group of arguments.

#### Signature

```python
def buildRadioGroup(mutexGroup: _MutuallyExclusiveGroup):
    ...
```



## categorizeGroups

[Show source in argparse2json.py:151](../../../../cli2gui/tojson/argparse2json.py#L151)

Categorize the parser groups and arg_items.

#### Signature

```python
def categorizeGroups(groups: list[ArgparseGroup]) -> list[c2gtypes.Group]:
    ...
```

#### See also

- [ArgparseGroup](#argparsegroup)



## catergorizeItems

[Show source in argparse2json.py:132](../../../../cli2gui/tojson/argparse2json.py#L132)

Catergorise each action and generate json.

#### Signature

```python
def catergorizeItems(
    actions: list[argparse.Action],
) -> Generator[c2gtypes.Item, None, None]:
    ...
```



## chooseName

[Show source in argparse2json.py:55](../../../../cli2gui/tojson/argparse2json.py#L55)

Get the program name.

#### Signature

```python
def chooseName(name: str, subparser: argparse.ArgumentParser) -> str:
    ...
```



## containsActions

[Show source in argparse2json.py:60](../../../../cli2gui/tojson/argparse2json.py#L60)

Check if any actions(a) are present in actions(b).

#### Signature

```python
def containsActions(actionA: list[argparse.Action], actionB: list[argparse.Action]):
    ...
```



## convert

[Show source in argparse2json.py:178](../../../../cli2gui/tojson/argparse2json.py#L178)

Convert argparse to a dict.

#### Arguments

- `parser` *argparse.ArgumentParser* - argparse parser

#### Returns

- `c2gtypes.ParserRep` - dictionary representing parser object

#### Signature

```python
def convert(parser: argparse.ArgumentParser) -> c2gtypes.ParserRep:
    ...
```



## extractRawGroups

[Show source in argparse2json.py:97](../../../../cli2gui/tojson/argparse2json.py#L97)

Recursively extract argument groups and associated actions from ParserGroup objects.

#### Signature

```python
def extractRawGroups(actionGroup: argparse._ArgumentGroup) -> ArgparseGroup:
    ...
```

#### See also

- [ArgparseGroup](#argparsegroup)



## isDefaultProgname

[Show source in argparse2json.py:50](../../../../cli2gui/tojson/argparse2json.py#L50)

Identify if the passed name is the default program name.

#### Signature

```python
def isDefaultProgname(name: str, subparser: argparse.ArgumentParser) -> bool:
    ...
```



## iterParsers

[Show source in argparse2json.py:34](../../../../cli2gui/tojson/argparse2json.py#L34)

Iterate over name, parser pairs.

#### Signature

```python
def iterParsers(
    parser: argparse.ArgumentParser,
) -> list[tuple[str, argparse.ArgumentParser]]:
    ...
```



## process

[Show source in argparse2json.py:168](../../../../cli2gui/tojson/argparse2json.py#L168)

Reapply the mutex groups and then categorize them and the arg_items under the parser.

#### Signature

```python
def process(parser: argparse.ArgumentParser) -> list[c2gtypes.Group]:
    ...
```



## reapplyMutexGroups

[Show source in argparse2json.py:65](../../../../cli2gui/tojson/argparse2json.py#L65)

_argparse stores mutually exclusive groups independently...

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

[Show source in argparse2json.py:163](../../../../cli2gui/tojson/argparse2json.py#L163)

Remove groups where group['arg_items'] is false.

#### Signature

```python
def stripEmpty(groups: list[ArgparseGroup]):
    ...
```

#### See also

- [ArgparseGroup](#argparsegroup)


