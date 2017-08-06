


def buffer_values(jsonStr):
    try:
        print jsonStr.keys()
        print jsonStr.values()
    except (AttributeError, ValueError):
        print "[-] IDk what that was, but it wasn't JSON."
        raise AttributeError
    return 
