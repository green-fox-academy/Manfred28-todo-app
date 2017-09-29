import sys
import datetime
from viewer import Viewer
from todo_task_list import TodoList

class App():
    def __init__(self):
        self.commands = [
            {"arg": "-h", "desc": "Lists the available commands", "usage": "usage: app.py -h"},
            {"arg": "-l", "desc": "Lists all the tasks", "usage": "usage: app.py -l"},
            {"arg": "-a", "desc": "Adds a new task", "usage": "usage: app.py -a task"},
            {"arg": "-r", "desc": "Removes a task", "usage": "usage: app.py -r [number]"},
            {"arg": "-c", "desc": "Completes a task", "usage": "usage: app.py -c [number]"}
        ]
        self.arguments = sys.argv[1:]
        self.viewer = Viewer()
        self.todo_list = TodoList()

    def run(self):
        if not self.arguments:
            self.viewer.print_usage(self.commands)
        else:
            try:
                if self.parse_arguments()() != None:
                    command_index = self.lookup_command(self.arguments[0])
                    print("\n***Unsupported argument***\n")
                    print(self.commands[command_index]["usage"])
            except KeyError:
                print("\n***Unsupported argument***\n")
                self.viewer.print_usage(self.commands)

    def parse_arguments(self):
        return {
            "-h": lambda: self.viewer.print_usage(self.commands),
            "-l": lambda: self.viewer.print_tasks(self.todo_list.filter_tasks(self.arguments)),
            "-a": lambda: self.todo_list.add_task(self.arguments),
            "-r": lambda: self.todo_list.remove_task(self.arguments),
            "-c": lambda: self.todo_list.complete_task(self.arguments)
        }[self.arguments[0][0:2]]

    def lookup_command(self, command):
            for item in self.commands:
                if item["arg"] == command:
                    return self.commands.index(item)


def main():
    app = App()
    app.run()
   
main()
