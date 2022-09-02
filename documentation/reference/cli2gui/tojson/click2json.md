# Click2json

[Cli2gui Index](../../README.md#cli2gui-index) /
[Cli2gui](../index.md#cli2gui) /
[Tojson](./index.md#tojson) /
Click2json

> Auto-generated documentation for [cli2gui.tojson.click2json](../../../../cli2gui/tojson/click2json.py) module.

- [Click2json](#click2json)
  - [actionToJson](#actiontojson)
  - [categorize](#categorize)
  - [categorizeCommand](#categorizecommand)
  - [convert](#convert)
  - [extract](#extract)

## actionToJson

[Show source in click2json.py:34](../../../../cli2gui/tojson/click2json.py#L34)

Generate json for an action and set the widget - used by the application.

#### Signature

```python
def actionToJson(action: Any, widget: str) -> c2gtypes.Item:
    ...
```



## categorize

[Show source in click2json.py:52](../../../../cli2gui/tojson/click2json.py#L52)

Catergorise each action and generate json.

#### Signature

```python
def categorize(actions: list[Any]) -> Generator[c2gtypes.Item, None, None]:
    ...
```



## categorizeCommand

[Show source in click2json.py:58](../../../../cli2gui/tojson/click2json.py#L58)

Catergorise each action and generate json.

#### Signature

```python
def categorizeCommand(actions: list[Any]) -> Generator[c2gtypes.Item, None, None]:
    ...
```



## convert

[Show source in click2json.py:64](../../../../cli2gui/tojson/click2json.py#L64)

Convert click to a dict.

#### Arguments

- `parser` *click.core.Command* - click parser

#### Returns

- `c2gtypes.ParserRep` - dictionary representing parser object

#### Signature

```python
def convert(parser: Any) -> c2gtypes.ParserRep:
    ...
```



## extract

[Show source in click2json.py:10](../../../../cli2gui/tojson/click2json.py#L10)

Get the actions as json for the parser.

#### Signature

```python
def extract(parser: Any) -> list[c2gtypes.Group]:
    ...
```


