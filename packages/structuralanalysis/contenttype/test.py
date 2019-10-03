from yargy import Parser
from ipymarkup import show_markup
from random import sample 
from IPython.display import display
from dataloader import DataLoader
from fact import CONTENT_TYPE_PARSER, ContentTypeFact

lines = DataLoader().getTextList()
parser = Parser(CONTENT_TYPE_PARSER)

for line in lines[:5]:
    match = parser.match(line)

# 5 first element from list
for line in lines[:5]:
    matches = list(parser.findall(line))
    for match in matches:
        print([_.value + ':' for _ in match.tokens])
    spans = [_.span for _ in matches]
    show_markup(line, spans)

# random element from list
for line in sample(lines, 5):
    matches = list(parser.findall(line))
    spans = [_.span for _ in matches]
    show_markup(line, spans)
