from nodes import bases
import globals

class ImportNode(bases.InstructionNode):
    KIND = 'ImportNode'
    def __init__(self, module) -> None:
        self.module = module

    def evaluate(self, ignore_int = False):
        super().evaluate(ignore_int)
        globals.Importer.import_module(f'commands/{self.module}')