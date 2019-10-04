from yargy import Parser
from fulldate import FULL_DATE_PARSER, FullDateFact
from monthday import MOUNTH_DAY_DATE_PARSER, MonthDayDateFact
from dayweek import WEEK_DATE_PARSER, DayWeekDateFact
from ipymarkup import show_markup
from dataloader import DataLoader
from random import sample
from IPython.display import display


lines = DataLoader().getTextList()
parser = Parser(MOUNTH_DAY_DATE_PARSER)

for line in lines[:21]:
    result_list = []
    matches = list(parser.findall(line))
    print('----------------------------------------------------------------------')
    for match in matches:
        if match is not None:
            try:
                result_list.append(match.fact.gender)
                print("Gender: " + match.fact.gender)
            except KeyError:
                print("Gender: KeyError")             
    show_markup(line, [_.span for _ in matches])
    result_list = list(dict.fromkeys(result_list))
    print(result_list)
