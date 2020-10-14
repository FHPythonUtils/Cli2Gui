Module cli2gui.c2gtypes
=======================
Types for cli2gui

Classes
-------

`BuildSpec(*args, **kwargs)`
:   representation for the BuildSpec

    ### Ancestors (in MRO)

    * builtins.dict

    ### Class variables

    `darkTheme: Union[str, list, NoneType]`
    :

    `gui: str`
    :

    `image: Optional[str]`
    :

    `max_args_shown: int`
    :

    `menu: Optional[dict]`
    :

    `parser: str`
    :

    `program_description: Optional[str]`
    :

    `program_name: Optional[str]`
    :

    `run_function: Optional[collections.abc.Callable]`
    :

    `sizes: Optional[dict]`
    :

    `theme: Union[str, list, NoneType]`
    :

`FullBuildSpec(*args, **kwargs)`
:   representation for the FullBuildSpec (BuildSpec + ParserRep)

    ### Ancestors (in MRO)

    * builtins.dict

    ### Class variables

    `darkTheme: Union[str, list[str], None]`
    :

    `gui: str`
    :

    `image: Union[str, None]`
    :

    `max_args_shown: int`
    :

    `menu: Union[dict[str, Any], None]`
    :

    `parser: str`
    :

    `parser_description: str`
    :

    `program_description: Union[str, None]`
    :

    `program_name: Union[str, None]`
    :

    `run_function: Union[Callable[..., Any], None]`
    :

    `sizes: Union[dict[str, Any], None]`
    :

    `theme: Union[str, list[str], None]`
    :

    `widgets: list[Widgets]`
    :

`Group(*args, **kwargs)`
:   representation for an argument group

    ### Ancestors (in MRO)

    * builtins.dict

    ### Class variables

    `arg_items: list`
    :

    `groups: Union[list, list]`
    :

    `name: str`
    :

`Item(*args, **kwargs)`
:   representation for an arg_item

    ### Ancestors (in MRO)

    * builtins.dict

    ### Class variables

    `choices: Union[list, list]`
    :

    `commands: list`
    :

    `dest: str`
    :

    `display_name: str`
    :

    `help: str`
    :

    `type: str`
    :

`ParserRep(*args, **kwargs)`
:   representation for a parser

    ### Ancestors (in MRO)

    * builtins.dict

    ### Class variables

    `parser_description: Optional[str]`
    :

    `widgets: list`
    :