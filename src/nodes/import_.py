from nodes import bases
import globals

class ImportNode(bases.InstructionNode):
    KIND = 'ImportNode'
    def __init__(self, module) -> None:
        self.module = module

    def evaluate(self):
        super().evaluate()
        globals.Importer.import_module(f'commands/{self.module}')