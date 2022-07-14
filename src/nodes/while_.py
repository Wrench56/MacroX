from nodes import bases
from utils import logger
import globals
import time

class WhileNode(bases.BlockNode):
    KIND = 'WhileNode'

    EMPTY_SLEEP = 0.01

    def __init__(self, condition):
        self.condition = condition

        self.body = None
    
    def evaluate(self):
        if self.body == None:
            logger.warning('While\'s body is empty!')
            while True:
                time.sleep(self.EMPTY_SLEEP) # Save the processor! :)

        while self.body and not globals.break_bool:
            if not self.check_condition():
                break

            for node in self.body:
                node.evaluate()
                if globals.break_bool:
                    break
        

    def check_condition(self) -> bool:
        if isinstance(self.condition, bases.Node):
            cond = self.condition.evaluate()
            if cond == True:
                return True
            
        else:
            self.condition = self.identifier_to_value(self.condition)
            cond = self.str_to_bool(self.condition)
            if cond == True:
                return True
        
        return False

    def set_body(self, body):
        self.body = body.copy()

    def prettyprint(self, indent):
        indent_str = ' '*indent
        condition = self.condition
        if isinstance(condition, bases.ForkNode):
            condition = condition.prettyprint(indent=(indent+4))

        body_str = ''
        body = self.body
        if isinstance(body, list):
            for node in body:
                body_str += node.prettyprint(indent=indent+4)

        return f'{self.KIND} (\n{indent_str}    Condition: {condition}\n{indent_str}    Body: {body_str}\n{indent_str})'