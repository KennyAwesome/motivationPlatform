import datetime


def get_reminder(reminders, task_id):
    for r in reminders:
        if r["task_id"] == task_id:
            return r["date"]
    return None


def get_tasks_by_date(tasks, date=datetime.datetime.utcnow()):
    day_tasks = []
    other_tasks = []
    date_formatted = date.isoformat()[0:10]
    for t in tasks:
        try:
            if t['due_date'] == date_formatted:
                day_tasks.append(t)
            else:
                other_tasks.append(t)
        except:
            # No due date? Assume today
            day_tasks.append(t)
            pass
    return day_tasks, other_tasks


def parse_tasks(tasks, reminders):
    todays_tasks, other_tasks = get_tasks_by_date(tasks)

    midnight_date = datetime.datetime.utcnow().replace(hour=23, minute=59, second=59, microsecond=0).isoformat() + "Z"
    for t in todays_tasks:
        reminder = get_reminder(reminders, t["id"])
        if reminder != None:
            t["reminder_date"] = reminder
        else:
            t["reminder_date"] = midnight_date
    return todays_tasks


def is_past_reminder(task, date=datetime.datetime.utcnow()):
    reminder_date = datetime.datetime.strptime(task["reminder_date"][:19], "%Y-%m-%dT%H:%M:%S")
    return reminder_date < date
