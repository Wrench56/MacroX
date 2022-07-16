from utils import logger
from tokens import base_token

class Command():
    arg_parse_list = []
    def __init__(self, args) -> None:
        self.args = args
        self.counter = 0
        self.star_parsed = None

    def get_parse_list(self):
        return self.arg_parse_list

    def parse_star(self):
        if self.arg_parse_list[0] == '*':
            return_list = []
            for arg in self.args.keys():
                if isinstance(arg, int):
                    return_list.append(self.args[arg])
                else:
                    break
            self.counter += 1
            self.star_parsed = True
            return return_list
        else:
            self.star_parsed = False

    def parse_argument(self):
        if self.star_parsed is None:
            ret = self.parse_star()
            if ret is not None:
                return ret

        arg = self.args.get(self.arg_parse_list[self.counter])
        if not arg and not self.star_parsed:
            arg = self.args.get(self.counter)
        if not arg:
            arg = None
        self.counter += 1

        return arg

            