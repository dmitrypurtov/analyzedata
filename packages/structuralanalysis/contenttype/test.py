from yargy import Parser
from ipymarkup import show_markup
from random import sample 
from IPython.display import display
from dataloader import DataLoader
from fact import CONTENT_TYPE_PARSER, ContentTypeFact

lines = DataLoader().getTextList()
parser = Parser(CONTENT_TYPE_PARSER)

for line in lines[:21]:
    result_list = []
    matches = list(parser.findall(line))
    print('----------------------------------------------------------------------')
    for match in matches:
        if match is not None:
            try:
                result_list.append(match.fact.content)
                print("Content: " + match.fact.content)
            except KeyError:
                print("Content: KeyError")             
    show_markup(line, [_.span for _ in matches])
    result_list = list(dict.fromkeys(result_list))
    print(result_list)
