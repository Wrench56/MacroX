from utils import logger
from commands.base_command import Command
import win32con
import win32api

class Send(Command):
    arg_parse_list = ['hwnd', 'string']
    def __init__(self, args) -> None:
        super().__init__(args)

    def evaluate(self):
        hwnd = self.parse_argument()
        string = self.parse_argument()

        if not isinstance(hwnd, int):
            logger.error('You did not pass a hwnd value to send command!', command='send')
        if not isinstance(string, str):
            logger.warning('The passed send value is not a string! Auto-converting to string!', command='send')
            try:
                string = str(string)
            except:
                logger.error('Could not convert non-string value to string!', command='send')

        for char in string:
            win32api.PostMessage(hwnd, win32con.WM_CHAR, ord(char), 0)