from utils import logger
from commands.base_command import Command
import time
class Sleep(Command):
    arg_parse_list = ['ms']
    def __init__(self, args) -> None:
        super().__init__(args)

    def evaluate(self):
        ms = self.parse_argument()

        if not isinstance(ms, int):
            logger.error('Invalid millisecond value!', command='sleep')
        
        time.sleep(ms/1000)
        
