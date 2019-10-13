from ipymarkup import show_markup
from yargy import rule, and_, or_
from yargy.interpretation import fact, attribute
from yargy.predicates import dictionary, normalized

CityFact = fact('CityFact', ['city'])

CITIES = {
    'москва': '236',
    'мск': '236',
    'санкт-петербург': '16113',
    'петербург': '16113',
    'питер': '16113',
    'сбп': '16113',
}

NAME = dictionary(CITIES).interpretation(
    CityFact.city.normalized().custom(CITIES.__getitem__)
)

CITY_PARSER = or_(
    rule(
        NAME
    ),
).interpretation(
    CityFact
)