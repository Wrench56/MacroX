from utils import logger
from commands.base_command import Command
import win32con
import win32gui

class Close(Command):
    arg_parse_list = ['hwnd']
    def __init__(self, args) -> None:
        super().__init__(args)

    def evaluate(self):
        hwnd = self.parse_argument()
        if not isinstance(hwnd, int):
            logger.error('You did not pass a hwnd value!', command='close')
            
        win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)

