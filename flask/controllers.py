
from helpfulDecorators import json_attribs_check


@json_attribs_check
def buffer_values(jsonStr):
    print "in the buff"


    return












"""
    try:
        print jsonStr.keys()
        print jsonStr.values()
    except (AttributeError, ValueError):
        print "[-] IDk what that was, but it wasn't JSON."
        raise AttributeError

"""
