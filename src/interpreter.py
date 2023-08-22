from utils import prettyprint, options
import tokenizer
import parser
class Interpreter():
    def __init__(self, path: str) -> None:
        self.path = path

    def start(self):
        tokens = self.tokenize(self.path)
        
        # Print tokens when verbose is enabled
        if options.options.verbose:
            prettyprint.print_tokens(tokens)
            print()

        root = self.parse(tokens)
        
        # Print parsed tree when verbose is enabled
        if options.options.verbose:
            print(root)
            print(f'\n{30 * "="} [Starting] {30 * "="}\n')

        root.evaluate()

    def tokenize(self, path):
        Tokenizer = tokenizer.Tokenizer()
        return Tokenizer.tokenize(path=path)

    def parse(self, tokens):
        Parser = parser.Parser(tokens)
        return Parser.parse()


