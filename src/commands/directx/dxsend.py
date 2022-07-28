from commands.lib import parse_char
from utils import logger
from commands.base_command import Command
from commands.directx.lib import funcs

import time

class Dxsend(Command):
    arg_parse_list = ['string', 'auto_cap']
    DELAY = 0.0005
    def __init__(self, args) -> None:
        super().__init__(args)
    
    def evaluate(self):
        string = self.parse_argument()
        auto_cap = self.parse_argument()
        if auto_cap is None:
            auto_cap = True

        if not isinstance(string, str):
            logger.warning(f'The passed send value "{string}" is not a string! Auto-converting to string!', command='dxsend')
            try:
                string = str(string)
            except:
                logger.error('Could not convert non-string value to string!', command='dxsend')


        for char in parse_char.string2directx(string, auto_cap=auto_cap):
            if auto_cap and char > 1000:
                char = char - 1000
                funcs.pressKey(42)
                funcs.pressKey(char)
                funcs.releaseKey(42)
            else:
                funcs.pressKey(char)
            
            time.sleep(self.DELAY)
            funcs.releaseKey(char)
