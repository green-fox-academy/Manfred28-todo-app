class TodoTask(object):
    def __init__(self, complete, description):
        self.complete = complete
        self.description = description

    def __str__(self):
        return ("[x]" if self.complete else "[ ]") + self.description
