from nodes import bases

class Root(bases.BlockNode):
    KIND = 'RootNode'
    def __init__(self):
        self.body = []

    def evaluate(self):
        for node in self.body:
            node.evaluate()