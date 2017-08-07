

from functools import wraps
import json
from jsonschema import validate, FormatChecker, ValidationError
from datetime import datetime 

def json_attribs_check(func):
    """
        Decorator for validating json, a thing we might do often.
     
        Use the standard syntctical sugar:
            @json_attribs_check
            def my_json_related_function():
                doSomeStuff()
        This syntax ensures @json_attribs_check always runs before defined func 
    """
    @wraps(func)
    def inner_func(jsonStr):
        gslvtsSchema = {"type":"object",
                        "properties":{
                            "tagID": {"type":"number"}, 
                            "UTC": {"type":"string",
                                    "format":"date-time"}
                            }
                       }
        try:
            jsonGslvts=json.loads(jsonStr)
            for elem in jsonGslvts:
                try: 
                    validate(elem, gslvtsSchema, format_checker=FormatChecker())
                except ValidationError, e:
                    print "[-] Invalid json post data. Check it, brah."
                    print e
                    raise AttributeError 
        except (AttributeError, ValueError):
            print "[-] IDk what that was, but it wasn't JSON."
            raise AttributeError

        return
 
    return inner_func




