from utils import logger
from commands.base_command import Command

class Input(Command):
    arg_parse_list = ['string']
    def __init__(self, args) -> None:
        super().__init__(args)
    
    def evaluate(self):
        string = self.parse_argument()
        if string is None:
            string = ''
        return input(string)
