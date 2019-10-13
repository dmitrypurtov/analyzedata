import os
import json
from datetime import datetime


class CustomJsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        return o.__dict__

class JsonEncoder:
    def __init__(self):
        self

    def convert_to_json(self, json_object):
        return json.dumps(json_object, cls=CustomJsonEncoder)
    
    def convert_to_object(self, json_str):
        return json.loads(json_str)
    
    def convert_to_object_from_file(self, path):
        loaded_json = None
        with open(path, encoding='utf-8') as fh:
            loaded_json = json.load(fh)      
        return loaded_json
