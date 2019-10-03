from ipymarkup import show_markup
from yargy import rule, and_, or_
from yargy.interpretation import fact, attribute
from yargy.predicates import eq, gte, lte, length_eq, dictionary, normalized
from IPython.display import display

MonthDayDateFact = fact('MonthDayDateFact', ['month', 'day',
                         attribute('current_era', True)])

MONTHS = {
    'январь': 1,
    'февраль': 2,
    'март': 3,
    'апрель': 4,
    'май': 5,
    'июнь': 6,
    'июль': 7,
    'август': 8,
    'сентябрь': 9,
    'октябрь': 10,
    'ноябрь': 11,
    'декабрь': 12,
}

MONTH_NAME = dictionary(MONTHS).interpretation(
    MonthDayDateFact.month.normalized().custom(MONTHS.__getitem__)
)

MONTH = and_(
    gte(1),
    lte(12)
).interpretation(
    MonthDayDateFact.month.custom(int)
)

DAY = and_(
    gte(1),
    lte(31)
).interpretation(
    MonthDayDateFact.day.custom(int)
)

MOUNTH_DAY_DATE_PARSER = or_(
    rule(
        MONTH_NAME,
        DAY
    ),
    rule(
        DAY,
        MONTH_NAME
    ),
).interpretation(
    MonthDayDateFact
)
