import datetime
from yargy import Parser
from .fulldate import FULL_DATE_PARSER, FullDateFact

class ExtractionDate:
    text = ""
    
    def __init__(self, text):
        self.text = text
        self

    def getDate(self):
        parser = Parser(FULL_DATE_PARSER)
        DateFact = parser.find(self.text)
        if DateFact:
            return datetime.date(DateFact.fact.year, DateFact.fact.month, DateFact.fact.day)
        return None