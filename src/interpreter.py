from utils.kwarg_converter import convert
from utils import prettyprint
import tokenizer
class Interpreter():
    def __init__(self, path: str) -> None:
        self.path = path

    def start(self):
        tokens = self.tokenize()
        prettyprint.print_tokens(tokens)

        

    def tokenize(self):
        Tokenizer = tokenizer.Tokenizer()
        return Tokenizer.tokenize(path=self.path)



