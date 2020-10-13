Module cli2gui.application.widgets
==================================
Widgets class holding methods to create widgets in addition to a sizes
attribute that can be overridden to provide the end user with customisation over
the size of the gui

Classes
-------

`Widgets(sizes: dict[str, Any], pySimpleGui: pySimpleGuiType)`
:   Widgets class holding methods to create widgets in addition to a sizes
    attribute that can be overridden to provide the end user with customisation
    over the size of the gui

    ### Methods

    `button(self, text: str) ‑> PySimpleGUI.PySimpleGUI.Element`
    :   Return a button

    `check(self, key: str) ‑> PySimpleGUI.PySimpleGUI.Element`
    :   Return a checkbox

    `dropdown(self, key: str, arg_items: list[str]) ‑> pySimpleGuiType.Element`
    :   Return a dropdown

    `fileBrowser(self, key: str) ‑> list[pySimpleGuiType.Element]`
    :   Return a fileBrowser button and field

    `getImgData(self, imagePath: Union[str, None], first: bool = False) ‑> Union[bytes, NoneType]`
    :   Generate image data using PIL

    `helpArgHelp(self, helpText: str) ‑> PySimpleGUI.PySimpleGUI.Element`
    :   Return a label for the arg help text

    `helpArgName(self, displayName: str, commands: list[str]) ‑> pySimpleGuiType.Element`
    :   Return a label for the arg name

    `helpArgNameAndHelp(self, commands: list[str], helpText: str, displayName: str) ‑> pySimpleGuiType.Element`
    :   Return a column containing the argument name and help text

    `helpDropdownWidget(self, displayName: str, commands: list[str], helpText: str, dest: str, choices: list[str]) ‑> list[pySimpleGuiType.Element]`
    :   Return a set of widgets that make up an arg with a choice

    `helpFileWidget(self, displayName: str, commands: list[str], helpText: str, dest: str) ‑> list[pySimpleGuiType.Element]`
    :   Return a set of widgets that make up an arg with a file

    `helpFlagWidget(self, displayName: str, commands: list[str], helpText: str, dest: str) ‑> list[pySimpleGuiType.Element]`
    :   Return a set of widgets that make up an arg with true/ false

    `helpTextWidget(self, displayName: str, commands: list[str], helpText: str, dest: str) ‑> list[pySimpleGuiType.Element]`
    :   Return a set of widgets that make up an arg with text

    `inputText(self, key: str) ‑> PySimpleGUI.PySimpleGUI.Element`
    :   Return an input text field

    `label(self, text: str, font: int = 11) ‑> PySimpleGUI.PySimpleGUI.Element`
    :   Return a label

    `stringSentencecase(self, string: Union[str, None]) ‑> str`
    :   Convert a string to sentence case

    `stringTitlecase(self, string: Union[str, None], splitStr: str = 'ALL')`
    :   Convert a string to title case

    `title(self, text: str, image: Union[str, None] = None) ‑> list[pySimpleGuiType.Element]`
    :   Return a set of widgets that make up the application header