import sys

class App():
    def __init__(self):
        self.commands = [
            {"arg": "-l", "desc": "Lists all the tasks"},
            {"arg": "-a", "desc": "Adds a new task"},
            {"arg": "-r", "desc": "Removes an task"},
            {"arg": "-c", "desc": "Completes an task"}
        ]

    def print_usage(self):
        print("Command Line Todo application\n" +
              "=============================" +
              "\n" +
              "Command line arguments:" +
              self.commands[0]["arg"] + "   " + self.commands[0]["desc"] + "\n" +
              self.commands[1]["arg"] + "   " + self.commands[1]["desc"] + "\n" +
              self.commands[2]["arg"] + "   " + self.commands[3]["desc"] + "\n" +
              self.commands[4]["arg"] + "   " + self.commands[4]["desc"] + "\n")

def main():
    app = App()
    args = sys.argv[1:]
    if not args:
        app.print_usage()

main()
