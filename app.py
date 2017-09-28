import sys

class App():
    def __init__(self):
        self.commands = [
            {"arg": "-l", "desc": "Lists all the tasks"},
            {"arg": "-a", "desc": "Adds a new task"},
            {"arg": "-r", "desc": "Removes a task"},
            {"arg": "-c", "desc": "Completes a task"}
        ]

    def print_usage(self):
        print("Command Line Todo application\n" +
              "=============================\n\n" +
              "Command line arguments:\n" +
              self.commands[0]["arg"] + "   " + self.commands[0]["desc"] + "\n" +
              self.commands[1]["arg"] + "   " + self.commands[1]["desc"] + "\n" +
              self.commands[2]["arg"] + "   " + self.commands[2]["desc"] + "\n" +
              self.commands[3]["arg"] + "   " + self.commands[3]["desc"] + "\n")

def main():
    app = App()
    args = sys.argv[1:]
    if not args:
        app.print_usage()

main()
