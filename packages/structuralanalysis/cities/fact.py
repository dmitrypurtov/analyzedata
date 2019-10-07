from ipymarkup import show_markup
from yargy import rule, and_, or_
from yargy.interpretation import fact, attribute
from yargy.predicates import dictionary, normalized

CityFact = fact('CityFact', ['city'])

CITIES = {
    'Москва': '236',
    'МСК': '236',
    'Санкт-Петербург': '16113',
    'СПБ': '16113',
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