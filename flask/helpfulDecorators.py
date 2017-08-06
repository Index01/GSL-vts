

from functools import wraps


def json_attribs_check(func):
    """
        Decorator for validating json, a thing we might do often. 
    """
    @wraps(func)
    def inner_func(jsonStr):
        print "jsonstr: %s" % jsonStr()

        try:
            print jsonStr.keys()
            print jsonStr.values()
            
        except (AttributeError, ValueError):
            print "[-] IDk what that was, but it wasn't JSON."
            raise AttributeError

        return
 
    return inner_func




