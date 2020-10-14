Module cli2gui.application.pysimplegui2args
===========================================
Functions to create args from pysimplegui values

Functions
---------

    
`argFormat(values: dict[str, Any], argumentParser: str) ‑> Any`
:   Format the args for the desired parser
    
    Args:
            values (dict[str, Any]): values from simple gui
            argument_parser (str): argument parser to use
    
    Returns:
            Any: args

    
`argparseFormat(values: dict[str, Any]) ‑> argparse.Namespace`
:   Format args for argparse

    
`clickFormat(values: dict[str, Any]) ‑> list`
:   Format args for click

    
`docoptFormat(values: dict[str, Any]) ‑> dict`
:   Format args for docopt

    
`getoptFormat(values: dict[str, Any]) ‑> tuple`
:   Format args for getopt

    
`optparseFormat(values: dict[str, Any]) ‑> dict`
:   Format args for optparse