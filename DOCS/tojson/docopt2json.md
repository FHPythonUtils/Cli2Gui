Module cli2gui.tojson.docopt2json
=================================
Generate a dict for docopt

Functions
---------

    
`actionToJson(action: tuple[str, str, str, Any, str], widget: str, isPos: bool) ‑> c2gtypes.Item`
:   Generate json for an action and set the widget - used by the application

    
`categorize(actions: list[tuple[str, str, str, Any, str]], isPos: bool = False) ‑> Iterator[c2gtypes.Item]`
:   Catergorise each action and generate json

    
`convert(parser: Any) ‑> cli2gui.c2gtypes.ParserRep`
:   Convert getopt to a dict
    
    Args:
            parser (Any): docopt parser
    
    Returns:
            c2gtypes.ParserRep: dictionary representing parser object

    
`extract(parser: Any) ‑> list[c2gtypes.Group]`
:   Get the actions as json for the parser

    
`parse(optionDescription: str) ‑> tuple[str, str, str, Any, str]`
:   Parse an option help text, adapted from docopt

    
`parseOpt(doc: Any) ‑> list[tuple[str, str, str, Any, str]]`
:   Parse an option help text, adapted from docopt

    
`parsePos(doc: Any) ‑> list[tuple[str, str, str, Any, str]]`
:   Parse positional arguments from docstring

    
`parseSection(name: str, source: Any) ‑> list[str]`
:   Taken from docopt