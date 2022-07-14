from nodes import bases

class LabelNode(bases.Node):
    KIND = 'LabelNode'
    def __init__(self) -> None:
        self.body = []

    def set_body(self, body: list):
        self.body = body.copy()

    def evaluate(self, jump=False):
        if jump:
            for node in self.body:
                node.evaluate()

    def prettyprint(self, indent):
        indent_str = ' '*indent
        body_str = ''
        if isinstance(self.body, list):
            for node in self.body:
                body_str += node.prettyprint(indent=indent+4)

        return f'{self.KIND} (\n{indent_str}    Body: {body_str}\n{indent_str})'