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
        self.viewer = Viewer()
        self.todo_list = TodoList()

    def run(self):
        if not self.arguments:
            self.viewer.print_usage(self.commands)
        else:
            try:
                self.parse_arguments()()
            except KeyError:
                print("\n***Unsupported argument***\n")
                self.viewer.print_usage(self.commands)

    def parse_arguments(self):
        return {
            "-l": lambda: self.viewer.print_tasks(self.todo_list.task_list),
            "-a": lambda: self.todo_list.add_task(self.arguments),
            "-r": lambda: self.todo_list.remove_task(self.arguments),
            "-c": lambda: self.todo_list.complete_task(self.arguments)
        }[self.arguments[0]]

def main():
    app = App()
    app.run()
   
main()
