from ipymarkup import show_markup
from yargy import rule, and_, or_
from yargy.interpretation import fact, attribute
from yargy.predicates import dictionary, normalized

GenderFact = fact('GenderFact', ['gender'])

GENDERS = {
    'мужчина': 'Male',
    'парень': 'Male',
    'женщина': 'Female',
    'девушка': 'Female',
    'мальчик': 'Male',
    'девочка': 'Female',
}

NAME = dictionary(GENDERS).interpretation(
    GenderFact.gender.normalized().custom(GENDERS.__getitem__)
)

GENDER_PARSER = or_(
    rule(
        NAME
    ),
).interpretation(
    GenderFact
)