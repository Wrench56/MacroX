from utils import variable_handler, jump_handler, importer, global_argument_handler

VH = variable_handler.VariableHandler()
JH = jump_handler.JumpHandler()
GAH = global_argument_handler.GlobalArgumentHandler(vh=VH)
Importer = importer.Importer()

break_bool = False