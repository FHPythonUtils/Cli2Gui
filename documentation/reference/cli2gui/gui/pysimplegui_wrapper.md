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

[Show source in pysimplegui_wrapper.py:16](../../../../cli2gui/gui/pysimplegui_wrapper.py#L16)

Wrapper class for PySimpleGUI.

#### Signature

```python
class PySimpleGUIWrapper(AbstractGUI):
    def __init__(self, base24Theme: list[str], psg_lib: str) -> None: ...
```

#### See also

- [AbstractGUI](./abstract_gui.md#abstractgui)

### PySimpleGUIWrapper()._button

[Show source in pysimplegui_wrapper.py:99](../../../../cli2gui/gui/pysimplegui_wrapper.py#L99)

Return a button.

#### Signature

```python
def _button(self, text: str) -> Any: ...
```

### PySimpleGUIWrapper()._check

[Show source in pysimplegui_wrapper.py:89](../../../../cli2gui/gui/pysimplegui_wrapper.py#L89)

Return a checkbox.

#### Signature

```python
def _check(self, key: str, default: str | None = None) -> Any: ...
```

### PySimpleGUIWrapper()._dropdown

[Show source in pysimplegui_wrapper.py:120](../../../../cli2gui/gui/pysimplegui_wrapper.py#L120)

Return a dropdown.

#### Signature

```python
def _dropdown(self, key: str, argItems: list[str]) -> Any: ...
```

### PySimpleGUIWrapper()._fileBrowser

[Show source in pysimplegui_wrapper.py:129](../../../../cli2gui/gui/pysimplegui_wrapper.py#L129)

Return a fileBrowser button and field.

#### Signature

```python
def _fileBrowser(
    self,
    key: str,
    default: str | None = None,
    _type: ItemType = ItemType.File,
    additional_properties: dict | None = None,
) -> list[Any]: ...
```

#### See also

- [ItemType](../types.md#itemtype)

### PySimpleGUIWrapper()._helpArgHelp

[Show source in pysimplegui_wrapper.py:178](../../../../cli2gui/gui/pysimplegui_wrapper.py#L178)

Return a label for the arg help text.

#### Signature

```python
def _helpArgHelp(self, helpText: str) -> Any: ...
```

### PySimpleGUIWrapper()._helpArgName

[Show source in pysimplegui_wrapper.py:174](../../../../cli2gui/gui/pysimplegui_wrapper.py#L174)

Return a label for the arg name.

#### Signature

```python
def _helpArgName(self, displayName: str, commands: list[str]) -> Any: ...
```

### PySimpleGUIWrapper()._helpArgNameAndHelp

[Show source in pysimplegui_wrapper.py:182](../../../../cli2gui/gui/pysimplegui_wrapper.py#L182)

Return a column containing the argument name and help text.

#### Signature

```python
def _helpArgNameAndHelp(
    self, commands: list[str], helpText: str, displayName: str
) -> Any: ...
```

### PySimpleGUIWrapper()._helpCounterWidget

[Show source in pysimplegui_wrapper.py:233](../../../../cli2gui/gui/pysimplegui_wrapper.py#L233)

Return a set of self that make up an arg with text.

#### Signature

```python
def _helpCounterWidget(self, item: Item) -> list[Any]: ...
```

#### See also

- [Item](../types.md#item)

### PySimpleGUIWrapper()._helpDropdownWidget

[Show source in pysimplegui_wrapper.py:258](../../../../cli2gui/gui/pysimplegui_wrapper.py#L258)

Return a set of self that make up an arg with a choice.

#### Signature

```python
def _helpDropdownWidget(self, item: Item) -> list[Any]: ...
```

#### See also

- [Item](../types.md#item)

### PySimpleGUIWrapper()._helpFileWidget

[Show source in pysimplegui_wrapper.py:245](../../../../cli2gui/gui/pysimplegui_wrapper.py#L245)

Return a set of self that make up an arg with a file.

#### Signature

```python
def _helpFileWidget(self, item: Item) -> list[Any]: ...
```

#### See also

- [Item](../types.md#item)

### PySimpleGUIWrapper()._helpFlagWidget

[Show source in pysimplegui_wrapper.py:208](../../../../cli2gui/gui/pysimplegui_wrapper.py#L208)

Return a set of self that make up an arg with true/ false.

#### Signature

```python
def _helpFlagWidget(self, item: Item) -> list[Any]: ...
```

#### See also

- [Item](../types.md#item)

### PySimpleGUIWrapper()._helpTextWidget

[Show source in pysimplegui_wrapper.py:220](../../../../cli2gui/gui/pysimplegui_wrapper.py#L220)

Return a set of self that make up an arg with text.

#### Signature

```python
def _helpTextWidget(self, item: Item) -> list[Any]: ...
```

#### See also

- [Item](../types.md#item)

### PySimpleGUIWrapper()._inputText

[Show source in pysimplegui_wrapper.py:68](../../../../cli2gui/gui/pysimplegui_wrapper.py#L68)

Return an input text field.

#### Signature

```python
def _inputText(self, key: str, default: str | None = None) -> Any: ...
```

### PySimpleGUIWrapper()._label

[Show source in pysimplegui_wrapper.py:108](../../../../cli2gui/gui/pysimplegui_wrapper.py#L108)

Return a label.

#### Signature

```python
def _label(self, text: str, font: int = 11) -> Any: ...
```

### PySimpleGUIWrapper()._spin

[Show source in pysimplegui_wrapper.py:78](../../../../cli2gui/gui/pysimplegui_wrapper.py#L78)

Return an input text field.

#### Signature

```python
def _spin(self, key: str, default: str | None = None) -> Any: ...
```

### PySimpleGUIWrapper()._title

[Show source in pysimplegui_wrapper.py:189](../../../../cli2gui/gui/pysimplegui_wrapper.py#L189)

Return a set of self that make up the application header.

#### Signature

```python
def _title(self, text: str, image: str = "") -> list[Any]: ...
```

### PySimpleGUIWrapper().addItemsAndGroups

[Show source in pysimplegui_wrapper.py:361](../../../../cli2gui/gui/pysimplegui_wrapper.py#L361)

Items and groups and return a list of psg Elements.

#### Arguments

- `section` *Group* - section with a name to display and items

#### Returns

Type: *list[list[Element]]*
updated argConstruct

#### Signature

```python
def addItemsAndGroups(self, section: Group) -> list[list[Any]]: ...
```

#### See also

- [Group](../types.md#group)

### PySimpleGUIWrapper().addWidgetFromItem

[Show source in pysimplegui_wrapper.py:277](../../../../cli2gui/gui/pysimplegui_wrapper.py#L277)

Select a widget based on the item type.

#### Arguments

- `item` *Item* - the item

#### Signature

```python
def addWidgetFromItem(self, item: Item) -> list[Any]: ...
```

#### See also

- [Item](../types.md#item)

### PySimpleGUIWrapper().createLayout

[Show source in pysimplegui_wrapper.py:386](../../../../cli2gui/gui/pysimplegui_wrapper.py#L386)

Create the pysimplegui layout from the build spec.

#### Arguments

----
 - `buildSpec` *FullBuildSpec* - build spec containing widget
 - `self` *self* - class to build self

#### Returns

-------
 - `list[list[Any]]` - list of self (layout list)

#### Signature

```python
def createLayout(
    self, buildSpec: FullBuildSpec, menu: str | list[str]
) -> list[list[Any]]: ...
```

#### See also

- [FullBuildSpec](../types.md#fullbuildspec)

### PySimpleGUIWrapper().generatePopup

[Show source in pysimplegui_wrapper.py:301](../../../../cli2gui/gui/pysimplegui_wrapper.py#L301)

Create the popup window.

#### Arguments

----
 - `buildSpec` *FullBuildSpec* - [description]
 values (Union[dict[Any, Any]): Returned when a button is clicked. Such
 as the menu

#### Returns

-------
 - `Window` - A PySimpleGui Window

#### Signature

```python
def generatePopup(
    self, buildSpec: FullBuildSpec, values: dict[Any, Any] | list[Any]
) -> Any: ...
```

#### See also

- [FullBuildSpec](../types.md#fullbuildspec)

### PySimpleGUIWrapper().getImgData

[Show source in pysimplegui_wrapper.py:503](../../../../cli2gui/gui/pysimplegui_wrapper.py#L503)

Generate image data using PIL.

#### Signature

```python
def getImgData(self, imagePath: str, first: bool = False) -> bytes: ...
```

### PySimpleGUIWrapper().main

[Show source in pysimplegui_wrapper.py:458](../../../../cli2gui/gui/pysimplegui_wrapper.py#L458)

Run the gui (psg) with a given buildSpec, quit_callback, and run_callback.

#### Arguments

- `buildSpec` *FullBuildSpec* - Full cli parse/ build spec
:param Callable[[], None] quit_callback: generic callable used to quit
:param Callable[[dict[str, Any]], None] run_callback: generic callable used to run

#### Signature

```python
def main(
    self,
    buildSpec: FullBuildSpec,
    quit_callback: Callable[[], None],
    run_callback: Callable[[dict[str, Any]], None],
) -> None: ...
```

#### See also

- [FullBuildSpec](../types.md#fullbuildspec)