from utils import logger
from commands.base_command import Command

class Print(Command):
    arg_parse_list = ['*', 'sep', 'end']
    def __init__(self, args) -> None:
        super().__init__(args)

    def evaluate(self):
        print_list = self.parse_argument()
        sep = self.parse_argument()
        if sep is None:
            sep = ''
        end = self.parse_argument()
        if end is None:
            end = '\n'

        print(*print_list, sep=sep, end=end)