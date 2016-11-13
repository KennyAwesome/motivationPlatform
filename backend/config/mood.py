# values for the moodscore
MOOD_ABSOLUTE_VALUE = 0.0

MOOD_POINTS_MAX = 100
MOOD_POINTS_STARRED = 20
MOOD_POINTS_REGULAR = 10

MOOD_PLEASURE_BASE = -0.88
MOOD_PLEASURE_FACTOR = 0.2

MOOD_EXPRESSION_RANGE = 5

MOODS = [
    {
        'name': 'excited',
        'upper_bound': 0.2
    },
    {
        'name': 'encouraging',
        'upper_bound': 0.4
    },
    {
        'name': 'happy',
        'upper_bound': 0.6
    },
    {
        'name': 'boss',
        'upper_bound': 1.0
    }
]