from textwrap import indent
from utils import logger
from nodes import bases

class IfNode(bases.Node):
    KIND = 'IfNode'
    def __init__(self, condition):
        self.condition = condition

        self.if_body = None
        self.else_body = None

    def evaluate(self):
        pass
    
    def set_body(self, body: list[bases.Node]|bases.Node):
        if isinstance(body, list):
            if self.if_body == None:
                self.if_body = body.copy()
            else:
                self.else_body = body.copy()
        elif isinstance(body, IfNode):
            if self.if_body != None:
                self.else_body = body
            else:
                logger.error('Unknown error')

    def __repr__(self) -> str:
        return self.prettyprint(0)

    def prettyprint(self, indent):
        indent_str = ' '*indent
        condition = self.condition
        if isinstance(condition, bases.BaseNode):
            condition = condition.prettyprint(indent=(indent+4))



        return f'{self.KIND} (\n{indent_str}    Condition: {condition}\n{indent_str}    If-Body: {self.pprint_body(self.if_body, indent)}\n{indent_str}    Else-Body: {self.pprint_body(self.else_body, indent)}\n{indent_str})'

    def pprint_body(self, body, indent: int) -> str:
        ret_str = ''
        if isinstance(body, list):
            for node in body:
                ret_str += node.prettyprint(indent=indent+4)
        elif isinstance(body, IfNode):
            ret_str += body.prettyprint(indent=indent+4)
        
        return ret_str