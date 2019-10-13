import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(
    __file__)).rsplit('packages')[0] + 'packages')

from yargy import Parser
from ipymarkup import show_markup
from random import sample 
from IPython.display import display
from dataloader import DataLoader
from fact import CONTENT_TYPE_PARSER, ContentTypeFact

lines = DataLoader().exemple_offers()
parser = Parser(CONTENT_TYPE_PARSER)

for line in lines[:10]:
    result_list = []
    matches = list(parser.findall(line))
    print('----------------------------------------------------------------------')
    print("Content: ")
    for match in matches:
        if match is not None:
            try:
                result_list.append(match.fact.contenttype)
                print("\t", match.fact.contenttype)
            except KeyError:
                print("Content: KeyError")             
    result_list = list(dict.fromkeys(result_list))
    print("Result:")
    print(result_list)
    show_markup(line, [_.span for _ in matches])
