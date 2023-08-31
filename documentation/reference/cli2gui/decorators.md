# Decorators

[Cli2gui Index](../README.md#cli2gui-index) /
[Cli2gui](./index.md#cli2gui) /
Decorators

> Auto-generated documentation for [cli2gui.decorators](../../../cli2gui/decorators.py) module.

- [Decorators](#decorators)
  - [Cli2Gui](#cli2gui)
  - [Click2Gui](#click2gui)
  - [createFromParser](#createfromparser)

## Cli2Gui

[Show source in decorators.py:168](../../../cli2gui/decorators.py#L168)

Decorator to use in the function that contains the argument parser.
Serialises data to JSON and launches the Cli2Gui application.

#### Arguments

run_function (Callable[..., Any]): The name of the function to call eg.
- `auto_enable` *bool, optional* - Enable the GUI by default. If enabled by
default requires `--disable-cli2gui`, otherwise requires `--cli2gui`.
Defaults to False.
- `parser` *str, optional* - Override the parser to use. Current
- `options` *are* - "argparse", "getopt", "optparse", "docopt",
"dephell_argparse". Defaults to "argparse".
- `gui` *str, optional* - Override the gui to use. Current options are:
"pysimplegui", "pysimpleguiqt","pysimpleguiweb". Defaults to
"pysimplegui".
theme (Union[str, list[str]], optional): Set a base24 theme. Can
also pass a base24 scheme file. eg. one-light.yaml. Defaults to "".
darkTheme (Union[str, list[str]], optional): Set a base24 dark
theme variant. Can also pass a base24 scheme file. eg. one-dark.yaml.
Defaults to "".
sizes (Union[dict[str, int]], optional): Set the UI sizes such as
the button size. Defaults to "".
- `image` *str, optional* - Set the program icon. File
extensions can be any that PIL supports. Defaults to "".
- `program_name` *str, optional* - Override the program name.
Defaults to "".
- `program_description` *str, optional* - Override the program
description. Defaults to "".
- `max_args_shown` *int, optional* - Maximum number of args shown before
using a scrollbar. Defaults to 5.
menu (Union[dict[str, Any]], optional): Add a menu to the program.
Defaults to "". eg. THIS_DIR = str(Path(__file__).resolve().parent)
- `menu={"File"` - THIS_DIR + "/file.md"}

#### Returns

- `Any` - Runs the application

#### Signature

```python
def Cli2Gui(
    run_function: Callable[..., Any],
    auto_enable: bool = False,
    parser: str | ParserType = "argparse",
    gui: str | ParserType = "pysimplegui",
    theme: str | list[str] = "",
    darkTheme: str | list[str] = "",
    sizes: str | dict[str, int] = "",
    image: str = "",
    program_name: str = "",
    program_description: str = "",
    max_args_shown: int = 5,
    menu: str | dict[str, Any] = "",
) -> Any:
    ...
```



## Click2Gui

[Show source in decorators.py:102](../../../cli2gui/decorators.py#L102)

Decorator to use in the function that contains the argument parser.
Serialises data to JSON and launches the Cli2Gui application.

#### Arguments

run_function (Callable[..., Any]): The name of the function to call eg.
- `gui` *str, optional* - Override the gui to use. Current options are:
"pysimplegui", "pysimpleguiqt","pysimpleguiweb". Defaults to
"pysimplegui".
theme (Union[str, list[str]], optional): Set a base24 theme. Can
also pass a base24 scheme file. eg. one-light.yaml. Defaults to "".
darkTheme (Union[str, list[str]], optional): Set a base24 dark
theme variant. Can also pass a base24 scheme file. eg. one-dark.yaml.
Defaults to "".
sizes (Union[dict[str, int]], optional): Set the UI sizes such as
the button size. Defaults to "".
- `image` *str, optional* - Set the program icon. File
extensions can be any that PIL supports. Defaults to "".
- `program_name` *str, optional* - Override the program name.
Defaults to "".
- `program_description` *str, optional* - Override the program
description. Defaults to "".
- `max_args_shown` *int, optional* - Maximum number of args shown before
using a scrollbar. Defaults to 5.
menu (Union[dict[str, Any]], optional): Add a menu to the program.
Defaults to "". eg. THIS_DIR = str(Path(__file__).resolve().parent)
- `menu={"File"` - THIS_DIR + "/file.md"}
**kwargs (dict[Any, Any]): kwargs

#### Returns

- `Any` - Runs the application

#### Signature

```python
def Click2Gui(
    run_function: Callable[..., Any],
    gui: str | GUIType = "pysimplegui",
    theme: str | list[str] = "",
    darkTheme: str | list[str] = "",
    sizes: str | dict[str, int] = "",
    image: str = "",
    program_name: str = "",
    program_description: str = "",
    max_args_shown: int = 5,
    menu: str | dict[str, Any] = "",
    **kwargs: dict[str, Any]
) -> Any:
    ...
```



## createFromParser

[Show source in decorators.py:30](../../../cli2gui/decorators.py#L30)

Generate a buildSpec from a parser.

#### Arguments

- `selfParser` *object* - A parser that acts on self. eg. ArgumentParser.parse_args
argsParser (Union[tuple[Any, Any]]): A parser that acts on function
arguments. eg. getopt.getopt
kwargsParser (Union[dict[Any, Any]]): A parser that acts on named params
- `sourcePath` *str* - Program source path
- `buildSpec` *types.BuildSpec* - Build spec
**kwargs (dict[Any, Any]): kwargs

#### Returns

- `types.FullBuildSpec` - buildSpec to be used by the application

#### Raises

- `RuntimeError` - Throw error if incorrect parser selected

#### Signature

```python
def createFromParser(
    selfParser: Any,
    argsParser: tuple[Any, ...],
    kwargsParser: dict[Any, Any],
    sourcePath: str,
    buildSpec: BuildSpec,
    **kwargs: dict[Any, Any]
) -> FullBuildSpec:
    ...
```

#### See also

- [BuildSpec](./types.md#buildspec)
- [FullBuildSpec](./types.md#fullbuildspec)