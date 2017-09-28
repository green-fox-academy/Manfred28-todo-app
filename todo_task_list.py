from todo_task import TodoTask

class TodoList(object):
    def __init__(self):
        self.task_list = []
        self.read_tasks_from_file()

    def read_tasks_from_file(self):
        with open("todo_data", "r") as tasks:
            for task in tasks.read().split("\n"):
                if task:
                    complete = True if task[0] == "1" else False
                    self.task_list.append(TodoTask(complete, description=task[1:]))
    
    def add_task(self, description):
        self.task_list.append(TodoTask(False, " " + description))
        self.update_file()

    def remove_task(self, index):
        del self.task_list[int(index) - 1]
        self.update_file()

    def complete_task(self, index):
        self.task_list[int(index)-1].complete = not self.task_list[int(index) - 1].complete
        self.update_file()

    def update_file(self):
        with open("todo_data", "w") as todo_data:
            for task in self.task_list:
                complete = "1" if task.complete else "0"
                todo_data.write(complete + task.description + "\n")
