# DearPyGuiWrapper

[Cli2gui Index](../../README.md#cli2gui-index) / [Cli2gui](../index.md#cli2gui) / [Gui](./index.md#gui) / DearPyGuiWrapper

> Auto-generated documentation for [cli2gui.gui.dearpygui_wrapper](../../../../cli2gui/gui/dearpygui_wrapper.py) module.

- [DearPyGuiWrapper](#dearpyguiwrapper)
  - [DearPyGuiWrapper](#dearpyguiwrapper-1)
    - [DearPyGuiWrapper().addItemsAndGroups](#dearpyguiwrapper()additemsandgroups)
    - [DearPyGuiWrapper().addWidgetFromItem](#dearpyguiwrapper()addwidgetfromitem)
    - [DearPyGuiWrapper().main](#dearpyguiwrapper()main)
    - [DearPyGuiWrapper().open_menu_item](#dearpyguiwrapper()open_menu_item)
  - [hex_to_rgb](#hex_to_rgb)

## DearPyGuiWrapper

[Show source in dearpygui_wrapper.py:24](../../../../cli2gui/gui/dearpygui_wrapper.py#L24)

Wrapper class for Dear PyGui.

#### Signature

```python
class DearPyGuiWrapper(AbstractGUI):
    def __init__(self, base24Theme: list[str]) -> None: ...
```

#### See also

- [AbstractGUI](./abstract_gui.md#abstractgui)

### DearPyGuiWrapper().addItemsAndGroups

[Show source in dearpygui_wrapper.py:86](../../../../cli2gui/gui/dearpygui_wrapper.py#L86)

Items and groups and return a list of these so we can get values from the dpg widgets.

:param types.Group section: section with a name to display and items

#### Returns

Type: *list[types.Item]*
flattened list of items

#### Signature

```python
def addItemsAndGroups(self, section: types.Group) -> list[types.Item]: ...
```

### DearPyGuiWrapper().addWidgetFromItem

[Show source in dearpygui_wrapper.py:70](../../../../cli2gui/gui/dearpygui_wrapper.py#L70)

Select a widget based on the item type.

:param types.Item item: the item

#### Signature

```python
def addWidgetFromItem(self, item: types.Item) -> None: ...
```

### DearPyGuiWrapper().main

[Show source in dearpygui_wrapper.py:130](../../../../cli2gui/gui/dearpygui_wrapper.py#L130)

Run the gui (dpg) with a given buildSpec, quit_callback, and run_callback.

- Theming + Configure dpg
- Menu Prep
- Create Window, set up Menu and Widgets
- Then, start dpg

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

### DearPyGuiWrapper().open_menu_item

[Show source in dearpygui_wrapper.py:116](../../../../cli2gui/gui/dearpygui_wrapper.py#L116)

Open a menu item.

#### Arguments

- `sender` *_type_* - file to open
- `_app_data` *_type_* - [unused]

#### Signature

```python
def open_menu_item(self, sender: str, _app_data: None) -> None: ...
```



## hex_to_rgb

[Show source in dearpygui_wrapper.py:15](../../../../cli2gui/gui/dearpygui_wrapper.py#L15)

Convert a color hex code to a tuple of integers (r, g, b).

#### Signature

```python
def hex_to_rgb(hex_code: str) -> tuple[int, int, int, int]: ...
```