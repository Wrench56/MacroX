class Window():
    def __init__(self, *args):
        self.execute(args.copy())

    def execute(self):
        print('Hello World!')
        