# Pysimplegui2args

> Auto-generated documentation for [cli2gui.application.pysimplegui2args](../../../../cli2gui/application/pysimplegui2args.py) module.

Functions to create args from pysimplegui values.

- [Cli2gui](../../README.md#cli2gui-index) / [Modules](../../MODULES.md#cli2gui-modules) / [Cli2gui](../index.md#cli2gui) / [Application](index.md#application) / Pysimplegui2args
    - [argFormat](#argformat)
    - [argparseFormat](#argparseformat)
    - [clickFormat](#clickformat)
    - [docoptFormat](#docoptformat)
    - [getoptFormat](#getoptformat)
    - [optparseFormat](#optparseformat)

## argFormat

[[find in source code]](../../../../cli2gui/application/pysimplegui2args.py#L60)

```python
def argFormat(
    values: dict[str, Any],
    argumentParser: str | ParserType,
) -> Any:
```

Format the args for the desired parser.

#### Arguments

values (dict[str, Any]): values from simple gui
- `argumentParser` *str* - argument parser to use

#### Returns

- `Any` - args

## argparseFormat

[[find in source code]](../../../../cli2gui/application/pysimplegui2args.py#L11)

```python
def argparseFormat(values: dict[str, Any]) -> argparse.Namespace:
```

Format args for argparse.

## clickFormat

[[find in source code]](../../../../cli2gui/application/pysimplegui2args.py#L51)

```python
def clickFormat(values: dict[str, Any]) -> list[Any]:
```

Format args for click.

## docoptFormat

[[find in source code]](../../../../cli2gui/application/pysimplegui2args.py#L41)

```python
def docoptFormat(values: dict[str, Any]) -> dict[str, Any]:
```

Format args for docopt.

## getoptFormat

[[find in source code]](../../../../cli2gui/application/pysimplegui2args.py#L36)

```python
def getoptFormat(values: dict[str, Any]) -> tuple[list[Any], list[Any]]:
```

Format args for getopt.

## optparseFormat

[[find in source code]](../../../../cli2gui/application/pysimplegui2args.py#L28)

```python
def optparseFormat(values: dict[str, Any]) -> dict[str, Any]:
```

Format args for optparse.
