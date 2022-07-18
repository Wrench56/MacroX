from utils import logger
from commands.base_command import Command
import win32con
import win32api

class Send(Command):
    arg_parse_list = ['hwnd', 'string']
    def __init__(self, args) -> None:
        super().__init__(args)

    def evaluate(self):
        skip_count = 0
        hwnd = self.parse_argument()
        string = self.parse_argument()

        if not isinstance(hwnd, int):
            logger.error('You did not pass a hwnd value to send command!', command='send')
        if not isinstance(string, str):
            logger.warning(f'The passed send value "{string}" is not a string! Auto-converting to string!', command='send')
            try:
                string = str(string)
            except:
                logger.error('Could not convert non-string value to string!', command='send')

        chr_ord = None
        for i, char in enumerate(string):
            if skip_count > 0:
                skip_count -= 1
                continue
            if char == '#':
                if len(string)-1 >= i+3:
                    if string[i+1] == 'E' and string[i+2] == 'S' and string[i+3] == 'C':
                        chr_ord = 27
                        skip_count = 3

            else:
                chr_ord = ord(char)
            print(chr_ord)
            win32api.PostMessage(hwnd, win32con.WM_CHAR, chr_ord, 0)