# PySimpleGUIWrapper

[Cli2gui Index](../../README.md#cli2gui-index) / [Cli2gui](../index.md#cli2gui) / [Gui](./index.md#gui) / PySimpleGUIWrapper

> Auto-generated documentation for [cli2gui.gui.pysimplegui_wrapper](../../../../cli2gui/gui/pysimplegui_wrapper.py) module.

- [PySimpleGUIWrapper](#pysimpleguiwrapper)
  - [PySimpleGUIWrapper](#pysimpleguiwrapper-1)
    - [PySimpleGUIWrapper()._button](#pysimpleguiwrapper()_button)
    - [PySimpleGUIWrapper()._check](#pysimpleguiwrapper()_check)
    - [PySimpleGUIWrapper()._dropdown](#pysimpleguiwrapper()_dropdown)
    - [PySimpleGUIWrapper()._fileBrowser](#pysimpleguiwrapper()_filebrowser)
    - [PySimpleGUIWrapper()._helpArgHelp](#pysimpleguiwrapper()_helparghelp)
    - [PySimpleGUIWrapper()._helpArgName](#pysimpleguiwrapper()_helpargname)
    - [PySimpleGUIWrapper()._helpArgNameAndHelp](#pysimpleguiwrapper()_helpargnameandhelp)
    - [PySimpleGUIWrapper()._helpCounterWidget](#pysimpleguiwrapper()_helpcounterwidget)
    - [PySimpleGUIWrapper()._helpDropdownWidget](#pysimpleguiwrapper()_helpdropdownwidget)
    - [PySimpleGUIWrapper()._helpFileWidget](#pysimpleguiwrapper()_helpfilewidget)
    - [PySimpleGUIWrapper()._helpFlagWidget](#pysimpleguiwrapper()_helpflagwidget)
    - [PySimpleGUIWrapper()._helpTextWidget](#pysimpleguiwrapper()_helptextwidget)
    - [PySimpleGUIWrapper()._inputText](#pysimpleguiwrapper()_inputtext)
    - [PySimpleGUIWrapper()._label](#pysimpleguiwrapper()_label)
    - [PySimpleGUIWrapper()._spin](#pysimpleguiwrapper()_spin)
    - [PySimpleGUIWrapper()._title](#pysimpleguiwrapper()_title)
    - [PySimpleGUIWrapper().addItemsAndGroups](#pysimpleguiwrapper()additemsandgroups)
    - [PySimpleGUIWrapper().addWidgetFromItem](#pysimpleguiwrapper()addwidgetfromitem)
    - [PySimpleGUIWrapper().createLayout](#pysimpleguiwrapper()createlayout)
    - [PySimpleGUIWrapper().generatePopup](#pysimpleguiwrapper()generatepopup)
    - [PySimpleGUIWrapper().getImgData](#pysimpleguiwrapper()getimgdata)
    - [PySimpleGUIWrapper().main](#pysimpleguiwrapper()main)

## PySimpleGUIWrapper

[Show source in pysimplegui_wrapper.py:17](../../../../cli2gui/gui/pysimplegui_wrapper.py#L17)

Wrapper class for PySimpleGUI.

#### Signature

```python
class PySimpleGUIWrapper(AbstractGUI):
    def __init__(self, base24Theme: list[str], psg_lib: str) -> None: ...
```

#### See also

- [AbstractGUI](./abstract_gui.md#abstractgui)

### PySimpleGUIWrapper()._button

[Show source in pysimplegui_wrapper.py:100](../../../../cli2gui/gui/pysimplegui_wrapper.py#L100)

Return a button.

#### Signature

```python
def _button(self, text: str) -> gui_lib.Element: ...
```

### PySimpleGUIWrapper()._check

[Show source in pysimplegui_wrapper.py:90](../../../../cli2gui/gui/pysimplegui_wrapper.py#L90)

Return a checkbox.

#### Signature

```python
def _check(self, key: str, default: str | None = None) -> gui_lib.Element: ...
```

### PySimpleGUIWrapper()._dropdown

[Show source in pysimplegui_wrapper.py:121](../../../../cli2gui/gui/pysimplegui_wrapper.py#L121)

Return a dropdown.

#### Signature

```python
def _dropdown(self, key: str, argItems: list[str]) -> gui_lib.Element: ...
```

### PySimpleGUIWrapper()._fileBrowser

[Show source in pysimplegui_wrapper.py:130](../../../../cli2gui/gui/pysimplegui_wrapper.py#L130)

Return a fileBrowser button and field.

#### Signature

```python
def _fileBrowser(
    self, key: str, default: str | None = None
) -> list[gui_lib.Element]: ...
```

### PySimpleGUIWrapper()._helpArgHelp

[Show source in pysimplegui_wrapper.py:157](../../../../cli2gui/gui/pysimplegui_wrapper.py#L157)

Return a label for the arg help text.

#### Signature

```python
def _helpArgHelp(self, helpText: str) -> gui_lib.Element: ...
```

### PySimpleGUIWrapper()._helpArgName

[Show source in pysimplegui_wrapper.py:153](../../../../cli2gui/gui/pysimplegui_wrapper.py#L153)

Return a label for the arg name.

#### Signature

```python
def _helpArgName(self, displayName: str, commands: list[str]) -> gui_lib.Element: ...
```

### PySimpleGUIWrapper()._helpArgNameAndHelp

[Show source in pysimplegui_wrapper.py:161](../../../../cli2gui/gui/pysimplegui_wrapper.py#L161)

Return a column containing the argument name and help text.

#### Signature

```python
def _helpArgNameAndHelp(
    self, commands: list[str], helpText: str, displayName: str
) -> gui_lib.Element: ...
```

### PySimpleGUIWrapper()._helpCounterWidget

[Show source in pysimplegui_wrapper.py:209](../../../../cli2gui/gui/pysimplegui_wrapper.py#L209)

Return a set of self that make up an arg with text.

#### Signature

```python
def _helpCounterWidget(self, item: types.Item) -> list[gui_lib.Element]: ...
```

### PySimpleGUIWrapper()._helpDropdownWidget

[Show source in pysimplegui_wrapper.py:229](../../../../cli2gui/gui/pysimplegui_wrapper.py#L229)

Return a set of self that make up an arg with a choice.

#### Signature

```python
def _helpDropdownWidget(self, item: types.Item) -> list[gui_lib.Element]: ...
```

### PySimpleGUIWrapper()._helpFileWidget

[Show source in pysimplegui_wrapper.py:219](../../../../cli2gui/gui/pysimplegui_wrapper.py#L219)

Return a set of self that make up an arg with a file.

#### Signature

```python
def _helpFileWidget(self, item: types.Item) -> list[gui_lib.Element]: ...
```

### PySimpleGUIWrapper()._helpFlagWidget

[Show source in pysimplegui_wrapper.py:189](../../../../cli2gui/gui/pysimplegui_wrapper.py#L189)

Return a set of self that make up an arg with true/ false.

#### Signature

```python
def _helpFlagWidget(self, item: types.Item) -> list[gui_lib.Element]: ...
```

### PySimpleGUIWrapper()._helpTextWidget

[Show source in pysimplegui_wrapper.py:199](../../../../cli2gui/gui/pysimplegui_wrapper.py#L199)

Return a set of self that make up an arg with text.

#### Signature

```python
def _helpTextWidget(self, item: types.Item) -> list[gui_lib.Element]: ...
```

### PySimpleGUIWrapper()._inputText

[Show source in pysimplegui_wrapper.py:69](../../../../cli2gui/gui/pysimplegui_wrapper.py#L69)

Return an input text field.

#### Signature

```python
def _inputText(self, key: str, default: str | None = None) -> gui_lib.Element: ...
```

### PySimpleGUIWrapper()._label

[Show source in pysimplegui_wrapper.py:109](../../../../cli2gui/gui/pysimplegui_wrapper.py#L109)

Return a label.

#### Signature

```python
def _label(self, text: str, font: int = 11) -> gui_lib.Element: ...
```

### PySimpleGUIWrapper()._spin

[Show source in pysimplegui_wrapper.py:79](../../../../cli2gui/gui/pysimplegui_wrapper.py#L79)

Return an input text field.

#### Signature

```python
def _spin(self, key: str, default: str | None = None) -> gui_lib.Element: ...
```

### PySimpleGUIWrapper()._title

[Show source in pysimplegui_wrapper.py:170](../../../../cli2gui/gui/pysimplegui_wrapper.py#L170)

Return a set of self that make up the application header.

#### Signature

```python
def _title(self, text: str, image: str = "") -> list[gui_lib.Element]: ...
```

### PySimpleGUIWrapper().addItemsAndGroups

[Show source in pysimplegui_wrapper.py:320](../../../../cli2gui/gui/pysimplegui_wrapper.py#L320)

Items and groups and return a list of psg Elements.

:param types.Group section: section with a name to display and items

#### Returns

Type: *list[list[Element]]*
updated argConstruct

#### Signature

```python
def addItemsAndGroups(self, section: types.Group) -> list[list[gui_lib.Element]]: ...
```

### PySimpleGUIWrapper().addWidgetFromItem

[Show source in pysimplegui_wrapper.py:242](../../../../cli2gui/gui/pysimplegui_wrapper.py#L242)

Select a widget based on the item type.

:param types.Item item: the item

#### Signature

```python
def addWidgetFromItem(self, item: types.Item) -> list[gui_lib.Element]: ...
```

### PySimpleGUIWrapper().createLayout

[Show source in pysimplegui_wrapper.py:345](../../../../cli2gui/gui/pysimplegui_wrapper.py#L345)

Create the pysimplegui layout from the build spec.

#### Arguments

----
 - `buildSpec` *types.FullBuildSpec* - build spec containing widget
 - `self` *self* - class to build self

#### Returns

-------
 - `list[list[gui_lib.Element]]` - list of self (layout list)

#### Signature

```python
def createLayout(
    self, buildSpec: types.FullBuildSpec, menu: str | list[str]
) -> list[list[gui_lib.Element]]: ...
```

### PySimpleGUIWrapper().generatePopup

[Show source in pysimplegui_wrapper.py:260](../../../../cli2gui/gui/pysimplegui_wrapper.py#L260)

Create the popup window.

#### Arguments

----
 - `buildSpec` *types.FullBuildSpec* - [description]
 values (Union[dict[Any, Any]): Returned when a button is clicked. Such
 as the menu

#### Returns

-------
 - `Window` - A PySimpleGui Window

#### Signature

```python
def generatePopup(
    self, buildSpec: types.FullBuildSpec, values: dict[Any, Any] | list[gui_lib.Element]
) -> gui_lib.Window: ...
```

### PySimpleGUIWrapper().getImgData

[Show source in pysimplegui_wrapper.py:459](../../../../cli2gui/gui/pysimplegui_wrapper.py#L459)

Generate image data using PIL.

#### Signature

```python
def getImgData(self, imagePath: str, first: bool = False) -> bytes: ...
```

### PySimpleGUIWrapper().main

[Show source in pysimplegui_wrapper.py:414](../../../../cli2gui/gui/pysimplegui_wrapper.py#L414)

Run the gui (psg) with a given buildSpec, quit_callback, and run_callback.

:param types.FullBuildSpec buildSpec: Full cli parse/ build spec
:param Callable[[], None] quit_callback: generic callable used to quit
:param Callable[[dict[str, Any]], None] run_callback: generic callable used to run

#### Signature

```python
def main(
    self,
    buildSpec: types.FullBuildSpec,
    quit_callback: Callable[[], None],
    run_callback: Callable[[dict[str, Any]], None],
) -> None: ...
```