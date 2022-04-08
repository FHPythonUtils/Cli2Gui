#! /bin/sh

i=https://github.com/PySimpleGUI/PySimpleGUI/raw/master/PySimpleGUI.py
o=cli2gui/application/PySimpleGUI.py

curl -L -o "$o" "$i"

echo "done $o"
