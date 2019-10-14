import re
from yargy import Parser


class ExtractionContact:
    text = ""
    
    def __init__(self, text):
        self.text = text
        self

    def getEmails(self):
        result_list = []
        result_list = re.findall('([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)', self.text)
        result_list = list(dict.fromkeys(result_list))
        return next(iter(result_list), '')

    def getPhones(self):
        result_list = []
        result_list = re.findall('(?:\B\+ ?49|\b0)(?: *[(-]? *\d(?:[ \d]*\d)?)? *(?:[)-] *)?\d+ *(?:[/)-] *)?\d+ *(?:[/)-] *)?\d+(?: *- *\d+)?', self.text)
        result_list = list(dict.fromkeys(result_list))
        return next(iter(result_list), '')

    def getUrls(self):
        result_list = []
        result_list = re.findall(
            'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', self.text)
        result_list = list(dict.fromkeys(result_list))
        return next(iter(result_list), '')
