from utils import logger
from commands.base_command import Command
import win32con
import win32gui

class Child(Command):
    arg_parse_list = ['hwnd']
    def __init__(self, args) -> None:
        super().__init__(args)

    def evaluate(self):
        hwnd = self.parse_argument()
        if not isinstance(hwnd, int):
            logger.error('You did not pass a hwnd value!', command='child')

        child_hwnd = win32gui.GetWindow(hwnd, win32con.GW_CHILD)
        if child_hwnd == 0:
            logger.warning('The child handler is null. That means the child was not found.', command='child')
        return child_hwnd


