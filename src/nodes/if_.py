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
        if isinstance(self.condition, bases.Node):
            cond = self.condition.evaluate()
            if cond == True:
                self.evaluate_body(self.if_body)
            elif cond == False:
                self.evaluate_body(self.else_body)
        else:
            cond = self.str_to_bool(self.condition)
            if cond == True:
                self.evaluate_body(self.if_body)
            elif cond == False:
                self.evaluate_body(self.else_body)
    

    def evaluate_body(self, body):
        if isinstance(body, list):
            for node in body:
                node.evaluate()
        elif isinstance(body, bases.Node):
            body.evaluate()

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