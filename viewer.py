class Viewer(object):
    def print_usage(self, commands):
        print("Command Line Todo application\n" +
              "=============================\n\n" +
              "Command line arguments:")
        for command in commands:
            print(command["arg"] + "   " + command["desc"])
