from globals import VH, IQ
import time

class Node():
    KIND = 'Node'
    def __init__(self) -> None:
        pass

    def identifier_to_value(self, ast):
        if isinstance(ast, str):
            if ast.startswith('$'):
                return VH.get(ast)

        return ast

    def evaluate(self):
        #! Write a less painful script here!
        while IQ.interrupt:
            time.sleep(0.00000000001)

    def __repr__(self) -> str:
        return self.prettyprint(0)

    def __str__(self) -> str:
        return self.__repr__()

class ForkNode(Node):
    KIND = 'ForkNode'
    _pp_left = 'left'
    _pp_right = 'right'
    def __init__(self):
        pass

    def prettyprint(self, indent: int) -> str:
        indent_str = ' '*indent
        left = self.left

        right = self.right
        if isinstance(right, ForkNode):
            right = right.prettyprint(indent=(indent+4))


        return f'{self.KIND} (\n{indent_str}    {self._pp_left}: {left}\n{indent_str}    {self._pp_right}: {right}\n{indent_str})'
    

class BlockNode(Node):
    KIND = 'BlockNode'
    def __init__(self) -> None:
        self.body = []

    def set_body(self, body: list[Node]):
        self.body = body.copy()

    def prettyprint(self, indent):
        indent_str = ' '*indent
        body_str = ''
        for node in self.body:
            body_str += node.prettyprint(indent=indent+4)

        return f'{self.KIND} (\n{indent_str}    Body: {body_str}\n{indent_str})'

class InstructionNode(Node):
    def __init__(self) -> None:
        pass

    def prettyprint(self, indent) -> str:
        return f'{self.KIND}()'