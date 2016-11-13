import datetime



def get_reminder(reminders, task_id):
    for r in reminders:
        if r["task_id"] == task_id:
            return r["date"]
    return None


# compares by time as well
def has_past_reminder(task, date=datetime.datetime.utcnow()):
    reminder_date = datetime.datetime.strptime(task["reminder_date"][:19], "%Y-%m-%dT%H:%M:%S")
    return reminder_date < date


# compares only by date
def has_today_reminder(task, date=datetime.datetime.utcnow()):
    date_formatted = date.isoformat()[0:10]

    try:
        if task['due_date'] == date_formatted:
            return True
        else:
            return False
    except:
        # no due date, assume today
        return True


def has_star(task):
    return task['starred']


def enrich_tasks_dates(tasks, reminders, date_default=datetime.datetime.utcnow()):
    #date_formatted = date_default.isoformat()[0:10] # take only the first 10 elements (YYYY-MM-DD)
    date_formatted = date_default.replace(hour=23, minute=59, second=59, microsecond=0).isoformat() + "Z"

    for task in tasks:
        reminder = get_reminder(reminders, task['id'])

        if reminder is not None:
            task["reminder_date"] = reminder
        else:
            task["reminder_date"] = date_formatted

    return


# get n of overdue, open items (unstarred, starred)
# assuming they are already "enriched"
def get_n_overdue(tasks, date=datetime.datetime.utcnow()):
    n_overdue_reg = 0
    n_overdue_star = 0

    for task in tasks:
        if has_past_reminder(task, date):
            if has_star(task):
                n_overdue_star += 1
            else:
                n_overdue_reg += 1

    return n_overdue_reg, n_overdue_star


def get_n_open(tasks):
    n_open_reg = 0
    n_open_star = 0

    for task in tasks:
        if has_star(task):
            n_open_star += 1
        else:
            n_open_reg += 1

    return n_open_reg, n_open_star


def get_today_tasks(tasks):
    todays_tasks = []
    today = datetime.datetime.now().isoformat()[0:10]
    for t in tasks:
        try:
            if t['due_date'] == today:
                todays_tasks.append(t)
        except:
            # No due date? Assume today
            todays_tasks.append(t)
            pass

    return todays_tasks

#
# def split_tasks_by_date(tasks, date=datetime.datetime.utcnow()):
#     day_tasks = []
#     other_tasks = []
#     date_formatted = date.isoformat()[0:10]
#     for t in tasks:
#         try:
#             if t['due_date'] == date_formatted:
#                 day_tasks.append(t)
#             else:
#                 other_tasks.append(t)
#         except:
#             # No due date? Assume today
#             day_tasks.append(t)
#             pass
#     return day_tasks, other_tasks
#
# #def split_tasks_by_
#
#
# def parse_tasks(tasks, reminders):
#     todays_tasks, other_tasks = split_tasks_by_date(tasks)
#
#     midnight_date = datetime.datetime.utcnow().replace(hour=23, minute=59, second=59, microsecond=0).isoformat() + "Z"
#     for t in todays_tasks:
#         reminder = get_reminder(reminders, t["id"])
#         if reminder != None:
#             t["reminder_date"] = reminder
#         else:
#             t["reminder_date"] = midnight_date
#     return todays_tasks, other_tasks
