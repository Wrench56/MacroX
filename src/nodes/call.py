from nodes import bases
from utils import logger

class CallNode(bases.Node):
    KIND = 'CallNode'
    def __init__(self, command: str, arguments: list) -> None:
        self.command = command[1:]
        self.arguments = arguments

        self.check_sequence()

    def evaluate(self):
        args_dict = self.create_dict(self.arguments)
        


    def create_dict(self, args: list):
        ret_dict = {}
        counter = 0
        skip_flag = False

        for i, token in enumerate(args):
            if skip_flag:
                skip_flag = False
                continue
            if token.token == 'KeywordArgument':
                ret_dict[token.part.split(' ')[0]] = args[i+1]
                skip_flag = True
            else:
                ret_dict[counter] = token.part
                counter += 1

        return ret_dict


    def check_sequence(self):
        key_argument_flag = False
        skip_flag = False

        for token in self.arguments:
            if skip_flag:
                skip_flag = False
                continue
            if token.token == 'KeywordArgument':
                skip_flag = True
                key_argument_flag = True
            else:
                if key_argument_flag:
                    logger.error('You tried to use a regular argument after a keyword argument! That\'s a no go!')
    
    def prettyprint(self, indent):
        indent_str = ' '*indent

        return f'{self.KIND} (\n{indent_str}    Command: {self.command}\n{indent_str}    Arguments: {self.arguments}\n{indent_str})'
