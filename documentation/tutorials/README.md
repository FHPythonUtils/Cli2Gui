
<!-- omit in toc -->
# Tutorial: How to Use `Cli2Gui` in Your Project

`Cli2Gui` is a Python package that allows you to transform command-line interface (CLI) applications
into graphical user interfaces (GUIs). It supports popular parsers like `argparse`, and different
GUI libraries, like `freesimplegui`. In this tutorial, we will walk through how to integrate
`Cli2Gui` into your Python project.

- [Setup](#setup)
- [Basic Usage](#basic-usage)
	- [Basic CLI Application](#basic-cli-application)
	- [Adding `Cli2Gui`](#adding-cli2gui)
- [Advanced Example with Argument Groups](#advanced-example-with-argument-groups)
- [Customizing the GUI](#customizing-the-gui)

## Setup

For the examples below, install the `Cli2Gui` package by running:

```bash
pip install cli2gui[fsg]
```

Note: If you need the functionality provided by these libraries, use the following extras:

- **psg**: For PySimpleGUI support, adding easy-to-build, functional GUIs.
- **fsg**: For FreeSimpleGUI, a lightweight, streamlined GUI option.
- **web**: To run your app in a web browser via PySimpleGUIWeb.
- **qt**: For PySimpleGUIQt, creating polished, native desktop GUIs.
- **pandoc**: To pretty print markdown files and similar

## Basic Usage

The primary way to use `Cli2Gui` is through a decorator that you add to your main function. The
decorator transforms your CLI into a GUI when necessary.

Here's a simple example of how to integrate `Cli2Gui` into a basic program:

### Basic CLI Application

```python
import argparse

def run(args):
    print(args.arg)

def main():
    parser = argparse.ArgumentParser(description="Example parser")
    parser.add_argument("arg", type=str, help="Positional argument")
    args = parser.parse_args()
    run(args)

if __name__ == "__main__":
    main()
```

In this basic example, we have a CLI app that takes a positional argument. Next, we will enhance
it with `Cli2Gui` to provide a GUI option.

### Adding `Cli2Gui`

We'll now decorate the `main` function with `Cli2Gui`:

```python
from cli2gui import Cli2Gui

# Define the function that will handle the program's logic
def run(args):
    print(args.arg)

# Use Cli2Gui as a decorator to convert CLI into a GUI, using freesimplegui
@Cli2Gui(run_function=run, gui="freesimplegui")
def main():
    parser = argparse.ArgumentParser(description="Example parser with GUI support")
    parser.add_argument("arg", type=str, help="Positional argument")
    args = parser.parse_args()
    run(args)

if __name__ == "__main__":
    main()
```

The `Cli2Gui` decorator wraps around the `main` function and adds support for both CLI and GUI.
You can now run this program in two ways:

- **CLI Mode**: `python3 main.py`
- **GUI Mode**: run `python3 main.py --cli2gui` and the GUI will appear, allowing you to enter
	the arguments interactively.

## Advanced Example with Argument Groups

Let’s expand on the previous example with a more complex argument structure, including mutually
exclusive groups, optional arguments, and file inputs. We will also demonstrate how to add a
menu to the GUI.

```python
from cli2gui import Cli2Gui
import argparse
from pathlib import Path

# Define the function that will handle the program's logic
def handle(args):
    print(args)

# Define the CLI function with advanced arguments
@Cli2Gui(
    run_function=handle,
    gui="freesimplegui",
    menu={
        "File": "path/to/file.md",
        "Another File": "path/to/another_file.md",
    }
)
def cli():
    parser = argparse.ArgumentParser(description="Advanced CLI with GUI support")

    # Positional arguments
    parser.add_argument("positional", help="Positional argument")
    parser.add_argument("positional_file", type=argparse.FileType("r"), help="Positional file input")

    # Optional arguments
    parser.add_argument("--optional", help="Optional argument")
    parser.add_argument("--store-true", action="store_true", help="Store true")
    parser.add_argument("--store-false", action="store_false", help="Store false")
    parser.add_argument("--store", help="Store value")
    parser.add_argument("--count", action="count", help="Count occurrences")
    parser.add_argument("--choices", choices=["choice1", "choice2"], help="Pick a choice")
    parser.add_argument("--somefile", type=argparse.FileType("r"), help="Optional file input")

    # Mutually exclusive group
    group = parser.add_argument_group("Image options")
    mxg = group.add_mutually_exclusive_group()
    mxg.add_argument("--mxg-true", action="store_true", help="Mutually exclusive store true")
    mxg.add_argument("--mxg-false", action="store_false", help="Mutually exclusive store false")
    mxg.add_argument("--mxg", help="Mutually exclusive store")
    mxg.add_argument("--mxg-count", action="count", help="Mutually exclusive count")
    mxg.add_argument("--mxg-choices", choices=["choice1", "choice2"], help="Mutually exclusive choice")

    args = parser.parse_args()
    handle(args)

if __name__ == "__main__":
    cli()
```

In this example:

- **run_function**: The function to be executed when the user clicks the "Run" button in the GUI. This is the `handle()` function
- **gui**: Specify the GUI framework to use. Supported options are: `"dearpygui"`, `"pysimplegui"`, `"pysimpleguiqt"`, `"pysimpleguiweb"`, `"freesimplegui"`. Defaults to `"dearpygui"`. In the example, this is `"freesimplegui"`.
- **menu**: Add a custom menu to the GUI. Example: `{"File": "/path/to/file.md"}`.

## Customizing the GUI

You can customize various aspects of the GUI, including the theme, icon, and program name. Here’s
how you can apply some customization options:

```python
@Cli2Gui(
    run_function=handle,
    gui="freesimplegui",
    theme="one-light.yaml",
    darkTheme="one-dark.yaml",
    image="path/to/icon.png",
    program_name="My Custom Program",
    program_description="This is a custom description"
)
def cli():
    # Argument parsing logic here
    pass
```

In this example:

- **run_function**: The function to be executed when the user clicks the "Run" button in the GUI. This is the `handle()` function
- **gui**: Specify the GUI framework to use. Supported options are: `"dearpygui"`, `"pysimplegui"`, `"pysimpleguiqt"`, `"pysimpleguiweb"`, `"freesimplegui"`. Defaults to `"dearpygui"`. In the example, this is `"freesimplegui"`.
- **theme**: Set a base24 theme or provide a base24 scheme file (e.g., `"one-light.yaml"`).
- **darkTheme**: Specify a dark theme variant using a base24 scheme or file (e.g., `"one-dark.yaml"`).
- **image**: Define the program icon. Supported formats are those compatible with the Python Imaging Library (PIL).
- **program_name**: Override the default program name with a custom name.
- **program_description**: Provide a custom description for the program.
- **menu**: Add a custom menu to the GUI. Example: `{"File": "/path/to/file.md"}`.
