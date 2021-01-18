# widgets

> Auto-generated documentation for [cli2gui.application.widgets](../../../cli2gui/application/widgets.py) module.

Widgets class holding methods to create widgets in addition to a sizes
attribute that can be overridden to provide the end user with customisation over
the size of the gui

- [Cli2gui](../../README.md#cli2gui-index) / [Modules](../../README.md#cli2gui-modules) / [cli2gui](../index.md#cli2gui) / [application](index.md#application) / widgets
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

## Widgets

[[find in source code]](../../../cli2gui/application/widgets.py#L14)

```python
class Widgets():
    def __init__(sizes: dict[(str, Any)], pySimpleGui: Any):
```

Widgets class holding methods to create widgets in addition to a sizes
attribute that can be overridden to provide the end user with customisation
over the size of the gui

### Widgets().button

[[find in source code]](../../../cli2gui/application/widgets.py#L69)

```python
def button(text: str) -> pySimpleGuiType.Element:
```

Return a button

### Widgets().check

[[find in source code]](../../../cli2gui/application/widgets.py#L65)

```python
def check(key: str) -> pySimpleGuiType.Element:
```

Return a checkbox

### Widgets().dropdown

[[find in source code]](../../../cli2gui/application/widgets.py#L77)

```python
def dropdown(key: str, arg_items: list[str]) -> pySimpleGuiType.Element:
```

Return a dropdown

### Widgets().fileBrowser

[[find in source code]](../../../cli2gui/application/widgets.py#L81)

```python
def fileBrowser(key: str) -> list[pySimpleGuiType.Element]:
```

Return a fileBrowser button and field

### Widgets().getImgData

[[find in source code]](../../../cli2gui/application/widgets.py#L25)

```python
def getImgData(
    imagePath: Union[(str, None)],
    first: bool = False,
) -> Union[(bytes, None)]:
```

Generate image data using PIL

### Widgets().helpArgHelp

[[find in source code]](../../../cli2gui/application/widgets.py#L94)

```python
def helpArgHelp(helpText: str) -> pySimpleGuiType.Element:
```

Return a label for the arg help text

### Widgets().helpArgName

[[find in source code]](../../../cli2gui/application/widgets.py#L91)

```python
def helpArgName(
    displayName: str,
    commands: list[str],
) -> pySimpleGuiType.Element:
```

Return a label for the arg name

### Widgets().helpArgNameAndHelp

[[find in source code]](../../../cli2gui/application/widgets.py#L97)

```python
def helpArgNameAndHelp(
    commands: list[str],
    helpText: str,
    displayName: str,
) -> pySimpleGuiType.Element:
```

Return a column containing the argument name and help text

### Widgets().helpDropdownWidget

[[find in source code]](../../../cli2gui/application/widgets.py#L128)

```python
def helpDropdownWidget(
    displayName: str,
    commands: list[str],
    helpText: str,
    dest: str,
    choices: list[str],
) -> list[pySimpleGuiType.Element]:
```

Return a set of widgets that make up an arg with a choice

### Widgets().helpFileWidget

[[find in source code]](../../../cli2gui/application/widgets.py#L123)

```python
def helpFileWidget(
    displayName: str,
    commands: list[str],
    helpText: str,
    dest: str,
) -> list[pySimpleGuiType.Element]:
```

Return a set of widgets that make up an arg with a file

### Widgets().helpFlagWidget

[[find in source code]](../../../cli2gui/application/widgets.py#L113)

```python
def helpFlagWidget(
    displayName: str,
    commands: list[str],
    helpText: str,
    dest: str,
) -> list[pySimpleGuiType.Element]:
```

Return a set of widgets that make up an arg with true/ false

### Widgets().helpTextWidget

[[find in source code]](../../../cli2gui/application/widgets.py#L118)

```python
def helpTextWidget(
    displayName: str,
    commands: list[str],
    helpText: str,
    dest: str,
) -> list[pySimpleGuiType.Element]:
```

Return a set of widgets that make up an arg with text

### Widgets().inputText

[[find in source code]](../../../cli2gui/application/widgets.py#L60)

```python
def inputText(key: str) -> pySimpleGuiType.Element:
```

Return an input text field

### Widgets().label

[[find in source code]](../../../cli2gui/application/widgets.py#L73)

```python
def label(text: str, font: int = 11) -> pySimpleGuiType.Element:
```

Return a label

### Widgets().stringSentencecase

[[find in source code]](../../../cli2gui/application/widgets.py#L50)

```python
def stringSentencecase(string: Union[(str, None)]) -> str:
```

Convert a string to sentence case

### Widgets().stringTitlecase

[[find in source code]](../../../cli2gui/application/widgets.py#L37)

```python
def stringTitlecase(string: Union[(str, None)], splitStr: str = 'ALL'):
```

Convert a string to title case

### Widgets().title

[[find in source code]](../../../cli2gui/application/widgets.py#L102)

```python
def title(
    text: str,
    image: Union[(str, None)] = None,
) -> list[pySimpleGuiType.Element]:
```

Return a set of widgets that make up the application header
