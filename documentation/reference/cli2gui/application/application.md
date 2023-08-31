# Application

[Cli2gui Index](../../README.md#cli2gui-index) /
[Cli2gui](../index.md#cli2gui) /
[Application](./index.md#application) /
Application

> Auto-generated documentation for [cli2gui.application.application](../../../../cli2gui/application/application.py) module.

- [Application](#application)
  - [addItemsAndGroups](#additemsandgroups)
  - [createLayout](#createlayout)
  - [generatePopup](#generatepopup)
  - [run](#run)
  - [setBase24Theme](#setbase24theme)
  - [setupWidgets](#setupwidgets)
  - [themeFromFile](#themefromfile)

## addItemsAndGroups

[Show source in application.py:165](../../../../cli2gui/application/application.py#L165)

Add arg_items and groups to the argConstruct list.

#### Arguments

- `section` *types.Group* - contents/ section containing name, arg_items
and groups
- `argConstruct` *list[list[Element]]* - list of widgets to
add to the program window
- `widgets` *Widgets* - widgets object used to generate widgets to add to
argConstruct

#### Returns

- `list` - updated argConstruct

#### Signature

```python
def addItemsAndGroups(
    section: types.Group, argConstruct: list[list[Element]], widgets: Widgets
):
    ...
```

#### See also

- [Widgets](./widgets.md#widgets)



## createLayout

[Show source in application.py:265](../../../../cli2gui/application/application.py#L265)

Create the pysimplegui layout from the build spec.

#### Arguments

- `buildSpec` *types.FullBuildSpec* - build spec containing widget
- `widgets` *Widgets* - class to build widgets
- `pySimpleGui` *Any* - version of PySimpleGui to use
- `menu` *list[str]]* - menu data

#### Returns

- `list[list[Element]]` - list of widgets (layout list)

#### Signature

```python
def createLayout(
    buildSpec: types.FullBuildSpec,
    widgets: Widgets,
    pySimpleGui: Any,
    menu: str | list[str],
) -> list[list[Element]]:
    ...
```

#### See also

- [Widgets](./widgets.md#widgets)



## generatePopup

[Show source in application.py:196](../../../../cli2gui/application/application.py#L196)

Create the popup window.

#### Arguments

- `buildSpec` *types.FullBuildSpec* - [description]
values (Union[dict[Any, Any]): Returned when a button is clicked. Such
as the menu
- `widgets` *Widgets* - class to build widgets
- `pySimpleGui` *Any* - PySimpleGui class

#### Returns

- `pySimpleGui.Window` - A PySimpleGui Window

#### Signature

```python
def generatePopup(
    buildSpec: types.FullBuildSpec,
    values: dict[Any, Any] | list[Any],
    widgets: Widgets,
    pySimpleGui: Any,
) -> Window:
    ...
```

#### See also

- [Widgets](./widgets.md#widgets)



## run

[Show source in application.py:328](../../../../cli2gui/application/application.py#L328)

Main entry point for the application.

#### Arguments

- `buildSpec` *types.FullBuildSpec* - args that customise the application such as the theme
or the function to run

#### Signature

```python
def run(buildSpec: types.FullBuildSpec):
    ...
```



## setBase24Theme

[Show source in application.py:36](../../../../cli2gui/application/application.py#L36)

Set the base24 theme to the application.

#### Arguments

theme (Union[str, list[str]]): the light theme
darkTheme (Union[str, list[str]]): the dark theme
- `pySimpleGui` *Any* - pysimplegui module

#### Signature

```python
def setBase24Theme(
    theme: str | list[str], darkTheme: str | list[str], pySimpleGui: Any
) -> None:
    ...
```



## setupWidgets

[Show source in application.py:125](../../../../cli2gui/application/application.py#L125)

Set the widget sizes to the application.

#### Arguments

- `gui` *str* - user selected gui eg. pysimpleguiqt
sizes (Union[dict[str, Any]]): widget sizes
- `pySimpleGui` *Any* - pysimplegui module

#### Returns

- `Widgets` - widgets object all set up nicely

#### Signature

```python
def setupWidgets(gui: str, sizes: dict[str, Any], pySimpleGui: Any) -> Widgets:
    ...
```

#### See also

- [Widgets](./widgets.md#widgets)



## themeFromFile

[Show source in application.py:23](../../../../cli2gui/application/application.py#L23)

Set the base24 theme from a base24 scheme.yaml to the application.

#### Arguments

- `themeFile` *str* - path to file

#### Returns

- `list[str]` - theme to set

#### Signature

```python
def themeFromFile(themeFile: str) -> list[str]:
    ...
```