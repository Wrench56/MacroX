import importer
import interpreter

Importer = importer.Importer('commands')
commands = Importer.import_commands()

Interpreter = interpreter.Interpreter(path='C:\\Users\\Mark\\Documents\\macrox\\sample\\test.mox')
Interpreter.start()