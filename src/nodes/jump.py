from nodes import bases
from globals import JH

class JumpNode(bases.Node):
    KIND = 'JumpNode'
    def __init__(self, label) -> None:
        self.label = label[1:] #! label[1:], since the first char is "~"

    def evaluate(self):
        JH.jump(self.label)

    def prettyprint(self, indent):
        indent_str = ' '*indent

        return f'{self.KIND} (\n{indent_str}    Label: {self.label}\n{indent_str})'