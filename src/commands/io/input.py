from utils import logger
from tokens import base_token
from commands.base_command import Command

class Input(Command):
    arg_parse_list = ['string']
    def __init__(self, args) -> None:
        super().__init__(args)
    
    def evaluate(self):
        string = self.parse_argument()
        if string is None:
            string = ''

        return base_token.Token('String', f'"{input(string)}"')
