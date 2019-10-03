from yargy import Parser
from fact import GENDER_PARSER, GenderFact


class ExtractionGender:
    text = ""
    
    def __init__(self, text):
        self.text = text
        self

    def get(self):
        parser = Parser(GENDER_PARSER)
        GenderFact = parser.find(self.text)
        if GenderFact:
            return GenderFact.fact.gender
        return None
