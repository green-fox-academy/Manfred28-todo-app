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


def main():
    app = App()
    viewer = Viewer()
    todo_list = TodoList()
    args = sys.argv[1:]
    if not args:
        viewer.print_usage(app.commands)
    elif args[0] == "-l" and len(args) == 1:
        viewer.print_tasks(todo_list.task_list)

main()
