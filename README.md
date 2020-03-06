[![Github top language](https://img.shields.io/github/languages/top/FredHappyface/Python.Cli2Gui.svg?style=for-the-badge)](../../)
[![Codacy grade](https://img.shields.io/codacy/grade/[codacy-proj-id].svg?style=for-the-badge)](https://www.codacy.com/manual/FredHappyface/Python.Cli2Gui)
[![Repository size](https://img.shields.io/github/repo-size/FredHappyface/Python.Cli2Gui.svg?style=for-the-badge)](../../)
[![Issues](https://img.shields.io/github/issues/FredHappyface/Python.Cli2Gui.svg?style=for-the-badge)](../../issues)
[![License](https://img.shields.io/github/license/FredHappyface/Python.Cli2Gui.svg?style=for-the-badge)](/LICENSE.md)
[![Commit activity](https://img.shields.io/github/commit-activity/m/FredHappyface/Python.Cli2Gui.svg?style=for-the-badge)](../../commits/master)
[![Last commit](https://img.shields.io/github/last-commit/FredHappyface/Python.Cli2Gui.svg?style=for-the-badge)](../../commits/master)
[![PyPI](https://img.shields.io/pypi/dm/cli2gui.svg?style=for-the-badge)](https://pypi.org/project/cli2gui/)

# Python.Cli2Gui

<img src="readme-assets/icons/name.png" alt="Project Icon" width="750">

[desc]

```python
Cli2Gui(run_function, theme=None, darkTheme=None, sizes=None, image=None,
program_name=None, program_description=None, max_args_shown=5, **kwargs):
```
## Using
### run_function (required)
The name of the function to call func(args: argparse.Namespace())

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

### theme (optional)
Set a theme

```python
@Cli2Gui(theme=["#e7e7e9", "#dfdfe1", "#cacace", "#a0a1a7", "#696c77",
		"#383a42", "#202227", "#090a0b", "#ca1243", "#c18401", "#febb2a",
		"#50a14f", "#0184bc", "#4078f2", "#a626a4", "#986801", "#f0f0f1",
		"#fafafa", "#ec2258", "#f4a701", "#6db76c", "#01a7ef", "#709af5",
		"#d02fcd",])
```

### darkTheme (optional)
Set a dark theme variant

```python
@Cli2Gui(darkTheme=["#282c34", "#3f4451", "#4f5666", "#545862", "#9196a1",
		"#abb2bf", "#e6e6e6", "#ffffff", "#e06c75", "#d19a66", "#e5c07b",
		"#98c379", "#56b6c2", "#61afef", "#c678dd", "#be5046", "#21252b",
		"#181a1f", "#ff7b86", "#efb074", "#b1e18b", "#63d4e0", "#67cdff",
		"#e48bff",])
```

### sizes (optional)
Set the UI sizes

```python
@Cli2Gui(sizes={
			"title_size": 28,
			"label_size": (30, None),
			"input_size": (30, 1),
			"button":(10, 1),
			"padding":(5, 10),
			"helpText_size": 14,
			"text_size": 11
		})
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
maximum number of args shown before using a scrollbar

```python
@Cli2Gui(max_args_shown=5)
```

### Install With PIP

```python
pip install cli2gui
```

Head to https://pypi.org/project/cli2gui/ for more info


## Language information
### Built for
This program has been written for Python 3 and has been tested with
Python version 3.8.0 <https://www.python.org/downloads/release/python-380/>.

## Install Python on Windows
### Chocolatey
```powershell
choco install python
```
### Download
To install Python, go to <https://www.python.org/> and download the latest
version.

## Install Python on Linux
### Apt
```bash
sudo apt install python3.8
```

## How to run
### With VSCode
1. Open the .py file in vscode
2. Ensure a python 3.8 interpreter is selected (Ctrl+Shift+P > Python:Select
Interpreter > Python 3.8)
3. Run by pressing Ctrl+F5 (if you are prompted to install any modules, accept)
### From the Terminal
```bash
./[file].py
```

## Changelog
See the [CHANGELOG](/CHANGELOG.md) for more information.

## Download
### Clone
#### Using The Command Line
1. Press the Clone or download button in the top right
2. Copy the URL (link)
3. Open the command line and change directory to where you wish to
clone to
4. Type 'git clone' followed by URL in step 2
```bash
$ git clone https://github.com/FredHappyface/Python.Cli2Gui
```

More information can be found at
<https://help.github.com/en/articles/cloning-a-repository>

#### Using GitHub Desktop
1. Press the Clone or download button in the top right
2. Click open in desktop
3. Choose the path for where you want and click Clone

More information can be found at
<https://help.github.com/en/desktop/contributing-to-projects/cloning-a-repository-from-github-to-github-desktop>

### Download Zip File

1. Download this GitHub repository
2. Extract the zip archive
3. Copy/ move to the desired location

## Licence
MIT License
(See the [LICENSE](/LICENSE.md) for more information.)

## Screenshots

### Desktop
<div>
<img src="readme-assets/screenshots/desktop/screenshot-0.png" alt="Screenshot 1" width="600">
<img src="readme-assets/screenshots/desktop/screenshot-1.png" alt="Screenshot 2" width="600">
<img src="readme-assets/screenshots/desktop/screenshot-2.png" alt="Screenshot 3" width="600">
</div>

### Themes

|Light                                                                             |Dark                                                                              |Black                                                                             |
|:-:                                                                               |:-:                                                                               |:-:                                                                               |
|<img src="readme-assets/screenshots/themes/theme-1.png" alt="Theme 1" width="200">|<img src="readme-assets/screenshots/themes/theme-2.png" alt="Theme 2" width="200">|<img src="readme-assets/screenshots/themes/theme-3.png" alt="Theme 3" width="200">|
