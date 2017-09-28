class Viewer(object):
    def print_usage(self, commands):
        print("Command Line Todo application\n" +
              "=============================\n\n" +
              "Command line arguments:")
        for command in commands:
            print(command["arg"] + "   " + command["desc"])

    def print_tasks(self, tasks):
        if tasks:
            for task in tasks:
                print(task)
        else:
            print("No todos for today! :)")
            