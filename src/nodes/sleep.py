from nodes import bases
from time import sleep

class SleepNode(bases.InstructionNode):
    KIND = 'SleepNode'
    def __init__(self, time: int) -> None:
        self.time = time

    def evaluate(self):
        sec = self.time / 1000
        sleep(sec)

    def prettyprint(self, indent):
        indent_str = ' '*indent
        return f'{self.KIND} (\n{indent_str}    Time: {str(self.time)}ms\n{indent_str})'