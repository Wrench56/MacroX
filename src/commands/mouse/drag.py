import mouse
from utils import logger
from commands.base_command import Command

class Drag(Command):
    arg_parse_list = ['x', 'y', 'duration']
    def __init__(self, args) -> None:
        super().__init__(args)
    
    def evaluate(self):
        x = self.parse_argument()
        y = self.parse_argument()
        d = self.parse_argument()
        if d is None:
            d = 0.1

        mouse.drag(0, 0, x, y, absolute=False, duration=d)
