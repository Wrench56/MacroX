from nodes import bases
import globals

class WhileNode(bases.Node):
    KIND = 'WhileNode'
    def __init__(self, condition):
        self.condition = condition

        self.body = None
    
    def evaluate(self):
        if self.body == None:
            globals.logger.error('Unknown error: While\'s body is empty!')

        while True:
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
            cond = self.str_to_bool(self.condition)
            if cond == True:
                return True
        
        return False

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