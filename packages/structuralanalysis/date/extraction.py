import datetime
from yargy import Parser
from fact import RANGE_DATE_PARSER, RangDateFact


class ExtractionDate:
    text = ""
    start_date = None
    end_date = None
    
    def __init__(self, text):
        self.text = text
        self

    def getDate(self):
        parser = Parser(RANGE_DATE_PARSER)
        matches = list(parser.findall(self.text))
        startyear = datetime.datetime.now().year
        startmonth = None
        startday = None
        endyear = datetime.datetime.now().year
        endmonth = None
        endday = None
        for match in matches:
            if match is not None:
                try:
                    if datetime.datetime.now().year >= match.fact.startyear :
                        startyear = match.fact.startyear
                except KeyError:
                    pass
                try:
                    if startmonth is None:
                        startmonth = match.fact.startmonth
                except KeyError:
                    pass
                try:
                    if startday is None:
                        startday = match.fact.startday
                except KeyError:
                    pass

                try:
                    if datetime.datetime.now().year >= match.fact.endyear:
                        endyear = match.fact.endyear
                except KeyError:
                    pass
                try:
                    if endmonth is None:
                        endmonth = match.fact.endmonth
                except KeyError:
                    pass
                try:
                    if endday is None:
                        endday = match.fact.startyear
                except KeyError:
                    pass

        if (startmonth is not None and startday is not None) :
            start_date = datetime.date(startyear, startmonth, startday)

        if (startmonth is not None and startday is not None):
            end_date = datetime.date(endyear, endmonth, endday)