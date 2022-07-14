from nodes import bases

class LabelNode(bases.BlockNode):
    KIND = 'LabelNode'
    def __init__(self) -> None:
        self.body = []

    def evaluate(self, jump=False):
        if jump:
            for node in self.body:
                node.evaluate()