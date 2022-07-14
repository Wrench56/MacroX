from nodes import bases
from utils import logger
from globals import Importer

class CallNode(bases.Node):
    KIND = 'CallNode'
    def __init__(self, command: str, arguments: list) -> None:
        self.command = command[1:]
        self.arguments = arguments

        self.check_sequence()

    def evaluate(self):
        args_dict = self.create_dict(self.arguments)
        command_object = Importer.get_command(self.command)(args_dict)
        ret = command_object.evaluate()

        return ret 


    def create_dict(self, args: list):
        ret_dict = {}
        counter = 0
        skip_flag = False

        for i, token in enumerate(args):
            if skip_flag:
                skip_flag = False
                continue
            if token.token == 'KeywordArgument':
                ret_dict[token.part.split(' ')[0]] = self.identifier_to_value(args[i+1].part)
                skip_flag = True
            else:
                val = self.identifier_to_value(token.part)
                ret_dict[counter] = val
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
