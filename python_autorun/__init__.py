import inspect
import os
import json
import sys
from typing import Callable, List
from python_autorun.gargs import get_all_args
from enum import Enum, auto


class SourceOptions(Enum):
    ENV = auto()
    JSON = auto()
    ARGS = auto()
    ALL = auto()


src = SourceOptions


def autorun(var_source: List[SourceOptions]=None, json_filename: str=None) -> Callable:
    """Automatically runs decorator labelled function and exits program with return code 
given to function's return statement. Arguments given during definition of function 
are used to select values of variables from source selected by 'var_source'.
    """
    
    def inner1(f):
        nonlocal var_source
        
        argl = list(inspect.signature(f).parameters)
        arg_values = list()
        mod_name = inspect.getmodule(f).__name__
        var_src_list = {}
        var_src_container = {}
        
        if var_source is None:
            var_source = [src.ENV]
        
        var_source.reverse()

        if var_source is not None:
            for vs in var_source:
                if vs == src.ENV: var_src_list[src.ENV] = os.environ
                elif vs == src.ARGS: var_src_list[src.ARGS] = get_all_args()
                elif vs == src.JSON: 
                    if json_filename is not None:
                        with open(json_filename, 'r') as fp:
                            var_src_list[src.JSON] = json.load(fp)     
                else:
                    raise ValueError("Invalid source {vs}")

        for _, source in var_src_list.items():
            for var_name, var_value in source.items():
                var_src_container[var_name] = var_value

        if mod_name != '__main__':
            return None

        for arg in argl:
            value = var_src_container.get(arg)
            arg_values.append(value)

        def inner2(*args):
            if var_source == src.ALL:
                r = f(**var_src_container)
            else:
                r = f(*args)

            if r is None:
                sys.exit(0)
            sys.exit(r)
            
        return inner2(*arg_values)
    return inner1




