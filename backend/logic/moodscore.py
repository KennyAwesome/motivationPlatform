import random

from config import mood


# usage
# m = Mood()
# m.absoluteValue = 42 # you can set it the hard way
# m.updateAbsoluteValue(isDone=False,isStarred=False)
# pleasureCategory = m.lookupPleasure() #range is (1 - 4)

def calculate_points(tasks_done, tasks_overdue):
    points = 0

    for task in tasks_done:
        if task['starred']:
            points += mood.MOOD_POINTS_STARRED
        else:
            points += mood.MOOD_POINTS_REGULAR

    for task in tasks_overdue:
        if task['starred']:
            points -= mood.MOOD_POINTS_STARRED
        else:
            points -= mood.MOOD_POINTS_REGULAR

    if points < 0:
        points = 0

    return points


def calculate_score(points):
    pleasure = mood.MOOD_PLEASURE_BASE ** (mood.MOOD_PLEASURE_FACTOR * points) + 1

    for m in mood.MOODS:
        if pleasure <= m['upper_bound']:
            return m

    return mood.MOODS[0]


def get_speech(m):
    speeches = mood.MOOD_SPEECHES[m['name']]
    i = random.randint(0, len(speeches) - 1)

    return speeches[i]