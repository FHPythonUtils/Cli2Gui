# Comparison to similar projects

Do let me know if any of these are incorrect. Some of the comparisons are
based off documentation/ the readme

## Parser Support

| Parser                                                          | Cli2Gui             | [Gooey](https://github.com/chriskiehl/Gooey) | Quick |
| --------------------------------------------------------------- | ------------------- | -------------------------------------------- | ----- |
| [Argparse](https://docs.python.org/3/library/argparse.html)     | ✔                   | ✔                                            | ❌     |
| [Optparse](https://docs.python.org/3/library/optparse.html)     | ✔                   | ❌                                            | ❌     |
| [DocOpt](https://github.com/docopt/docopt)                      | ✔                   | ❌                                            | ❌     |
| [Click](https://github.com/pallets/click)                       | ✔                 * | ❌                                            | ✔     |
| [GetOpt](https://docs.python.org/3/library/getopt.html)         | ✔                   | ❌                                            | ❌     |
| [Dephell Argparse](https://github.com/dephell/dephell_argparse) | ✔                   | ❌                                            | ❌     |

```none
* Partial support (use [Click2Gui](#click2gui))

This works for simpler programs but sadly falls flat for more complex programs
```

## GUI Toolkit Support

| GUI Toolkits | Cli2Gui | Gooey | Quick |
| ------------ | ------- | ----- | ----- |
| Tkinter      | ✔       | ❌     | ❌     |
| WxWidgets    | ❌       | ✔     | ❌     |
| Qt           | ✔       | ❌     | ✔     |
| Gtk          | ❌       | ❌     | ❌     |
| Web          | ✔       | ❌     | ❌     |

## GUI Feature Support

| Basic GUI                  | Cli2Gui | Gooey            | Quick            |
| -------------------------- | ------- | ---------------- | ---------------- |
| Override name/ description | ✔       | ✔                | ❌                |
| Theming                    | ✔       | ⚠        Limited | ⚠        Limited |
| DarkMode                   | ✔       | ❌                | ✔                |
| Window Size                | ✔       | ✔                | ❌                |
| Element Size               | ✔       | ❌                | ❌                |
| Custom Images              | ✔       | ✔                | ❌                |

Cli2Gui is pretty lacking in these features and will probably remain that way
to ease maintainability - the primary aim is to support multiple argparse
libraries over fancy widgets

| Advanced GUI           | Cli2Gui | Gooey | Quick |
| ---------------------- | ------- | ----- | ----- |
| Dropdown               | ✔       | ✔     | ✔     |
| Slider                 | ❌       | ✔     | ✔     |
| Tabs                   | ❌       | ✔     | ✔     |
| Menus                  | ✔       | ✔     | ❌     |
| Max Args before Scroll | ✔       | ❌     | ❌     |
