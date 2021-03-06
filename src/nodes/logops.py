from nodes import bases
from utils import logger

class LogicalOperations(bases.ForkNode):
    KIND = 'LogicalOperationsNode'
    def __init__(self, op, left, right):
        self.op = op
        self.right = right
        self.left = left

        self.KIND = f'{self.op}Node'

    def conv_num(self, num) -> int|float|str|bool|None:
        if isinstance(num, bases.Node):
            return None
        elif isinstance(num, int):
            return num
        elif isinstance(num, float):
            return num
        elif num.startswith('0x'):
            return int(num, base=16)
        elif num.startswith('0b'):
            return int(num.replace('0b', '', 1), base=2)
        elif isinstance(num, str) and num.startswith('"') and num.endswith('"'):
            return num[1:-1]
        elif isinstance(num, str):
            if num == 'true':
                return True
            elif num == 'false':
                return False
            try:
                num = int(num)
            except:
                pass
            try:
                num = float(num)
            except:
                pass
            return num
        elif isinstance(num, bool):
            return num
        else:
            logger.error(f'Did not recognize the following value: {num}')

    def get_type(self, target) -> str:
        if isinstance(target, bool):
            return 'Bool'
        elif isinstance(target, int) or isinstance(target, float):
            return 'Num'
        elif isinstance(target, str):
            return 'String'
        


    def evaluate(self, ignore_int = False) -> bool:
        super().evaluate(ignore_int)
        left = self.conv_num(self.identifier_to_value(self.left))
        
        if isinstance(self.right, bases.Node):
            right = self.right.evaluate()
        right = self.conv_num(self.identifier_to_value(self.right))
        type_l = self.get_type(left)
        type_r = self.get_type(right)

        if type_l != type_r:
            logger.error(f'Can\'t use logical operation "{self.op}" on {type_l} and {type_r}!')

        if self.op == 'Equals':
            if left == right:
                return True
            return False

        elif self.op == 'NotEquals':
            if left != right:
                return True
            return False
        
        if type_l == 'Bool' or type_l == 'String':
            logger.error(f'Can\'t use operation {self.op} on {type_l}')


        if self.op == 'Greater':
            if left > right:
                return True
            return False

        elif self.op == 'Less':
            if left < right:
                return True
            return False
        
        elif self.op == 'GreaterEquals':
            if left >= right:
                return True
            return False
        
        elif self.op == 'LessEquals':
            if left <= right:
                return True
            return False

    