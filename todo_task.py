from datetime import datetime
from dateutil import parser

class TodoTask(object):
    def __init__(self, complete, description):
        self.type = "regular"
        self.complete = (complete == "True")
        self.description = description

    def __str__(self):
        return str(("[x]" if self.complete else "[ ]")) + self.description

    def __repr__(self):
        prop_values = []
        for k, v, in self.__dict__.items():
            prop_values.append(str(v))
        return "||".join(prop_values)


class TimedTodoTask(TodoTask):
    def __init__(self, complete, description, deadline):
        self.type = "timed"
        self.complete = (complete == "True")
        self.description = description
        self.deadline = deadline

    def check_deadline(self):
        days_until_deadline = str((parser.parse(self.deadline) - datetime.today()).days)
        if int(days_until_deadline) > 0:
            return "Deadline in: " + days_until_deadline + " days"
        else:
            return "Deadline over"


    def __str__(self):
        return (("[x]" if self.complete else "[ ]") + 
                self.description + " - " + self.check_deadline())
