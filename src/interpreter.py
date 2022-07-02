from utils.kwarg_converter import convert

class Interpreter():
    def __init__(self, commands: dict) -> None:
        self.commands = commands

    def execute(self, command):
        parsed = convert(command=command)
        print(parsed)
        command = parsed.get(0)

        if command == None: # Empty line
            return True
        
        command = command.lower()
        if command in self.commands.keys():
            module = self.commands[command]
            obj = getattr(module, command.capitalize())
            obj.execute(parsed)




