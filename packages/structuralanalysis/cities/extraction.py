from yargy import Parser
from fact import CITY_PARSER, CityFact


class ExtractionCity:
    text = ""
    
    def __init__(self, text):
        self.text = text
        self

    def get(self):
        result_list = []
        parser = Parser(CITY_PARSER)
        matches = list(parser.findall(self.text))
        for match in matches:
            if match is not None:
                try:
                    result_list.append(match.fact.city)
                except KeyError:
                    pass

        result_list = list(dict.fromkeys(result_list))
        return result_list
