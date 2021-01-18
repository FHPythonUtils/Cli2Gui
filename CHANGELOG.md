# Changelog
All major and minor version changes will be documented in this file. Details of
patch-level version changes can be found in [commit messages](../../commits/master).


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
