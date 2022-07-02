import os
from pydoc import importfile  

class Importer():
    def __init__(self, path: str) -> None:
        self.path = path
    
    def import_commands(self) -> dict:
        commands = {}
        for file_ in self.scan_dir(self.path):
            file_= file_.replace('//', '/').replace('\\', '/')
            module = importfile(os.getcwd() + '/' + file_)

            commands[(file_.split('/')[-1].replace('.py', ''))] = module

        return commands

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
