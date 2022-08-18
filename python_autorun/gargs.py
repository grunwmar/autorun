import sys
from typing import Any

def get_switch(switch: str) -> Any:
    """Returns value(s) of given switch, if switch not exists returns None"""

    argv = sys.argv

    if len(switch) == 1:
        dashed_arg = f"-{switch}"
    else:
        dashed_arg = f"--{switch}"
    for i, a in enumerate(argv):
        if a == dashed_arg:
            j = i + 1
            values = []
            if j < len(argv):
                next_arg = argv[j]
                for v in argv[j:]:
                    if v.startswith('-'):
                        if len(values) == 0:
                            return True
                        break
                    else:
                        values.append(v)
                if len(values) == 1:
                    return values[0]
                return values
            else:
                return True
                


def get_all_args() -> dict:
    """Returns dictionary of given switches in form of pairs switch: switch_value"""

    argv = sys.argv
    switches = []
    switches_stripped = []
    switches_values = {}

    for a in argv:
        if a.startswith("-"):
            switches.append(a)
    for s in switches:
        if s.startswith("-"):
            s = s[1:]
            if s.startswith("-"):
                s = s[1:]
                switches_stripped.append(s)
            else:
                switches_stripped.append(s)
    for s in switches_stripped:
        switches_values[s] = get_switch(s)
    return switches_values

    

