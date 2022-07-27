from nodes import bases
from tokens import base_token
from globals import JH
from utils import logger

class JumpNode(bases.InstructionNode):
    KIND = 'JumpNode'
    def __init__(self, label) -> None:
        self.label = label[1:] #! label[1:], since the first char is "~"

    def evaluate(self, ignore_int = False):
        super().evaluate(ignore_int)
        ret_val = JH.jump(self.label)
        if isinstance(ret_val, base_token.Token):
            return ret_val.part
        elif isinstance(ret_val, bases.Node):
            return ret_val.evaluate()
        else: #! This might cause some problems, be aware!
            return ret_val

    def prettyprint(self, indent):
        indent_str = ' '*indent
        return f'{self.KIND} (\n{indent_str}    Label: {self.label}\n{indent_str})'