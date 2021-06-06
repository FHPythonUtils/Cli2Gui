# pysimplegui2args

> Auto-generated documentation for [cli2gui.application.pysimplegui2args](../../../cli2gui/application/pysimplegui2args.py) module.

Functions to create args from pysimplegui values.

- [Cli2gui](../../README.md#cli2gui-index) / [Modules](../../README.md#cli2gui-modules) / [cli2gui](../index.md#cli2gui) / [application](index.md#application) / pysimplegui2args
    - [argFormat](#argformat)
    - [argparseFormat](#argparseformat)
    - [clickFormat](#clickformat)
    - [docoptFormat](#docoptformat)
    - [getoptFormat](#getoptformat)
    - [optparseFormat](#optparseformat)

## argFormat

[[find in source code]](../../../cli2gui/application/pysimplegui2args.py#L54)

```python
def argFormat(values: dict[(str, Any)], argumentParser: str) -> Any:
```

Format the args for the desired parser.

#### Arguments

values (dict[str, Any]): values from simple gui
- `argumentParser` *str* - argument parser to use

#### Returns

- `Any` - args

## argparseFormat

[[find in source code]](../../../cli2gui/application/pysimplegui2args.py#L9)

```python
def argparseFormat(values: dict[(str, Any)]) -> argparse.Namespace:
```

Format args for argparse.

## clickFormat

[[find in source code]](../../../cli2gui/application/pysimplegui2args.py#L45)

```python
def clickFormat(values: dict[(str, Any)]) -> list[Any]:
```

Format args for click.

## docoptFormat

[[find in source code]](../../../cli2gui/application/pysimplegui2args.py#L35)

```python
def docoptFormat(values: dict[(str, Any)]) -> dict[(str, Any)]:
```

Format args for docopt.

## getoptFormat

[[find in source code]](../../../cli2gui/application/pysimplegui2args.py#L30)

```python
def getoptFormat(values: dict[(str, Any)]) -> tuple[(list[Any], list[Any])]:
```

Format args for getopt.

## optparseFormat

[[find in source code]](../../../cli2gui/application/pysimplegui2args.py#L22)

```python
def optparseFormat(values: dict[(str, Any)]) -> dict[(str, Any)]:
```

Format args for optparse.
