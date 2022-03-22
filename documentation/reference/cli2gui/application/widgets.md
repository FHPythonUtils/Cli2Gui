# Widgets

> Auto-generated documentation for [cli2gui.application.widgets](../../../../cli2gui/application/widgets.py) module.

Widgets class holding methods to create widgets in addition to a sizes...

- [Cli2gui](../../README.md#cli2gui-index) / [Modules](../../MODULES.md#cli2gui-modules) / [Cli2gui](../index.md#cli2gui) / [Application](index.md#application) / Widgets
    - [Widgets](#widgets)
        - [Widgets().button](#widgetsbutton)
        - [Widgets().check](#widgetscheck)
        - [Widgets().dropdown](#widgetsdropdown)
        - [Widgets().fileBrowser](#widgetsfilebrowser)
        - [Widgets().getImgData](#widgetsgetimgdata)
        - [Widgets().helpArgHelp](#widgetshelparghelp)
        - [Widgets().helpArgName](#widgetshelpargname)
        - [Widgets().helpArgNameAndHelp](#widgetshelpargnameandhelp)
        - [Widgets().helpDropdownWidget](#widgetshelpdropdownwidget)
        - [Widgets().helpFileWidget](#widgetshelpfilewidget)
        - [Widgets().helpFlagWidget](#widgetshelpflagwidget)
        - [Widgets().helpTextWidget](#widgetshelptextwidget)
        - [Widgets().inputText](#widgetsinputtext)
        - [Widgets().label](#widgetslabel)
        - [Widgets().stringSentencecase](#widgetsstringsentencecase)
        - [Widgets().stringTitlecase](#widgetsstringtitlecase)
        - [Widgets().title](#widgetstitle)

attribute that can be overridden to provide the end user with customisation over
the size of the gui.

## Widgets

[[find in source code]](../../../../cli2gui/application/widgets.py#L15)

```python
class Widgets():
    def __init__(sizes: dict[str, Any], pySimpleGui: Any):
```

Widgets class holding methods to create widgets in addition to a sizes...

attribute that can be overridden to provide the end user with customisation
over the size of the gui.

### Widgets().button

[[find in source code]](../../../../cli2gui/application/widgets.py#L80)

```python
def button(text: str) -> Element:
```

Return a button.

### Widgets().check

[[find in source code]](../../../../cli2gui/application/widgets.py#L74)

```python
def check(key: str) -> Element:
```

Return a checkbox.

### Widgets().dropdown

[[find in source code]](../../../../cli2gui/application/widgets.py#L101)

```python
def dropdown(key: str, argItems: list[str]) -> Element:
```

Return a dropdown.

### Widgets().fileBrowser

[[find in source code]](../../../../cli2gui/application/widgets.py#L110)

```python
def fileBrowser(key: str) -> list[Element]:
```

Return a fileBrowser button and field.

### Widgets().getImgData

[[find in source code]](../../../../cli2gui/application/widgets.py#L29)

```python
def getImgData(imagePath: str, first: bool = False) -> bytes:
```

Generate image data using PIL.

### Widgets().helpArgHelp

[[find in source code]](../../../../cli2gui/application/widgets.py#L135)

```python
def helpArgHelp(helpText: str) -> Element:
```

Return a label for the arg help text.

### Widgets().helpArgName

[[find in source code]](../../../../cli2gui/application/widgets.py#L131)

```python
def helpArgName(displayName: str, commands: list[str]) -> Element:
```

Return a label for the arg name.

### Widgets().helpArgNameAndHelp

[[find in source code]](../../../../cli2gui/application/widgets.py#L139)

```python
def helpArgNameAndHelp(
    commands: list[str],
    helpText: str,
    displayName: str,
) -> Element:
```

Return a column containing the argument name and help text.

### Widgets().helpDropdownWidget

[[find in source code]](../../../../cli2gui/application/widgets.py#L194)

```python
def helpDropdownWidget(
    displayName: str,
    commands: list[str],
    helpText: str,
    dest: str,
    choices: list[str],
) -> list[Element]:
```

Return a set of widgets that make up an arg with a choice.

### Widgets().helpFileWidget

[[find in source code]](../../../../cli2gui/application/widgets.py#L185)

```python
def helpFileWidget(
    displayName: str,
    commands: list[str],
    helpText: str,
    dest: str,
) -> list[Element]:
```

Return a set of widgets that make up an arg with a file.

### Widgets().helpFlagWidget

[[find in source code]](../../../../cli2gui/application/widgets.py#L167)

```python
def helpFlagWidget(
    displayName: str,
    commands: list[str],
    helpText: str,
    dest: str,
) -> list[Element]:
```

Return a set of widgets that make up an arg with true/ false.

### Widgets().helpTextWidget

[[find in source code]](../../../../cli2gui/application/widgets.py#L176)

```python
def helpTextWidget(
    displayName: str,
    commands: list[str],
    helpText: str,
    dest: str,
) -> list[Element]:
```

Return a set of widgets that make up an arg with text.

### Widgets().inputText

[[find in source code]](../../../../cli2gui/application/widgets.py#L65)

```python
def inputText(key: str) -> Element:
```

Return an input text field.

### Widgets().label

[[find in source code]](../../../../cli2gui/application/widgets.py#L89)

```python
def label(text: str, font: int = 11) -> Element:
```

Return a label.

### Widgets().stringSentencecase

[[find in source code]](../../../../cli2gui/application/widgets.py#L55)

```python
def stringSentencecase(string: str) -> str:
```

Convert a string to sentence case.

### Widgets().stringTitlecase

[[find in source code]](../../../../cli2gui/application/widgets.py#L40)

```python
def stringTitlecase(string: str, splitStr: str = 'ALL'):
```

Convert a string to title case.

### Widgets().title

[[find in source code]](../../../../cli2gui/application/widgets.py#L146)

```python
def title(text: str, image: str = '') -> list[Element]:
```

Return a set of widgets that make up the application header.
