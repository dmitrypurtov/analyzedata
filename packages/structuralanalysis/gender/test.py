from yargy import Parser
from fact import GENDER_PARSER, GenderFact
from ipymarkup import show_markup
from dataloader import DataLoader
from random import sample
from IPython.display import display

lines = DataLoader().getTextList()
parser = Parser(GENDER_PARSER)

# 5 first element from list
for line in lines[:20]:
    matches = list(parser.findall(line))
    print('----------------------------------------------------------------------')
    for match in matches:
        display(match.fact)
        print([_.value + ':' for _ in match.tokens])
    spans = [_.span for _ in matches]
    show_markup(line, spans)

# random element from list
for line in sample(lines, 5):
    matches = list(parser.findall(line))
    spans = [_.span for _ in matches]
    show_markup(line, spans)
