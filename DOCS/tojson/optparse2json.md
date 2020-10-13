Module cli2gui.tojson.optparse2json
===================================
Generate a dict describing optparse arguments

pylint and pylance both want me to not access protected methods - I know better ;)

Functions
---------

    
`actionToJson(action: optparse.Option, widget: str) ‑> cli2gui.c2gtypes.Item`
:   Generate json for an action and set the widget - used by the application

    
`categorize(actions: list[optparse.Option])`
:   Catergorise each action and generate json

    
`convert(parser: optparse.OptionParser) ‑> cli2gui.c2gtypes.ParserRep`
:   Convert argparse to a dict
    
    Args:
            parser (optparse.OptionParser): optparse parser
    
    Returns:
            c2gtypes.ParserRep: dictionary representing parser object

    
`extractGroups(parser: optparse.OptionParser) ‑> cli2gui.c2gtypes.Group`
:   Get the actions as json for each item and group under the parser

    
`extractOptions(optionGroup: optparse.OptionParser) ‑> cli2gui.c2gtypes.Group`
:   Get the actions as json for each item under a group