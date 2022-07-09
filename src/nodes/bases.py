from globals import VH

class BaseNode():
    KIND = 'BaseNode'
    _pp_left = 'left'
    _pp_right = 'right'
    def __init__(self):
        pass
    
    def __repr__(self) -> str:
        return self.prettyprint(0)
    
    def evaluate(self):
        pass

    def prettyprint(self, indent: int) -> str:
        indent_str = ' '*indent
        left = self.left

        right = self.right
        if isinstance(right, BaseNode):
            right = right.prettyprint(indent=(indent+4))


        return f'{self.KIND} (\n{indent_str}    {self._pp_left}: {left}\n{indent_str}    {self._pp_right}: {right}\n{indent_str})'

    def identifier_to_value(self, ast):
        if isinstance(ast, str):
            if ast.startswith('$'):
                return VH.get(ast)

        return ast
    

