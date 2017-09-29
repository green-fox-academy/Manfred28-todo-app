from datetime import datetime, timedelta

from todo_task import TodoTask, TimedTodoTask

class TodoList(object):
    def __init__(self):
        self.task_list = []
        self.read_tasks_from_file()

    def read_tasks_from_file(self):
        with open("todo_data", "r") as tasks:
            for task in tasks.read().split("\n"):
                if task:
                    task = task.split("||")
                    if task[0] == "regular":
                        self.task_list.append(TodoTask(*task[1:]))
                    else:
                        self.task_list.append(TimedTodoTask(*task[1:]))

    def filter_tasks(self, args):
        if "a" in args[0][2:]:
            return self.task_list
        else:
            return [task for task in self.task_list if not task.complete]

    def add_task(self, args):
        if len(args) < 2:
            return args[0]
        if "d" in args[0][2:]:
            description = " " + " ".join(args[2:])
            self.task_list.append(TimedTodoTask("False", description, deadline=args[1]))
        else:
            description = " " + " ".join(args[1:])
            self.task_list.append(TodoTask("False", description))
        self.update_file()


    def remove_task(self, args):
        if len(args) != 2 or not args[1].isdigit():
            return args[0]
        del self.task_list[int(args[1]) - 1]
        self.update_file()

    def complete_task(self, args):
        if len(args) != 2 or not args[1].isdigit():
            return args[0]
        self.task_list[int(args[1])-1].complete = not self.task_list[int(args[1]) - 1].complete
        self.update_file()

    def update_file(self):
        with open("todo_data", "w") as todo_data:
            for task in self.task_list:
                todo_data.write(repr(task) + "\n")
