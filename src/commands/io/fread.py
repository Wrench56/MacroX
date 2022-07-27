from utils import logger
from commands.base_command import Command
from tokens import base_token

import os

class Fread(Command):
    arg_parse_list = ['filename']
    def __init__(self, args) -> None:
        super().__init__(args)
    
    def evaluate(self):
        fn = self.parse_argument()
        if not isinstance(fn, str):
            logger.error(f'Invalid filename: {fn}!', command="fread")

        if not os.path.exists(fn):
            logger.error('File does not exist!', command='fread')

        with open(fn, 'r') as file:
            content = file.read()
            file.close()
        
        return base_token.Token('String', f'"{content}"') #! f'"{content}"' cuz i strip away the first and last in case of strings!

