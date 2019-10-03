from yargy import rule, or_
from yargy.interpretation import fact, attribute
from yargy.predicates import dictionary, normalized

ContentTypeFact = fact(
    'ContentTypeFact', ['content', attribute('current_era', True)])

CONTENTS = {
    'съемки': 'shooting',
    'кастинг': 'casting',
}

NAME = dictionary(CONTENTS).interpretation(
    ContentTypeFact.content.normalized().custom(CONTENTS.__getitem__)
)

CONTENT_TYPE_PARSER = or_(
    rule(
        NAME
    ),
).interpretation(
    ContentTypeFact
)
