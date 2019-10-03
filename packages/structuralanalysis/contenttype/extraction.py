from yargy import Parser
from fact import CONTENT_TYPE_PARSER, ContentTypeFact


class ExtractionContentType:
    text = ""
    
    def __init__(self, text):
        self.text = text
        self

    def get(self):
        parser = Parser(CONTENT_TYPE_PARSER)
        ViewFact = parser.find(self.text)
        if ViewFact:
            return ViewFact.fact.content
        return None
