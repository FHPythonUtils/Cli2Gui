# Widgets

[Cli2gui Index](../../README.md#cli2gui-index) /
[Cli2gui](../index.md#cli2gui) /
[Application](./index.md#application) /
Widgets

> Auto-generated documentation for [cli2gui.application.widgets](../../../../cli2gui/application/widgets.py) module.

- [Widgets](#widgets)
  - [Widgets](#widgets-1)
    - [Widgets().button](#widgets()button)
    - [Widgets().check](#widgets()check)
    - [Widgets().dropdown](#widgets()dropdown)
    - [Widgets().fileBrowser](#widgets()filebrowser)
    - [Widgets().getImgData](#widgets()getimgdata)
    - [Widgets().helpArgHelp](#widgets()helparghelp)
    - [Widgets().helpArgName](#widgets()helpargname)
    - [Widgets().helpArgNameAndHelp](#widgets()helpargnameandhelp)
    - [Widgets().helpDropdownWidget](#widgets()helpdropdownwidget)
    - [Widgets().helpFileWidget](#widgets()helpfilewidget)
    - [Widgets().helpFlagWidget](#widgets()helpflagwidget)
    - [Widgets().helpTextWidget](#widgets()helptextwidget)
    - [Widgets().inputText](#widgets()inputtext)
    - [Widgets().label](#widgets()label)
    - [Widgets().stringSentencecase](#widgets()stringsentencecase)
    - [Widgets().stringTitlecase](#widgets()stringtitlecase)
    - [Widgets().title](#widgets()title)

## Widgets

[Show source in widgets.py:15](../../../../cli2gui/application/widgets.py#L15)

Widgets class holding methods to create widgets in addition to a sizes...

attribute that can be overridden to provide the end user with customisation
over the size of the gui.

#### Signature

```python
class Widgets:
    def __init__(self, sizes: dict[str, Any], pySimpleGui: Any):
        ...
```

### Widgets().button

[Show source in widgets.py:80](../../../../cli2gui/application/widgets.py#L80)

Return a button.

#### Signature

```python
def button(self, text: str) -> Element:
    ...
```

### Widgets().check

[Show source in widgets.py:74](../../../../cli2gui/application/widgets.py#L74)

Return a checkbox.

#### Signature

```python
def check(self, key: str) -> Element:
    ...
```

### Widgets().dropdown

[Show source in widgets.py:101](../../../../cli2gui/application/widgets.py#L101)

Return a dropdown.

#### Signature

```python
def dropdown(self, key: str, argItems: list[str]) -> Element:
    ...
```

### Widgets().fileBrowser

[Show source in widgets.py:110](../../../../cli2gui/application/widgets.py#L110)

Return a fileBrowser button and field.

#### Signature

```python
def fileBrowser(self, key: str) -> list[Element]:
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

[Show source in widgets.py:135](../../../../cli2gui/application/widgets.py#L135)

Return a label for the arg help text.

#### Signature

```python
def helpArgHelp(self, helpText: str) -> Element:
    ...
```

### Widgets().helpArgName

[Show source in widgets.py:131](../../../../cli2gui/application/widgets.py#L131)

Return a label for the arg name.

#### Signature

```python
def helpArgName(self, displayName: str, commands: list[str]) -> Element:
    ...
```

### Widgets().helpArgNameAndHelp

[Show source in widgets.py:139](../../../../cli2gui/application/widgets.py#L139)

Return a column containing the argument name and help text.

#### Signature

```python
def helpArgNameAndHelp(
    self, commands: list[str], helpText: str, displayName: str
) -> Element:
    ...
```

### Widgets().helpDropdownWidget

[Show source in widgets.py:194](../../../../cli2gui/application/widgets.py#L194)

Return a set of widgets that make up an arg with a choice.

#### Signature

```python
def helpDropdownWidget(
    self,
    displayName: str,
    commands: list[str],
    helpText: str,
    dest: str,
    choices: list[str],
) -> list[Element]:
    ...
```

### Widgets().helpFileWidget

[Show source in widgets.py:185](../../../../cli2gui/application/widgets.py#L185)

Return a set of widgets that make up an arg with a file.

#### Signature

```python
def helpFileWidget(
    self, displayName: str, commands: list[str], helpText: str, dest: str
) -> list[Element]:
    ...
```

### Widgets().helpFlagWidget

[Show source in widgets.py:167](../../../../cli2gui/application/widgets.py#L167)

Return a set of widgets that make up an arg with true/ false.

#### Signature

```python
def helpFlagWidget(
    self, displayName: str, commands: list[str], helpText: str, dest: str
) -> list[Element]:
    ...
```

### Widgets().helpTextWidget

[Show source in widgets.py:176](../../../../cli2gui/application/widgets.py#L176)

Return a set of widgets that make up an arg with text.

#### Signature

```python
def helpTextWidget(
    self, displayName: str, commands: list[str], helpText: str, dest: str
) -> list[Element]:
    ...
```

### Widgets().inputText

[Show source in widgets.py:65](../../../../cli2gui/application/widgets.py#L65)

Return an input text field.

#### Signature

```python
def inputText(self, key: str) -> Element:
    ...
```

### Widgets().label

[Show source in widgets.py:89](../../../../cli2gui/application/widgets.py#L89)

Return a label.

#### Signature

```python
def label(self, text: str, font: int = 11) -> Element:
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

[Show source in widgets.py:146](../../../../cli2gui/application/widgets.py#L146)

Return a set of widgets that make up the application header.

#### Signature

```python
def title(self, text: str, image: str = "") -> list[Element]:
    ...
```


