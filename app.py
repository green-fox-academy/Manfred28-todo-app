import sys
from viewer import Viewer

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
    args = sys.argv[1:]
    if not args:
        viewer.print_usage(app.commands)

main()
