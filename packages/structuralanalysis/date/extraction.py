import datetime
from yargy import Parser
from .fact import RANGE_DATE_PARSER, RangDateFact

class ExtractionDate:
    text = ""
    countFacts = 0
    start_date = None
    end_date = None
    
    def __init__(self, text):
        self.text = text
        self
    
    def updateDate(self, startyear, startmonth, startday, endyear, endmonth, endday):
        #сhange of year
        if startmonth is not None and endmonth is not None and startyear is not None and endyear is not None and startmonth > endmonth and startyear == endyear:
            endyear = endyear + 1

        fasts = 0
        start = datetime.datetime.now()
        end = datetime.datetime.now()
        if startyear is not None : 
            fasts = fasts + 1
            start = start.replace(year=startyear)
        if startmonth is not None : 
            fasts = fasts + 1
            start = start.replace(month=startmonth)
        if startday is not None : 
            fasts = fasts + 1
            start = start.replace(day=startday)

        if endyear is not None : 
            fasts = fasts + 1
            end = end.replace(year=endyear)
        if endmonth is not None : 
            fasts = fasts + 1
            end = end.replace(month=endmonth)
        if endday is not None : 
            fasts = fasts + 1
            end = end.replace(day=endday)

        if self.countFacts < fasts:
            self.countFacts = fasts
            self.start_date = start
            self.end_date = end
        
        return


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
                    if match.fact.startyear is not None and datetime.datetime.now().year >= match.fact.startyear :
                        startyear = match.fact.startyear
                except KeyError:
                    pass
                try:
                    if startmonth is None and match.fact.startmonth is not None:
                        startmonth = match.fact.startmonth
                except KeyError:
                    pass
                try:
                    if startday is None and match.fact.startday is not None:
                        startday = match.fact.startday
                except KeyError:
                    pass

                try:
                    if match.fact.endyear is not None and datetime.datetime.now().year >= match.fact.endyear:
                        endyear = match.fact.endyear
                except KeyError:
                    pass
                try:
                    if endmonth is None and match.fact.endmonth is not None:
                        endmonth = match.fact.endmonth
                except KeyError:
                    pass
                try:
                    if endday is None and match.fact.endday is not None:
                        endday = match.fact.endday
                except KeyError:
                    pass
                self.updateDate(startyear, startmonth, startday, endyear, endmonth, endday)
        return