Module cli2gui.tojson.getopt2json
=================================
Generate a dict for getopt

Functions
---------

    
`actionToJson(action: str, widget: str, short: bool = True) ‑> cli2gui.c2gtypes.Item`
:   Convert an arg to json, behave in the same way as argparse hence the large
    amount of duplication

    
`catLong(actions: list[str])`
:   categorize long args

    
`catShort(actions: list[str])`
:   categorize short args

    
`convert(parser: tuple[list[str], list[str]]) ‑> c2gtypes.ParserRep`
:   Convert getopt to a dict
    
    Args:
            parser (tuple[list[str], list[str]]): getopt parser
    
    Returns:
            c2gtypes.ParserRep: dictionary representing parser object

    
`process(group: list[str], groupName: str, categorize: Callable[[list[str]], Generator[c2gtypes.Item, None, None]]) ‑> list[c2gtypes.Group]`
:   Generate a group (or section)