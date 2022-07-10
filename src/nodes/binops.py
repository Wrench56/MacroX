from nodes import bases
from utils import logger

class BinaryOperations(bases.BaseNode):
    KIND = 'BinaryOperationsNode'
    def __init__(self, op, left, right) -> None:
        self.op = op
        self.left = left
        self.right = right

        self.return_type = None
        self.KIND = f'{self.op}Node'
    
    def set_ret_type(self, type): # return value is converted (right side type)
        if self.return_type is None:
            self.return_type = type

    def conv_num(self, num) -> int|str|float|None:
        if isinstance(num, bases.Node):
            return self.conv_num(num.evaluate())
        elif isinstance(num, int):
            self.set_ret_type(10)
            return num
        elif isinstance(num, float):
            self.set_ret_type()
            return num
        elif num.startswith('0x'):
            self.set_ret_type(16)
            return int(num, base=16)
        elif num.startswith('0b'):
            self.set_ret_type(2)
            return int(num.replace('0b', '', 1), base=2)
        elif isinstance(num, str) and num.startswith('"') and num.endswith('"'):
            return num[1:-1]
        elif isinstance(num, str):
            try:
                num = int(num)
                self.set_ret_type(10)
            except:
                self.set_ret_type(0)
                if self.op != 'Add' and self.op != 'Times':
                    logger.error(f'Can\'t use operation {self.op} on string!')
            return num
        else:
            logger.error(f'Did not recognize the following value: {num}')

    def evaluate(self):
        is_string = False
        is_num = False

        # Convert numbers here, since it needs evaluation!
        right = self.conv_num(self.identifier_to_value(self.right))
        left = self.conv_num(self.identifier_to_value(self.left))

        if isinstance(right, str):
            is_string = True
        elif isinstance(right, int):
            is_num = True
        else:
            logger.error(f'Can\'t use {self.op} operation on {right}')
        
        if isinstance(left, str):
            if is_num:
                logger.error(f'Can\'t add string and number!')   
        else:
            if is_string:
                logger.error(f'Can\'t add number and string!')
            
        if self.op == 'Add':
            if is_num:
                return self.conv_return((left + right))
            else:
                return left + right

        if self.op == 'Minus':
            if is_num:
                return self.conv_return((left - right))
                
            else:
                logger.error(f'Can\'t use operation minus on strings!')
            
        if self.op == 'Times':
            if is_num:
                return self.conv_return((left * right))
            else:
                return left * right # multiply strings, just like in python ('A'*10)
            
        if self.op == 'Divide':
            if is_num:
                res = left / right
                return res
            else:
                logger.error(f'Can\'t use operation division on strings!')
            
    def conv_return(self, val):
        if self.return_type == 16:
            return hex(val)
        elif self.return_type == 2:
            return bin(val)
        else:
            return val