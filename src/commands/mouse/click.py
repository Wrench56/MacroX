import mouse
from utils import logger
from commands.base_command import Command

class Click(Command):
    arg_parse_list = ['click_type']
    def __init__(self, args) -> None:
        super().__init__(args)
    
    def evaluate(self):
        click = self.parse_argument()
        if click not in ['left', 'right', 'middle']:
            logger.error(f'Unknown click type {click}!', command='click')

        mouse.click(click)
