from datetime import datetime
from dateutil import parser

class TodoTask(object):
    def __init__(self, complete, description):
        self.complete = complete
        self.description = description

    def __str__(self):
        return str(("[x]" if self.complete else "[ ]")) + self.description

    def __repr__(self):
        return ("1" if self.complete else "0") + "||" + self.description


class TimedTodoTask(TodoTask):
    def __init__(self, complete, description, deadline):
        self.complete = complete
        self.description = description
        self.deadline = deadline

    def time_left_for_task(self):
        
        return str((parser.parse(self.deadline) - datetime.today()).days)

    def __str__(self):
        return (("[x]" if self.complete else "[ ]") + 
                self.description + " - Deadline in: " + 
                self.time_left_for_task() + " days")

    def __repr__(self):
        return ("1" if self.complete else "0") + "||" + self.description + "||" + self.deadline