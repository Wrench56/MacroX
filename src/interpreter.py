from utils.kwarg_converter import convert
from utils import prettyprint
import tokenizer
import parser
class Interpreter():
    def __init__(self, path: str) -> None:
        self.path = path

    def start(self):
        tokens = self.tokenize(self.path)
        prettyprint.print_tokens(tokens)
        print('\n'*2)

        nodes = self.parse(tokens)
        print(nodes)

    def tokenize(self, path):
        Tokenizer = tokenizer.Tokenizer()
        return Tokenizer.tokenize(path=path)

    def parse(self, tokens):
        Parser = parser.Parser(tokens)
        return Parser.parse()


