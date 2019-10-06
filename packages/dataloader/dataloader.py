import os
import json
import re
import demoji

class DataLoader:
    def __init__(self):
        self

    def remove_tags(self, text):
        TAG_RE = re.compile(r'<[^>]+>')
        return TAG_RE.sub(' ', text)

    def remove_emoji(self, text):
        TAG_RE = demoji.replace(' ')
        return TAG_RE.sub(' ', text)

    def remove_highlighters(self, text):
        TAG_RE = text.replace('!', ' ')
        TAG_RE = text.replace('()', ' ')
        TAG_RE = text.replace(')', ' ')
        return TAG_RE.sub(' ', text)

    def getTextList(self):
        loaded_json = []
        result = []
        path = os.path.dirname(os.path.abspath(__file__)) + "/examples/" + 'offers.json'
        with open(path, encoding='utf-8') as fh:
            loaded_json = json.load(fh)
        for item in loaded_json:
            description = item['description']
            description = self.remove_tags(description)
            description = self.remove_emoji(description)
            description = self.remove_highlighters(description)
            result.append(description)
        return result
