# decorators

> Auto-generated documentation for [cli2gui.decorators](../../cli2gui/decorators.py) module.

Decorator and entry point for the program

- [Cli2gui](../README.md#cli2gui-index) / [Modules](../README.md#cli2gui-modules) / [cli2gui](index.md#cli2gui) / decorators
    - [Cli2Gui](#cli2gui)
    - [Click2Gui](#click2gui)
    - [createFromParser](#createfromparser)
    - [quote](#quote)
    - [quote](#quote)

## Cli2Gui

[[find in source code]](../../cli2gui/decorators.py#L142)

```python
def Cli2Gui(
    run_function: Union[(Callable[(..., Any)], None)],
    auto_enable: bool = False,
    parser: str = 'argparse',
    gui: str = 'pysimplegui',
    theme: Union[(str, list[str], None)] = None,
    darkTheme: Union[(str, list[str], None)] = None,
    sizes: Union[(dict[(str, int)], None)] = None,
    image: Union[(str, None)] = None,
    program_name: Union[(str, None)] = None,
    program_description: Union[(str, None)] = None,
    max_args_shown: int = 5,
    menu: Union[(dict[(str, Any)], None)] = None,
    **kwargs: dict[(str, Any)],
) -> Any:
```

Decorator to use in the function that contains the argument parser
Serialises data to JSON and launches the Cli2Gui application

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
theme (Union[str, list[str], None], optional): Set a base24 theme. Can
also pass a base24 scheme file. eg. one-light.yaml. Defaults to None.
darkTheme (Union[str, list[str], None], optional): Set a base24 dark
theme variant. Can also pass a base24 scheme file. eg. one-dark.yaml.
Defaults to None.
sizes (Union[dict[str, int], None], optional): Set the UI sizes such as
the button size. Defaults to None.
- `image` *(image* - Union[str, None], optional): Set the program icon. File
extensions can be any that PIL supports. Defaults to None.
program_name (Union[str, None], optional): Override the program name.
Defaults to None.
program_description (Union[str, None], optional): Override the program
description. Defaults to None.
- `max_args_shown` *int, optional* - Maximum number of args shown before
using a scrollbar. Defaults to 5.
menu (Union[dict[str, Any], None], optional): Add a menu to the program.
Defaults to None. eg. THIS_DIR = str(Path(__file__).resolve().parent)
- `menu={"File"` - THIS_DIR + "/file.md"}
**kwargs (dict[Any, Any]): kwargs

#### Returns

- `Any` - Runs the application

## Click2Gui

[[find in source code]](../../cli2gui/decorators.py#L85)

```python
def Click2Gui(
    run_function: Callable[(..., Any)],
    gui: str = 'pysimplegui',
    theme: Union[(str, list[str], None)] = None,
    darkTheme: Union[(str, list[str], None)] = None,
    sizes: Union[(dict[(str, int)], None)] = None,
    image: Union[(str, None)] = None,
    program_name: Union[(str, None)] = None,
    program_description: Union[(str, None)] = None,
    max_args_shown: int = 5,
    menu: Union[(dict[(str, Any)], None)] = None,
    **kwargs: dict[(str, Any)],
) -> Any:
```

Decorator to use in the function that contains the argument parser
Serialises data to JSON and launches the Cli2Gui application

#### Arguments

run_function (Callable[..., Any]): The name of the function to call eg.
- `gui` *str, optional* - Override the gui to use. Current options are:
"pysimplegui", "pysimpleguiqt","pysimpleguiweb". Defaults to
"pysimplegui".
theme (Union[str, list[str], None], optional): Set a base24 theme. Can
also pass a base24 scheme file. eg. one-light.yaml. Defaults to None.
darkTheme (Union[str, list[str], None], optional): Set a base24 dark
theme variant. Can also pass a base24 scheme file. eg. one-dark.yaml.
Defaults to None.
sizes (Union[dict[str, int], None], optional): Set the UI sizes such as
the button size. Defaults to None.
- `image` *(image* - Union[str, None], optional): Set the program icon. File
extensions can be any that PIL supports. Defaults to None.
program_name (Union[str, None], optional): Override the program name.
Defaults to None.
program_description (Union[str, None], optional): Override the program
description. Defaults to None.
- `max_args_shown` *int, optional* - Maximum number of args shown before
using a scrollbar. Defaults to 5.
menu (Union[dict[str, Any], None], optional): Add a menu to the program.
Defaults to None. eg. THIS_DIR = str(Path(__file__).resolve().parent)
- `menu={"File"` - THIS_DIR + "/file.md"}
**kwargs (dict[Any, Any]): kwargs

#### Returns

- `Any` - Runs the application

## createFromParser

[[find in source code]](../../cli2gui/decorators.py#L44)

```python
def createFromParser(
    selfParser: Union[(object, None)],
    argsParser: Union[(tuple[(Any, Any)], None)],
    kwargsParser: Union[(dict[(Any, Any)], None)],
    sourcePath: str,
    buildSpec: c2gtypes.BuildSpec,
    **kwargs: dict[(Any, Any)],
) -> c2gtypes.FullBuildSpec:
```

Generate a buildSpec from a parser

#### Arguments

selfParser (Union[object, None]): A parser that acts on self. eg. ArgumentParser.parse_args
argsParser (Union[tuple[Any, Any], None]): A parser that acts on function arguments. eg. getopt.getopt
kwargsParser (Union[dict[Any, Any], None]): A parser that acts on named params
- `sourcePath` *str* - Program source path
- `buildSpec` *c2gtypes.BuildSpec* - Build spec
**kwargs (dict[Any, Any]): kwargs

#### Returns

- `c2gtypes.FullBuildSpec` - buildSpec to be used by the application

## quote

[[find in source code]](../../cli2gui/decorators.py#L35)

```python
def quote(value: str):
```

quote

## quote

[[find in source code]](../../cli2gui/decorators.py#L39)

```python
def quote(value: str):
```

quote
