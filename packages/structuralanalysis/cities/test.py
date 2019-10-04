from yargy import Parser
from fact import CITY_PARSER, CityFact
from ipymarkup import show_markup
from dataloader import DataLoader
from IPython.display import display

lines = DataLoader().getTextList()
parser = Parser(CITY_PARSER)

for line in lines[:21]:
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
    print(result_list)
