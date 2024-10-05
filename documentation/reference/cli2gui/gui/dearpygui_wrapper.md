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

[Show source in dearpygui_wrapper.py:104](../../../../cli2gui/gui/dearpygui_wrapper.py#L104)

Items and groups and return a list of these so we can get values from the dpg widgets.

#### Arguments

- `section` *Group* - section with a name to display and items

#### Returns

Type: *list[Item]*
flattened list of items

#### Signature

```python
def addItemsAndGroups(self, section: Group) -> list[Item]: ...
```

#### See also

- [Group](../types.md#group)
- [Item](../types.md#item)

### DearPyGuiWrapper().addWidgetFromItem

[Show source in dearpygui_wrapper.py:83](../../../../cli2gui/gui/dearpygui_wrapper.py#L83)

Select a widget based on the item type.

#### Arguments

- `item` *Item* - the item

#### Signature

```python
def addWidgetFromItem(self, item: Item) -> None: ...
```

#### See also

- [Item](../types.md#item)

### DearPyGuiWrapper().main

[Show source in dearpygui_wrapper.py:148](../../../../cli2gui/gui/dearpygui_wrapper.py#L148)

Run the gui (dpg) with a given buildSpec, quit_callback, and run_callback.

- Theming + Configure dpg
- Menu Prep
- Create Window, set up Menu and Widgets
- Then, start dpg

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

### DearPyGuiWrapper().open_menu_item

[Show source in dearpygui_wrapper.py:134](../../../../cli2gui/gui/dearpygui_wrapper.py#L134)

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