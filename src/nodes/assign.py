from nodes import bases
from globals import VH

class AssignNode(bases.BaseNode):
    KIND = 'AssignNode'
    _pp_left = 'target'

    def __init__(self, _, target, right) -> None:
        self.left, self.target = target, target
        self.right = right

    def evaluate(self):
        self.right = self.identifier_to_value(self.right)

        if isinstance(self.right, bases.BaseNode):
            self.right = self.right.evaluate()
        
        if self.target.startswith('$'): # variable
            self.set_variable(self.target, self.right)
        else:
            self.set_global_argument(self.target, self.right)


    def set_variable(self, target, value):
        VH.set(target, value) # VH => VariableHandlers
        print(VH.variables)
    def set_global_argument(self, target, value):
        print(f'Set global argument {target}: {value}')