# application

> Auto-generated documentation for [cli2gui.application.application](../../../cli2gui/application/application.py) module.

Application here uses PySimpleGUI.

- [Cli2gui](../../README.md#cli2gui-index) / [Modules](../../README.md#cli2gui-modules) / [cli2gui](../index.md#cli2gui) / [application](index.md#application) / application
    - [addItemsAndGroups](#additemsandgroups)
    - [createLayout](#createlayout)
    - [generatePopup](#generatepopup)
    - [run](#run)
    - [setBase24Theme](#setbase24theme)
    - [setupWidgets](#setupwidgets)
    - [themeFromFile](#themefromfile)

## addItemsAndGroups

[[find in source code]](../../../cli2gui/application/application.py#L165)

```python
def addItemsAndGroups(
    section: c2gtypes.Group,
    argConstruct: list[list[Element]],
    widgets: Widgets,
):
```

Add arg_items and groups to the argConstruct list.

#### Arguments

- `section` *c2gtypes.Group* - contents/ section containing name, arg_items
and groups
- `argConstruct` *list[list[Element]]* - list of widgets to
add to the program window
- `widgets` *Widgets* - widgets object used to generate widgets to add to
argConstruct

#### Returns

- `list` - updated argConstruct

## createLayout

[[find in source code]](../../../cli2gui/application/application.py#L298)

```python
def createLayout(
    buildSpec: c2gtypes.FullBuildSpec,
    widgets: Widgets,
    pySimpleGui: Any,
    menu: str | list[str],
) -> list[list[Element]]:
```

Create the pysimplegui layout from the build spec.

#### Arguments

- `buildSpec` *c2gtypes.FullBuildSpec* - build spec containing widget
- `widgets` *Widgets* - class to build widgets
- `pySimpleGui` *Any* - version of PySimpleGui to use
- `menu` *list[str]]* - menu data

#### Returns

- `list[list[Element]]` - list of widgets (layout list)

## generatePopup

[[find in source code]](../../../cli2gui/application/application.py#L229)

```python
def generatePopup(
    buildSpec: c2gtypes.FullBuildSpec,
    values: dict[(Any, Any)] | list[Any],
    widgets: Widgets,
    pySimpleGui: Any,
) -> Window:
```

Create the popup window.

#### Arguments

- `buildSpec` *c2gtypes.FullBuildSpec* - [description]
values (Union[dict[Any, Any]): Returned when a button is clicked. Such
as the menu
- `widgets` *Widgets* - class to build widgets
- `pySimpleGui` *Any* - PySimpleGui class

#### Returns

- `pySimpleGui.Window` - A PySimpleGui Window

## run

[[find in source code]](../../../cli2gui/application/application.py#L361)

```python
def run(buildSpec: c2gtypes.FullBuildSpec):
```

Main entry point for the application.

#### Arguments

- `buildSpec` *c2gtypes.FullBuildSpec* - args that customise the application such as the theme
or the function to run

## setBase24Theme

[[find in source code]](../../../cli2gui/application/application.py#L36)

```python
def setBase24Theme(
    theme: str | list[str],
    darkTheme: str | list[str],
    pySimpleGui: Any,
) -> None:
```

Set the base24 theme to the application.

#### Arguments

theme (Union[str, list[str]]): the light theme
darkTheme (Union[str, list[str]]): the dark theme
- `pySimpleGui` *Any* - pysimplegui module

## setupWidgets

[[find in source code]](../../../cli2gui/application/application.py#L125)

```python
def setupWidgets(
    gui: str,
    sizes: dict[(str, Any)],
    pySimpleGui: Any,
) -> Widgets:
```

Set the widget sizes to the application.

#### Arguments

- `gui` *str* - user selected gui eg. pysimpleguiqt
sizes (Union[dict[str, Any]]): widget sizes
- `pySimpleGui` *Any* - pysimplegui module

#### Returns

- `Widgets` - widgets object all set up nicely

## themeFromFile

[[find in source code]](../../../cli2gui/application/application.py#L23)

```python
def themeFromFile(themeFile: str) -> list[str]:
```

Set the base24 theme from a base24 scheme.yaml to the application.

#### Arguments

- `themeFile` *str* - path to file

#### Returns

- `list[str]` - theme to set
