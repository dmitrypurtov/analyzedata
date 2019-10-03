import os
import json
import re


class DataLoader:
    def __init__(self):
        self

    def remove_tags(self, text):
        TAG_RE = re.compile(r'<[^>]+>')
        return TAG_RE.sub(' ', text)

    def getTextList(self):
        loaded_json = []
        result = []
        path = os.path.dirname(os.path.abspath(__file__)) + "\\" + 'data.json'
        with open(path, encoding='utf-8') as fh:
            loaded_json = json.load(fh)
        for item in loaded_json:
            description = item['description']
            description = self.remove_tags(description)
            result.append(description)
        return result
