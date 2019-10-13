import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(
    __file__)).rsplit('packages')[0] + 'packages')

from yargy import Parser
from facts import CITY_PARSER, CityFact
from ipymarkup import show_markup
from dataloader import DataLoader
from IPython.display import display

lines = DataLoader().exemple_offers()
parser = Parser(CITY_PARSER)

for line in lines[:1]:
    result_list = []
    matches = list(parser.findall(line))
    print('----------------------------------------------------------------------')
    for match in matches:
        if match is not None:
            try:
                result_list.append(match.fact.city)
                print("City: " + match.fact.city)
            except KeyError:
                print("City: KeyError")             
    show_markup(line, [_.span for _ in matches])
    result_list = list(dict.fromkeys(result_list))
    print(next(iter(result_list), ''))
