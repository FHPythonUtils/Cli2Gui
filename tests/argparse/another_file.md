## Decorator

```python
@Cli2Gui(run_function, auto_enable=False, parser="argparse", gui="pysimplegui",
		theme="", darkTheme="", image="", program_name="",
		program_description="", max_args_shown=5, **kwargs)
```

## Using the decorator in your project

### run_function (optional)

The name of the function to call eg. main(args). Defaults to None. If not
specified, program continues as normal (can only run once)

```python
def main(args):
	print(args.arg)

@Cli2Gui(run_function=main)
def cli():
	parser = argparse.ArgumentParser(description="this is an example parser")
	parser.add_argument("arg", type=str,
		help="positional arg")
	args = parser.parse_args()
	main(args)
```

### auto_enable (optional)

Enable the GUI by default. If enabled by default requires `--disable-cli2gui`, otherwise requires `--cli2gui`

```python
@Cli2Gui(auto_enable=False)
```

### parser (optional)

Override the parser to use, defaults to argparse. Current options are:
"argparse", "getopt", "optparse", "docopt", "dephell_argparse"

```python
@Cli2Gui(parser="argparse")
```

### gui (optional)

Override the gui to use. Current options are:
"pysimplegui", "pysimpleguiqt","pysimpleguiweb". Defaults to "pysimplegui".

pysimplegui is the recommended option

```python
@Cli2Gui(gui="pysimplegui")
```

### theme (optional)

Set a base24 theme. Can also pass a base24 scheme file. eg. `one-light.yaml`

```python
@Cli2Gui(theme=["#e7e7e9", "#dfdfe1", "#cacace", "#a0a1a7", "#696c77",
		"#383a42", "#202227", "#090a0b", "#ca1243", "#c18401", "#febb2a",
		"#50a14f", "#0184bc", "#4078f2", "#a626a4", "#986801", "#f0f0f1",
		"#fafafa", "#ec2258", "#f4a701", "#6db76c", "#01a7ef", "#709af5",
		"#d02fcd"])
```

### darkTheme (optional)

Set a base24 dark theme variant. Can also pass a base24 scheme file. eg.
`one-dark.yaml`

```python
@Cli2Gui(darkTheme=["#282c34", "#3f4451", "#4f5666", "#545862", "#9196a1",
		"#abb2bf", "#e6e6e6", "#ffffff", "#e06c75", "#d19a66", "#e5c07b",
		"#98c379", "#56b6c2", "#61afef", "#c678dd", "#be5046", "#21252b",
		"#181a1f", "#ff7b86", "#efb074", "#b1e18b", "#63d4e0", "#67cdff",
		"#e48bff"])
```

### image (optional)

Set the program icon. File extensions can be any that PIL supports

```python
@Cli2Gui(image="path/to/image.png")
```

### program_name (optional)

Override the program name

```python
@Cli2Gui(program_name="custom name")
```

### program_description (optional)

Override the program description

```python
@Cli2Gui(program_description="this is a custom description")
```

### max_args_shown (optional)

Maximum number of args shown before using a scrollbar

```python
@Cli2Gui(max_args_shown=5)
```

### menu (optional)

Add a menu to the program. Defaults to None. eg.

```python
THIS_DIR = str(Path(__file__).resolve().parent)
menu={"File": THIS_DIR + "/file.md"}
```

Works significantly better with pysimplegui than pysimpleguiqt

```python
@Cli2Gui(menu={"File": THIS_DIR + "/file.md", "Another File": THIS_DIR + "/another_file.md", })
```

## Click

```python
def Click2Gui(run_function, gui="pysimplegui", theme="", darkTheme="",
		image="", program_name="", program_description="",
		max_args_shown=5, menu="", **kwargs):
```

Very similar to the decorator but with the following differences...

### run_function (required)

Specify the click function to use. (attempts were made to offer full program
support however this behaved very poorly)

### parser (not applicable)

As this is exclusively for click, this option is not present
