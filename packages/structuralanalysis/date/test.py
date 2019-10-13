import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(
    __file__)).rsplit('packages')[0] + 'packages')

from yargy import Parser
from fact import RANGE_DATE_PARSER, RangDateFact
from ipymarkup import show_markup
from dataloader import DataLoader
from random import sample
from IPython.display import display


lines = DataLoader().exemple_offers()
parser = Parser(RANGE_DATE_PARSER)

for line in lines[:21]:
    result_list = []
    line = line.lower()
    matches = list(parser.findall(line))
    print('----------------------------------------------------------------------')
    for match in matches:
        if match is not None:
            try:
                #result_list.append(match.fact.gender)
                #print("startyear: " + match.fact.startyear)
                #print("startmonth: " + match.fact.startmonth)
                #print("startday: " + match.fact.startday)
                print(" ")
                #print("endyear: " + match.fact.endyear)
                #print("endmonth: " + match.fact.endmonth)
                #print("endday: " + match.fact.endday)
            except KeyError:
                print("Gender: KeyError")             
    show_markup(line, [_.span for _ in matches])
    result_list = list(dict.fromkeys(result_list))
    print(result_list)
