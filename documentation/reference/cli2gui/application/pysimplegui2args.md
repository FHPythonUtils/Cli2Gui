# Pysimplegui2args

[Cli2gui Index](../../README.md#cli2gui-index) / [Cli2gui](../index.md#cli2gui) / [Application](./index.md#application) / Pysimplegui2args

> Auto-generated documentation for [cli2gui.application.pysimplegui2args](../../../../cli2gui/application/pysimplegui2args.py) module.

- [Pysimplegui2args](#pysimplegui2args)
  - [argFormat](#argformat)
  - [argparseFormat](#argparseformat)
  - [clickFormat](#clickformat)
  - [docoptFormat](#docoptformat)
  - [getoptFormat](#getoptformat)
  - [optparseFormat](#optparseformat)

## argFormat

[Show source in pysimplegui2args.py:59](../../../../cli2gui/application/pysimplegui2args.py#L59)

Format the args for the desired parser.

#### Arguments

----
 values (dict[str, Any]): values from simple gui
 - `argumentParser` *str* - argument parser to use

#### Returns

-------
 - `Any` - args

#### Signature

```python
def argFormat(values: dict[str, Any], argumentParser: str | ParserType) -> Any: ...
```



## argparseFormat

[Show source in pysimplegui2args.py:11](../../../../cli2gui/application/pysimplegui2args.py#L11)

Format args for argparse.

#### Signature

```python
def argparseFormat(values: dict[str, Any]) -> argparse.Namespace: ...
```



## clickFormat

[Show source in pysimplegui2args.py:49](../../../../cli2gui/application/pysimplegui2args.py#L49)

Format args for click.

#### Signature

```python
def clickFormat(values: dict[str, Any]) -> list[Any]: ...
```



## docoptFormat

[Show source in pysimplegui2args.py:39](../../../../cli2gui/application/pysimplegui2args.py#L39)

Format args for docopt.

#### Signature

```python
def docoptFormat(values: dict[str, Any]) -> dict[str, Any]: ...
```



## getoptFormat

[Show source in pysimplegui2args.py:34](../../../../cli2gui/application/pysimplegui2args.py#L34)

Format args for getopt.

#### Signature

```python
def getoptFormat(values: dict[str, Any]) -> tuple[list[Any], list[Any]]: ...
```



## optparseFormat

[Show source in pysimplegui2args.py:26](../../../../cli2gui/application/pysimplegui2args.py#L26)

Format args for optparse.

#### Signature

```python
def optparseFormat(values: dict[str, Any]) -> dict[str, Any]: ...
```