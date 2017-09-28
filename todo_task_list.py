from todo_task import TodoTask

class TodoList(object):
    def __init__(self):
        self.task_list = []
        self.read_tasks_from_file()

    def read_tasks_from_file(self):
        with open("todo_data", "r") as tasks:
            task_list = tasks.read().split("\n")
            for task in task_list:
                complete = True if task[0] == "1" else False
                self.task_list.append(TodoTask(complete, description=task[1:]))
    