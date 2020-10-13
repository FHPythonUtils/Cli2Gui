Module cli2gui.application.application
======================================
Application here uses PySimpleGUI

Functions
---------

    
`addItemsAndGroups(section: c2gtypes.Group, argConstruct: list[list[pySimpleGuiType.Element]], widgets: Widgets)`
:   Add arg_items and groups to the argConstruct list
    
    Args:
            section (c2gtypes.Group): contents/ section containing name, arg_items
            and groups
            argConstruct (list[list[pySimpleGuiType.Element]]): list of widgets to
            add to the program window
            widgets (Widgets): widgets object used to generate widgets to add to
            argConstruct
    
    Returns:
            list: updated argConstruct

    
`createLayout(buildSpec: c2gtypes.FullBuildSpec, widgets: Widgets, pySimpleGui: pySimpleGuiType, menu: Union[list[str], None]) ‑> list[list[Element]]`
:   Create the pysimplegui layout from the build spec
    
    Args:
            build_spec (c2gtypes.FullBuildSpec): build spec containing widget
            descriptions, program name, description etc.
            widgets (Widgets): class to build widgets
    
    Returns:
            list[list[Element]]: list of widgets (layout list)

    
`generatePopup(buildSpec: c2gtypes.FullBuildSpec, values: Union[dict[Any, Any], list[Any]], widgets: Widgets, pySimpleGui: pySimpleGuiType) ‑> pySimpleGuiType.Window`
:   Create the popup window
    
    Args:
            buildSpec (c2gtypes.FullBuildSpec): [description]
            values (Union[dict[Any, Any]): Returned when a button is clicked. Such
            as the menu
            widgets (Widgets): class to build widgets
            pySimpleGui (pySimpleGuiType): PySimpleGui class
    
    Returns:
            pySimpleGui.Window: A PySimpleGui Window

    
`getYamlDict(yamlFileName: str) ‑> dict[str, str]`
:   Return a yaml_dict from reading yaml_file. If yaml_file is empty or
    doesn't exist, return an empty dict instead.

    
`run(buildSpec: c2gtypes.FullBuildSpec)`
:   Main entry point for the application
    
    Args:
            buildSpec (c2gtypes.FullBuildSpec): args that customise the application such as the theme
            or the function to run

    
`setBase24Theme(theme: Union[str, list[str], None], darkTheme: Union[str, list[str], None], pySimpleGui: pySimpleGuiType) ‑> None`
:   Set the base24 theme to the application
    
    Args:
            theme (Union[str, list[str], None]): the light theme
            darkTheme (Union[str, list[str], None]): the dark theme
            pySimpleGui (pySimpleGuiType): pysimplegui module

    
`setupWidgets(gui: str, sizes: Union[dict[str, Any], None], pySimpleGui: pySimpleGuiType) ‑> Widgets`
:   Set the widget sizes to the application
    
    Args:
            gui (str): user selected gui eg. pysimpleguiqt
            sizes (Union[dict[str, Any], None]): widget sizes
            pySimpleGui (pySimpleGuiType): pysimplegui module
    
    Returns:
            Widgets: widgets object all set up nicely

    
`themeFromFile(theme: str) ‑> list[str]`
:   Set the base24 theme from a base24 scheme.yaml to the application
    
    Args:
            theme (str): path to file
    
    Returns:
            list[str]: theme to set