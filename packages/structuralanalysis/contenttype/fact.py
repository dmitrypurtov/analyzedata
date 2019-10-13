from ipymarkup import show_markup
from yargy import rule, and_, or_
from yargy.interpretation import fact, attribute
from yargy.predicates import dictionary, normalized


ContentTypeFact = fact('ContentTypeFact', ['contenttype'])

CONTENTS = {
    'кастинг': 'Сasting',
    'фотосъемка': 'Photoshooting',
    'видеосъемка': 'Videoshooting',
    'реклама': 'Advertising',
    'шоу': 'TVShow',
    'клип': 'Clip',
    'показ': 'Fashionshow',
}

NAME = dictionary(CONTENTS).interpretation(
    ContentTypeFact.contenttype.normalized().custom(CONTENTS.__getitem__)
)

CONTENT_TYPE_PARSER = or_(
    rule(
        NAME
    ),
).interpretation(
    ContentTypeFact
)