import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(
    __file__)).rsplit('packages')[0] + 'packages')

from yargy import Parser
from fact import GENDER_PARSER, GenderFact
from ipymarkup import show_markup
from dataloader import DataLoader
from IPython.display import display

lines = DataLoader().exemple_offers()
parser = Parser(GENDER_PARSER)

for line in lines[:21]:
    result_list = []
    matches = list(parser.findall(line))
    print('----------------------------------------------------------------------')
    print("Gender: ")
    for match in matches:
        if match is not None:
            try:
                result_list.append(match.fact.gender)
                print("\t" + match.fact.gender)
            except KeyError:
                print("\tKeyError")               
    result_list = list(dict.fromkeys(result_list))
    print("Result:")
    print(result_list)
    show_markup(line, [_.span for _ in matches])

