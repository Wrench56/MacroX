from pprint import PrettyPrinter
from nodes import bases

class WhileNode(bases.Node):
    KIND = 'WhileNode'
    def __init__(self, condition):
        self.condition = condition

        self.body = None
    
    def evaluate(self):
        pass

    def set_body(self, body):
        self.body = body.copy()

    def prettyprint(self, indent):
        indent_str = ' '*indent
        condition = self.condition
        if isinstance(condition, bases.BaseNode):
            condition = condition.prettyprint(indent=(indent+4))

        body_str = ''
        body = self.body
        if isinstance(body, list):
            for node in body:
                body_str += node.prettyprint(indent=indent+4)

        return f'{self.KIND} (\n{indent_str}    Condition: {condition}\n{indent_str}    Body: {body_str}\n{indent_str})'

    def __repr__(self) -> str:
        return self.prettyprint(indent=0)