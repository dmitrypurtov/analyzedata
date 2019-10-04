from ipymarkup import show_markup
from yargy import rule, and_, or_
from yargy.interpretation import fact, attribute
from yargy.predicates import dictionary, normalized

ProfileTypeFact = fact('ProfileTypeFact', ['profile'])

PROFILES = {
    'Модель': 'model',
}

NAME = dictionary(PROFILES).interpretation(
    ProfileTypeFact.profile.normalized().custom(PROFILES.__getitem__)
)

PROFILE_TYPE_PARSER = or_(
    rule(
        NAME
    ),
).interpretation(
    ProfileTypeFact
)
