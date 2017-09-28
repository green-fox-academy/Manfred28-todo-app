import sys
from viewer import Viewer
from todo_task_list import TodoList

class App():
    def __init__(self):
        self.commands = [
            {"arg": "-l", "desc": "Lists all the tasks"},
            {"arg": "-a", "desc": "Adds a new task"},
            {"arg": "-r", "desc": "Removes a task"},
            {"arg": "-c", "desc": "Completes a task"}
        ]
        self.arguments = sys.argv[1:]

    def run(self):
        viewer = Viewer()
        todo_list = TodoList()
        if not self.arguments:
            viewer.print_usage(self.commands)
        elif self.arguments[0] == "-l" and len(self.arguments) == 1:
            viewer.print_tasks(todo_list.task_list)
        elif self.arguments[0] == "-a":
            todo_list.add_task(self.arguments[1])
        elif self.arguments[0] == "-r":
            todo_list.remove_task(self.arguments[1])
        elif self.arguments[0] == "-c" and self.arguments[1].isdigit():
            todo_list.complete_task(self.arguments[1])


def main():
    app = App()
    app.run()
   
main()
