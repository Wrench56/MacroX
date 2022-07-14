from nodes import bases

class Root(bases.Node):
    KIND = 'RootNode'
    def __init__(self):
        self.body = []

    def evaluate(self):
        for node in self.body:
            node.evaluate()

    def set_body(self, body):
        self.body = body.copy()

    def prettyprint(self, _):
        body_str = ''
        if isinstance(self.body, list):
            for node in self.body:
                body_str += node.prettyprint(indent=4)

        return f'{self.KIND} (\n    Body: {body_str}\n)'