import random

from config import mood


# def calculate_points(tasks_done, tasks_overdue):
def calculate_points(n_done_reg, n_done_star, n_overd_reg, n_overd_star):
    points_positive = n_done_reg * mood.MOOD_POINTS_REGULAR + n_done_star * mood.MOOD_POINTS_STARRED
    points_negative = n_overd_reg * mood.MOOD_POINTS_REGULAR + n_overd_star * mood.MOOD_POINTS_STARRED

    points = points_positive - points_negative

    if points < 0:
        points = 0

    return points


def calculate_score(points):
    pleasure = mood.MOOD_PLEASURE_BASE ** (mood.MOOD_PLEASURE_FACTOR * float(points)) + 1

    for m in mood.MOODS:
        if pleasure <= m['upper_bound']:
            return m, pleasure

    return mood.MOODS[0], pleasure


def get_speech(m):
    speeches = mood.MOOD_SPEECHES[m['name']]
    i = random.randint(0, len(speeches) - 1)

    return speeches[i]
