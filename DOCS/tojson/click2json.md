Module cli2gui.tojson.click2json
================================
Generate a dict describing optparse arguments

Functions
---------

    
`actionToJson(action: Any, widget: str) ‑> cli2gui.c2gtypes.Item`
:   Generate json for an action and set the widget - used by the application

    
`categorize(actions: list[Any]) ‑> Generator[c2gtypes.Item, None, None]`
:   Catergorise each action and generate json

    
`categorizeCommand(actions: list[Any]) ‑> Generator[c2gtypes.Item, None, None]`
:   Catergorise each action and generate json

    
`convert(parser: Any) ‑> cli2gui.c2gtypes.ParserRep`
:   Convert click to a dict
    
    Args:
            parser (click.core.Command): click parser
    
    Returns:
            c2gtypes.ParserRep: dictionary representing parser object

    
`extract(parser: Any) ‑> list[c2gtypes.Group]`
:   Get the actions as json for the parser