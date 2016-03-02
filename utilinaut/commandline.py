import sys

def get_argument(switch_name, raise_exc=False):
    """
    Gets the command-line argument specified by switch_name. Assumes standard Unix-style command-line arguments, i.e.:
    python program.py -a a_value --long-switch=ls_value
    Returns None if the argument can't be found - set raise_exc=True to raise an AttributeError instead.
    """
    if switch_name[:2] == "--":     # assume it's a long switch
        for argument in sys.argv:
            if argument[:len(switch_name)] == switch_name:
                return argument[len(switch_name) + 1:]
        if raise_exc:
            raise AttributeError("Switch '{0}' is not in sys.argv.".format(switch_name))
        else:
            return None
    else:
        try:
            switch_index = sys.argv.index(switch_name)
        except ValueError:  # list.index raises VE if switch_name is not in list
            if raise_exc:
                raise AttributeError("Switch '{0}' is not in sys.argv.".format(switch_name))
            else:
                return None
        if len(sys.argv) > switch_index:
            return sys.argv[switch_index + 1]
        else:
            if raise_exc:
                raise AttributeError("Switch '{0}' is not in sys.argv.".format(switch_name))
            else:
                return None
