from nodes import bases
import globals

class BreakNode(bases.Node):
    KIND = 'BreakNode'
    def __init__(self) -> None:
        pass

    def evaluate(self):
        globals.break_bool = True

    def prettyprint(self, indent) -> str:
        return f'{self.KIND}()'