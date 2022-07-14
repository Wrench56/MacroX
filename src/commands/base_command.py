from utils import logger
from tokens import base_token

class Command():
    arg_parse_list = []
    def __init__(self, args) -> None:
        self.args = args
        self.counter = 0

    def get_parse_list(self):
        return self.arg_parse_list

    def parse_argument(self):
            arg = self.args.get(self.arg_parse_list[self.counter])
            if not arg:
                arg = self.args.get(self.counter)
            if not arg:
                arg = None
            self.counter += 1

            return arg
            