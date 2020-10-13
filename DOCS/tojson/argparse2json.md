Module cli2gui.tojson.argparse2json
===================================
Generate a dict describing argparse arguments

pylint and pylance both want me to not access protected methods - I know better ;)

Functions
---------

    
`actionToJson(action: argparse.Action, widget: str) ‑> cli2gui.c2gtypes.Item`
:   Generate json for an action and set the widget - used by the application

    
`buildRadioGroup(mutexGroup: _MutuallyExclusiveGroup)`
:   Create a radio group for a mutex group of arguments

    
`categorizeGroups(groups: list[ArgparseGroup]) ‑> list[c2gtypes.Group]`
:   Categorize the parser groups and arg_items

    
`catergorizeItems(actions: list[argparse.Action]) ‑> Generator[c2gtypes.Item, None, None]`
:   Catergorise each action and generate json

    
`chooseName(name: str, subparser: argparse.ArgumentParser) ‑> str`
:   Get the program name

    
`containsActions(actionA: list[argparse.Action], actionB: list[argparse.Action])`
:   check if any actions(a) are present in actions(b)

    
`convert(parser: argparse.ArgumentParser) ‑> cli2gui.c2gtypes.ParserRep`
:   Convert argparse to a dict
    
    Args:
            parser (argparse.ArgumentParser): argparse parser
    
    Returns:
            c2gtypes.ParserRep: dictionary representing parser object

    
`extractRawGroups(actionGroup: argparse._ArgumentGroup) ‑> cli2gui.tojson.argparse2json.ArgparseGroup`
:   Recursively extract argument groups and associated actions
    from ParserGroup objects

    
`isDefaultProgname(name: str, subparser: argparse.ArgumentParser) ‑> bool`
:   Identify if the passed name is the default program name

    
`iterParsers(parser: argparse.ArgumentParser) ‑> list[tuple[str, argparse.ArgumentParser]]`
:   Iterate over name, parser pairs

    
`process(parser: argparse.ArgumentParser) ‑> list[c2gtypes.Group]`
:   Reapply the mutex groups and then categorize them and the arg_items under
    the parser

    
`reapplyMutexGroups(mutexGroups: list[argparse._MutuallyExclusiveGroup], actionGroups: list[Any])`
:   argparse stores mutually exclusive groups independently
    of all other groups. So, they must be manually re-combined
    with the groups/subgroups to which they were originally declared
    in order to have them appear in the correct location in the UI.
    
    Order is attempted to be preserved by inserting the MutexGroup
    into the _actions list at the first occurrence of any item
    where the two groups intersect

    
`stripEmpty(groups: list[ArgparseGroup])`
:   Remove groups where group['arg_items'] is false

Classes
-------

`ArgparseGroup(*args, **kwargs)`
:   dict() -> new empty dictionary
    dict(mapping) -> new dictionary initialized from a mapping object's
        (key, value) pairs
    dict(iterable) -> new dictionary initialized as if via:
        d = {}
        for k, v in iterable:
            d[k] = v
    dict(**kwargs) -> new dictionary initialized with the name=value pairs
        in the keyword argument list.  For example:  dict(one=1, two=2)

    ### Ancestors (in MRO)

    * builtins.dict

    ### Class variables

    `arg_items: list[argparse.Action]`
    :

    `groups: Union[list[ArgparseGroup], list[Any]]`
    :

    `name: str`
    :