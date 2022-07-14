from utils import logger
from commands.base_command import Command
import win32gui

class Window(Command):
    arg_parse_list = ['mname', 'sname']
    def __init__(self, args: dict):
        super().__init__(args)

    def evaluate(self):
        mname = self.parse_argument()
        sname = self.parse_argument()
        if mname is None and sname is None:
            logger.error('No window name specified', command='window')

        hwnd = win32gui.FindWindow(mname, sname)
        if hwnd == 0:
            logger.warning('The window handler is null. That means the window was not found.', command='window')

        return hwnd




