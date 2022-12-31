# Changelog

All major and minor version changes will be documented in this file. Details of
patch-level version changes can be found in [commit messages](../../commits/master).

## 2022.3 - 2022/12/31

- Feature, support defaults https://github.com/FHPythonUtils/Cli2Gui/issues/11
- Use full module namespace in-place of relative imports
- Use `Enum` for widget types. eg. `types.ItemType.Bool`
- Update internal types
- Add more supported types for other parsers. e.g `click`
	- Argparse supports: Bool, Int, Choice, File, Text
	- Click supports: Bool, Int, Choice, Text
	- DocOpt supports: Bool, Text
	- GetOpt supports: Bool, Text
	- Optparse supports: Bool, Int, Choice, Text

## 2022.2.1 - 2022/12/30

- Fix https://github.com/FHPythonUtils/Cli2Gui/issues/13

## 2022.2 - 2022/09/02

- Fix https://github.com/FHPythonUtils/Cli2Gui/issues/10, basic support for subparsers. `parser.add_subparsers()`

	```py
	parser = argparse.ArgumentParser(description="this is an example parser")
	subparsers = parser.add_subparsers(help='types of A')
	parser.add_argument("-v",)

	a_parser = subparsers.add_parser("A")
	b_parser = subparsers.add_parser("B")

	a_parser.add_argument("something", choices=['a1', 'a2'])

	args = parser.parse_args()
	```

## 2022.1 - 2022/04/07

- Fix https://github.com/FHPythonUtils/Cli2Gui/issues/7
- `catpandoc` is now optional https://github.com/FHPythonUtils/Cli2Gui/issues/5

## 2022 - 2022/01/24

- Bump pillow version (CVE-2022-22815, CVE-2022-22816, CVE-2022-22817)
- Update deps

## 2021.2.1 - 2021/10/14

- Use pre-commit to enforce reasonable standards + consistency
- Update readme with improved docs on installing and running python (fairly generic)
- Remove classifiers for license + python versions and rely on poetry to generate these
- Update tooling config (pyproject.toml)

## 2021.2 - 2021/07/24

- Use enum for parser + gui
- Use datatypes + typeddict...
- Add option for end user to select parser at runtime https://github.com/FHPythonUtils/Cli2Gui/issues/4
- Replace 'if' case/switch with function mappings

## 2021.1 - 2021/06/06

- reformat
- improve documentation
- typing improvements
- use relative imports
- update pyproject.toml

## 2021 - 2021/01/18

- Modelled the radio groups

## 2020.9.1 - 2020/10/14

- New Pillow release
- Typing fixes as recommended here https://github.com/microsoft/pylance-release/issues/485

## 2020.9 - 2020/10/13

- Added typing (drop py < 3.7)
- Update docstrings
- Update internal representation (tidy up)
- Use flavours for additional pysimplegui modules install `cli2gui[web]` and
  `cli2gui[qt]` for the respective versions
- Modernize parts of the codebase (eg. decorators.py)
- Use camelCase for variables

## 2020.8.1 - 2020/05/06

- Updated classifiers

## 2020.8 - 2020/04/27

- Added dephell_argparse support

## 2020.7.1 - 2020/04/24

- Added catch for ResourceWarning when running in `python -Wd`

## 2020.7 - 2020/04/16

- using poetry and dephell build systems

## 2020.6 - 2020/03/24

- added rudimentary click support

## 2020.5 - 2020/03/22

- added menu
- included part of catpandoc to achieve this (excluding catimage as this leads
to a circular import 😱)
- updated documentation to reflect this
- updated requirements.txt

## 2020.4

- bump

## 2020.3 - 2020/03/17

- can use pysimplegui, pysimpleguiqt, pysimpleguiweb
- updated readme and added data structures documentation
- bugfixes
- lint fixes

## 2020.3 - 2020/03/12

- added docopt parser
- base24 scheme can be used as theme
- Updated run_function. If not specified, program continues as normal
(can only run once)

## 2020.2 - 2020/03/12

- Fix

## 2020.1 - 2020/03/12

- Updated readme
- added images
- added getopt parser
- added optparse parser
- Program icon is to left of title
- Streamlined argparse2json
- refactor

## 2020 - 2020/03/06

- First release
