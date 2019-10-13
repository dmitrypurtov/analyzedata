from yargy import Parser
from .fact import CONTENT_TYPE_PARSER, ContentTypeFact


class ExtractionContentType:
    text = ""
    
    def __init__(self, text):
        self.text = text
        self

    def get(self):
        result_list = []
        parser = Parser(CONTENT_TYPE_PARSER)
        matches = list(parser.findall(self.text))
        for match in matches:
            if match is not None:
                try:
                    result_list.append(match.fact.contenttype)
                except KeyError:
                    pass

        result_list = list(dict.fromkeys(result_list))
        return result_list