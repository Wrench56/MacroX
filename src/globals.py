from utils import variable_handler, jump_handler, importer, global_argument_handler

VH = variable_handler.VariableHandler()
JH = jump_handler.JumpHandler()
GAH = global_argument_handler.GlobalArgumentHandler(vh=VH)
Importer = importer.Importer()
Importer.import_module('commands/win32api')
Importer.import_module('commands/io')
Importer.import_module('commands/time')
Importer.import_module('commands/directx')

break_bool = False