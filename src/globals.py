from utils import variable_handler, jump_handler, importer

VH = variable_handler.VariableHandler()
JH = jump_handler.JumpHandler()
Importer = importer.Importer()
Importer.import_module('commands')

break_bool = False