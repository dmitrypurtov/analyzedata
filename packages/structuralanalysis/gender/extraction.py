from yargy import Parser
from fact import GENDER_PARSER, GenderFact


class ExtractionGender:
    text = ""
    
    def __init__(self, text):
        self.text = text
        self

    def get(self):
        result_list = []
        parser = Parser(GENDER_PARSER)
        matches = list(parser.findall(self.text))
        for match in matches:
            if match is not None:
                try:
                    result_list.append(match.fact.gender)
                except KeyError:
                    pass

        result_list = list(dict.fromkeys(result_list))
        return result_list
