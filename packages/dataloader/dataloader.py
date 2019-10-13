import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(
    __file__)).rsplit('packages')[0] + 'packages')

import json
import re
from jsonencoder import JsonEncoder


class DataLoader:
    def __init__(self):
        self

    def remove_tags(self, text):
        TAG_RE = re.compile(r'<[^>]+>')
        return TAG_RE.sub(' ', text)

    def remove_highlighters(self, text):
        text = text.replace('!', ' ')
        text = text.replace('()', ' ')
        text = text.replace(')', ' ')
        return text.replace('  ', ' ')

    def exemple_offers(self):
        loaded_json = []
        result = []
        path = os.path.dirname(os.path.abspath(__file__)) + "/examples/" + 'offers.json'
        loaded_json = JsonEncoder().convert_to_object_from_file(path)
        for item in loaded_json:
            description = item['description']
            description = self.remove_tags(description)
            description = self.remove_highlighters(description)
            result.append(description)
        return result