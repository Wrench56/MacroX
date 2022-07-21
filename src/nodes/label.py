from nodes import bases

class LabelNode(bases.BlockNode):
    KIND = 'LabelNode'
    def __init__(self) -> None:
        self.body = []

    def evaluate(self, jump=False):
        super().evaluate()
        if jump:
            for node in self.body:
                super().evaluate()
                node.evaluate()