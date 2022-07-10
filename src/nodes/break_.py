from nodes import bases
import globals

class BreakNode(bases.Node):
    def __init__(self) -> None:
        pass

    def evaluate(self):
        globals.break_bool = True

    def prettyprint(self, indent=0) -> str:
        return 'Break'

    def __repr__(self) -> str:
        return self.prettyprint()