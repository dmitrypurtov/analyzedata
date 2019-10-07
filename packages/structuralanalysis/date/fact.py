from ipymarkup import show_markup
from yargy import rule, and_, or_
from yargy.interpretation import fact, attribute
from yargy.predicates import eq, gte, lte, length_eq, dictionary, normalized
from IPython.display import display

RangDateFact = fact('RangDateFact', ['startyear', 'startmonth', 'startday','endyear', 'endmonth', 'endday',
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

START_MONTH_NAME = dictionary(MONTHS).interpretation(RangDateFact.startmonth.normalized().custom(MONTHS.__getitem__))
END_MONTH_NAME = dictionary(MONTHS).interpretation(RangDateFact.endmonth.normalized().custom(MONTHS.__getitem__))

START_MONTH = and_(gte(1), lte(12)).interpretation(RangDateFact.startmonth.custom(int))
END_MONTH = and_(gte(1), lte(12)).interpretation(RangDateFact.endmonth.custom(int))

START_DAY = and_(gte(1),lte(31)).interpretation(RangDateFact.startday.custom(int))
END_DAY = and_(gte(1),lte(31)).interpretation(RangDateFact.endday.custom(int))

START_YEAR = and_(gte(2000),lte(2100)).interpretation(RangDateFact.startyear.custom(int))
END_YEAR = and_(gte(2000),lte(2100)).interpretation(RangDateFact.endyear.custom(int))

START_YEAR_SHORT = and_(gte(1),lte(99)).interpretation(RangDateFact.startyear.custom(int))
END_YEAR_SHORT = and_(gte(1),lte(99)).interpretation(RangDateFact.endyear.custom(int))

START_PREFIX = or_(rule(normalized('c')))
END_PREFIX = or_(rule(normalized('по')),  rule(normalized('на')), rule(normalized('и')), rule(normalized('до')), rule(eq('-')))


RANGE_DATE_PARSER = or_(
    #5.09 / 5.09.2019
    rule(
        START_DAY,
        '.',
        START_MONTH,
        '.',
        or_(
            START_YEAR,
            START_YEAR_SHORT
        ).optional()
    ),
    #8.09-8.09 / 8.09.2019-9.09.2019
    rule(
        START_DAY,
        '.',
        START_MONTH,
        eq('.').optional(),
        or_(
            START_YEAR,
            START_YEAR_SHORT
        ).optional(),
        END_PREFIX,
        END_DAY,
        '.',
        END_MONTH,
        eq('.').optional(),
        or_(
            END_YEAR,
            END_YEAR_SHORT
        ).optional()
    ),
    #8.09 по 8.09 / 8.09.2019 по 8.09.2019
    rule(
        START_PREFIX.optional(),
        START_DAY,
        '.',
        START_MONTH,
        eq('.').optional(),
        or_(
            START_YEAR,
            START_YEAR_SHORT
        ).optional(),
        END_PREFIX,
        END_DAY,
        '.',
        END_MONTH,
        eq('.').optional(),
        or_(
            END_YEAR,
            END_YEAR_SHORT
        ).optional()
    ),
    #5 стентября
    rule(
        START_DAY,
        START_MONTH_NAME,
        or_(
            START_YEAR,
            START_YEAR_SHORT
        ).optional()
    ),
    # 5 по 8 сентября /  5 сентября по 8 сентября
    rule(
        START_PREFIX.optional(),
        START_DAY,
        START_MONTH_NAME.optional(),
        or_(
            START_YEAR,
            START_YEAR_SHORT
        ).optional(),
        END_PREFIX,
        END_DAY,
        END_MONTH_NAME,
        or_(
            END_YEAR,
            END_YEAR_SHORT
        ).optional()
    )
).interpretation(
    RangDateFact
)
