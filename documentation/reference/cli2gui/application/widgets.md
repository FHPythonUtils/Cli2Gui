# Widgets

[Cli2gui Index](../../README.md#cli2gui-index) / [Cli2gui](../index.md#cli2gui) / [Application](./index.md#application) / Widgets

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

Methods to create widgets and a sizes attribute to provide users with
customization options for the size of the GUI.

Utility functions within the class manipulate images and text and create PySimpleGUI
Elements

#### Signature

```python
class Widgets:
    def __init__(self, sizes: dict[str, Any], pySimpleGui: Any) -> None: ...
```

### Widgets().addWidgetFromItem

[Show source in widgets.py:250](../../../../cli2gui/application/widgets.py#L250)

Add a widget from an item (types.Item).

#### Signature

```python
def addWidgetFromItem(self, item: types.Item) -> list[Element]: ...
```

### Widgets().button

[Show source in widgets.py:104](../../../../cli2gui/application/widgets.py#L104)

Return a button.

#### Signature

```python
def button(self, text: str) -> Element: ...
```

### Widgets().check

[Show source in widgets.py:98](../../../../cli2gui/application/widgets.py#L98)

Return a checkbox.

#### Signature

```python
def check(self, key: str, default: str | None = None) -> Element: ...
```

### Widgets().dropdown

[Show source in widgets.py:125](../../../../cli2gui/application/widgets.py#L125)

Return a dropdown.

#### Signature

```python
def dropdown(self, key: str, argItems: list[str]) -> Element: ...
```

### Widgets().fileBrowser

[Show source in widgets.py:134](../../../../cli2gui/application/widgets.py#L134)

Return a fileBrowser button and field.

#### Signature

```python
def fileBrowser(self, key: str, default: str | None = None) -> list[Element]: ...
```

### Widgets().getImgData

[Show source in widgets.py:41](../../../../cli2gui/application/widgets.py#L41)

Generate image data using PIL.

#### Signature

```python
def getImgData(self, imagePath: str, first: bool = False) -> bytes: ...
```

### Widgets().helpArgHelp

[Show source in widgets.py:160](../../../../cli2gui/application/widgets.py#L160)

Return a label for the arg help text.

#### Signature

```python
def helpArgHelp(self, helpText: str) -> Element: ...
```

### Widgets().helpArgName

[Show source in widgets.py:156](../../../../cli2gui/application/widgets.py#L156)

Return a label for the arg name.

#### Signature

```python
def helpArgName(self, displayName: str, commands: list[str]) -> Element: ...
```

### Widgets().helpArgNameAndHelp

[Show source in widgets.py:164](../../../../cli2gui/application/widgets.py#L164)

Return a column containing the argument name and help text.

#### Signature

```python
def helpArgNameAndHelp(
    self, commands: list[str], helpText: str, displayName: str
) -> Element: ...
```

### Widgets().helpCounterWidget

[Show source in widgets.py:216](../../../../cli2gui/application/widgets.py#L216)

Return a set of widgets that make up an arg with text.

#### Signature

```python
def helpCounterWidget(self, item: types.Item) -> list[Element]: ...
```

### Widgets().helpDropdownWidget

[Show source in widgets.py:238](../../../../cli2gui/application/widgets.py#L238)

Return a set of widgets that make up an arg with a choice.

#### Signature

```python
def helpDropdownWidget(self, item: types.Item) -> list[Element]: ...
```

### Widgets().helpFileWidget

[Show source in widgets.py:228](../../../../cli2gui/application/widgets.py#L228)

Return a set of widgets that make up an arg with a file.

#### Signature

```python
def helpFileWidget(self, item: types.Item) -> list[Element]: ...
```

### Widgets().helpFlagWidget

[Show source in widgets.py:192](../../../../cli2gui/application/widgets.py#L192)

Return a set of widgets that make up an arg with true/ false.

#### Signature

```python
def helpFlagWidget(self, item: types.Item) -> list[Element]: ...
```

### Widgets().helpTextWidget

[Show source in widgets.py:204](../../../../cli2gui/application/widgets.py#L204)

Return a set of widgets that make up an arg with text.

#### Signature

```python
def helpTextWidget(self, item: types.Item) -> list[Element]: ...
```

### Widgets().inputText

[Show source in widgets.py:77](../../../../cli2gui/application/widgets.py#L77)

Return an input text field.

#### Signature

```python
def inputText(self, key: str, default: str | None = None) -> Element: ...
```

### Widgets().label

[Show source in widgets.py:113](../../../../cli2gui/application/widgets.py#L113)

Return a label.

#### Signature

```python
def label(self, text: str, font: int = 11) -> Element: ...
```

### Widgets().spin

[Show source in widgets.py:87](../../../../cli2gui/application/widgets.py#L87)

Return an input text field.

#### Signature

```python
def spin(self, key: str, default: str | None = None) -> Element: ...
```

### Widgets().stringSentencecase

[Show source in widgets.py:67](../../../../cli2gui/application/widgets.py#L67)

Convert a string to sentence case.

#### Signature

```python
def stringSentencecase(self, string: str) -> str: ...
```

### Widgets().stringTitlecase

[Show source in widgets.py:52](../../../../cli2gui/application/widgets.py#L52)

Convert a string to title case.

#### Signature

```python
def stringTitlecase(self, string: str, splitStr: str = "ALL") -> str: ...
```

### Widgets().title

[Show source in widgets.py:171](../../../../cli2gui/application/widgets.py#L171)

Return a set of widgets that make up the application header.

#### Signature

```python
def title(self, text: str, image: str = "") -> list[Element]: ...
```