from nodes import bases
import globals

class BreakNode(bases.InstructionNode):
    KIND = 'BreakNode'
    def __init__(self) -> None:
        pass

    def evaluate(self):
        super().evaluate()
        globals.break_bool = True