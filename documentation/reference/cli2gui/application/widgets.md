# Widgets

[Cli2gui Index](../../README.md#cli2gui-index) /
[Cli2gui](../index.md#cli2gui) /
[Application](./index.md#application) /
Widgets

> Auto-generated documentation for [cli2gui.application.widgets](../../../../cli2gui/application/widgets.py) module.

- [Widgets](#widgets)
  - [Widgets](#widgets-1)
    - [Widgets().addWidgetFromItem](#widgets()addwidgetfromitem)
    - [Widgets().button](#widgets()button)
    - [Widgets().check](#widgets()check)
    - [Widgets().dropdown](#widgets()dropdown)
    - [Widgets().fileBrowser](#widgets()filebrowser)
    - [Widgets().getImgData](#widgets()getimgdata)
    - [Widgets().helpArgHelp](#widgets()helparghelp)
    - [Widgets().helpArgName](#widgets()helpargname)
    - [Widgets().helpArgNameAndHelp](#widgets()helpargnameandhelp)
    - [Widgets().helpCounterWidget](#widgets()helpcounterwidget)
    - [Widgets().helpDropdownWidget](#widgets()helpdropdownwidget)
    - [Widgets().helpFileWidget](#widgets()helpfilewidget)
    - [Widgets().helpFlagWidget](#widgets()helpflagwidget)
    - [Widgets().helpTextWidget](#widgets()helptextwidget)
    - [Widgets().inputText](#widgets()inputtext)
    - [Widgets().label](#widgets()label)
    - [Widgets().spin](#widgets()spin)
    - [Widgets().stringSentencecase](#widgets()stringsentencecase)
    - [Widgets().stringTitlecase](#widgets()stringtitlecase)
    - [Widgets().title](#widgets()title)

## Widgets

[Show source in widgets.py:16](../../../../cli2gui/application/widgets.py#L16)

Widgets class holding methods to create widgets in addition to a sizes.
attribute that can be overridden to provide the end user with customisation
over the size of the gui.

#### Signature

```python
class Widgets:
    def __init__(self, sizes: dict[str, Any], pySimpleGui: Any):
        ...
```

### Widgets().addWidgetFromItem

[Show source in widgets.py:238](../../../../cli2gui/application/widgets.py#L238)

Add a widget from an item (types.Item)

#### Signature

```python
def addWidgetFromItem(self, item: types.Item) -> list[Element]:
    ...
```

### Widgets().button

[Show source in widgets.py:92](../../../../cli2gui/application/widgets.py#L92)

Return a button.

#### Signature

```python
def button(self, text: str) -> Element:
    ...
```

### Widgets().check

[Show source in widgets.py:86](../../../../cli2gui/application/widgets.py#L86)

Return a checkbox.

#### Signature

```python
def check(self, key: str, default=None) -> Element:
    ...
```

### Widgets().dropdown

[Show source in widgets.py:113](../../../../cli2gui/application/widgets.py#L113)

Return a dropdown.

#### Signature

```python
def dropdown(self, key: str, argItems: list[str]) -> Element:
    ...
```

### Widgets().fileBrowser

[Show source in widgets.py:122](../../../../cli2gui/application/widgets.py#L122)

Return a fileBrowser button and field.

#### Signature

```python
def fileBrowser(self, key: str, default=None) -> list[Element]:
    ...
```

### Widgets().getImgData

[Show source in widgets.py:29](../../../../cli2gui/application/widgets.py#L29)

Generate image data using PIL.

#### Signature

```python
def getImgData(self, imagePath: str, first: bool = False) -> bytes:
    ...
```

### Widgets().helpArgHelp

[Show source in widgets.py:148](../../../../cli2gui/application/widgets.py#L148)

Return a label for the arg help text.

#### Signature

```python
def helpArgHelp(self, helpText: str) -> Element:
    ...
```

### Widgets().helpArgName

[Show source in widgets.py:144](../../../../cli2gui/application/widgets.py#L144)

Return a label for the arg name.

#### Signature

```python
def helpArgName(self, displayName: str, commands: list[str]) -> Element:
    ...
```

### Widgets().helpArgNameAndHelp

[Show source in widgets.py:152](../../../../cli2gui/application/widgets.py#L152)

Return a column containing the argument name and help text.

#### Signature

```python
def helpArgNameAndHelp(
    self, commands: list[str], helpText: str, displayName: str
) -> Element:
    ...
```

### Widgets().helpCounterWidget

[Show source in widgets.py:204](../../../../cli2gui/application/widgets.py#L204)

Return a set of widgets that make up an arg with text.

#### Signature

```python
def helpCounterWidget(self, item: types.Item) -> list[Element]:
    ...
```

### Widgets().helpDropdownWidget

[Show source in widgets.py:226](../../../../cli2gui/application/widgets.py#L226)

Return a set of widgets that make up an arg with a choice.

#### Signature

```python
def helpDropdownWidget(self, item: types.Item) -> list[Element]:
    ...
```

### Widgets().helpFileWidget

[Show source in widgets.py:216](../../../../cli2gui/application/widgets.py#L216)

Return a set of widgets that make up an arg with a file.

#### Signature

```python
def helpFileWidget(self, item: types.Item) -> list[Element]:
    ...
```

### Widgets().helpFlagWidget

[Show source in widgets.py:180](../../../../cli2gui/application/widgets.py#L180)

Return a set of widgets that make up an arg with true/ false.

#### Signature

```python
def helpFlagWidget(self, item: types.Item) -> list[Element]:
    ...
```

### Widgets().helpTextWidget

[Show source in widgets.py:192](../../../../cli2gui/application/widgets.py#L192)

Return a set of widgets that make up an arg with text.

#### Signature

```python
def helpTextWidget(self, item: types.Item) -> list[Element]:
    ...
```

### Widgets().inputText

[Show source in widgets.py:65](../../../../cli2gui/application/widgets.py#L65)

Return an input text field.

#### Signature

```python
def inputText(self, key: str, default=None) -> Element:
    ...
```

### Widgets().label

[Show source in widgets.py:101](../../../../cli2gui/application/widgets.py#L101)

Return a label.

#### Signature

```python
def label(self, text: str, font: int = 11) -> Element:
    ...
```

### Widgets().spin

[Show source in widgets.py:75](../../../../cli2gui/application/widgets.py#L75)

Return an input text field.

#### Signature

```python
def spin(self, key: str, default=None) -> Element:
    ...
```

### Widgets().stringSentencecase

[Show source in widgets.py:55](../../../../cli2gui/application/widgets.py#L55)

Convert a string to sentence case.

#### Signature

```python
def stringSentencecase(self, string: str) -> str:
    ...
```

### Widgets().stringTitlecase

[Show source in widgets.py:40](../../../../cli2gui/application/widgets.py#L40)

Convert a string to title case.

#### Signature

```python
def stringTitlecase(self, string: str, splitStr: str = "ALL"):
    ...
```

### Widgets().title

[Show source in widgets.py:159](../../../../cli2gui/application/widgets.py#L159)

Return a set of widgets that make up the application header.

#### Signature

```python
def title(self, text: str, image: str = "") -> list[Element]:
    ...
```