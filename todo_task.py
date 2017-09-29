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

    def time_left_for_task(self):
        return str((parser.parse(self.deadline) - datetime.today()).days)

    def __str__(self):
        return (("[x]" if self.complete else "[ ]") + 
                self.description + " - Deadline in: " + 
                self.time_left_for_task() + " days")
