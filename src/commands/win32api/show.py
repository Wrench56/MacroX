from utils import logger
from commands.base_command import Command
import win32con
import win32gui

class Show(Command):
    arg_parse_list = ['hwnd']
    def __init__(self, args) -> None:
        super().__init__(args)

    def evaluate(self):
        hwnd = self.parse_argument()

        if not isinstance(hwnd, int):
            logger.error('You did not pass a hwnd value!', command='show')
        
        win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL) #! This does not always work
        
