from ipymarkup import show_markup
from yargy import rule, and_, or_
from yargy.interpretation import fact, attribute
from yargy.predicates import eq, gte, lte, length_eq, dictionary, normalized

DayWeekDateFact = fact('DayWeekDateFact', [
                       'week', attribute('current_era', True)])

WEEKS = {
    'Понедельник': 1,
    'Вторник': 2,
    'Среда': 3,
    'Четверг': 4,
    'Пятница': 5,
    'Суббота': 6,
    'Воскресенье': 7,
    'Пнд': 1,
    'Втр': 2,
    'Срд': 3,
    'Чтв': 4,
    'Птн': 5,
    'Сбт': 6,
    'Вск': 7,
    'Пн': 1,
    'Вт': 2,
    'Ср': 3,
    'Чт': 4,
    'Пт': 5,
    'Сб': 6,
    'Вс': 7,
}

WEEK_NAME = dictionary(WEEKS).interpretation(
    DayWeekDateFact.week.normalized().custom(WEEKS.__getitem__)
)

WEEK_DATE_PARSER = or_(
    rule(
        WEEK_NAME
    )
).interpretation(
    DayWeekDateFact
)
