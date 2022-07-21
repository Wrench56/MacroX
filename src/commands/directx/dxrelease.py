from commands.lib import parse_char
from utils import logger
from commands.base_command import Command
from commands.directx.lib import funcs

class Dxrelease(Command):
    arg_parse_list = ['char']
    def __init__(self, args) -> None:
        super().__init__(args)
    
    def evaluate(self):
        char = self.parse_argument()

        if not isinstance(char, str):
            logger.warning(f'The passed send value "{char}" is not a string! Auto-converting to string!', command='dxrelease')
            try:
                char = str(char)
            except:
                logger.error('Could not convert non-string value to string!', command='dxrelease')

        char_ = parse_char.string2directx(char)[0] #! This will release only 1 key!
        funcs.releaseKey(char_)
