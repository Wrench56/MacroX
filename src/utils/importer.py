import os
from pydoc import importfile
from utils import logger

class Importer():
    def __init__(self) -> None:
        self.commands = {}
    
    def import_module(self, path):
        for file_ in self.scan_dir(path):
            file_= file_.replace('//', '/').replace('\\', '/')
            module = importfile(os.getcwd() + '/' + file_)
            module_name = file_.split('/')[-1].replace('.py', '')
            if not module_name in self.commands.keys():
                self.commands[module_name] = module
            else:
                logger.error(f'Same named command already imported! (Module name: {module_name})')
    
    def get_command(self, command_name):
        if command_name in self.commands.keys():
            return self.commands[command_name]
        else:
            logger.error(f'No such command: {command_name}')

    def scan_dir(self, path: str):
        with os.scandir(path) as it:
            for entry in it:
                if entry.is_file():
                    if entry.name.endswith(".py"):
                        yield entry.path
                    else:
                        pass # For now
                else:
                    #symlink or dir
                    if entry.is_dir():
                        return self.scan_dir((path+'/'+entry.name).replace('//', '/'))
                    else:
                        #! Symlink
                        pass
