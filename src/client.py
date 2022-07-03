import importer
import interpreter

Importer = importer.Importer('commands')
commands = Importer.import_commands()

Interpreter = interpreter.Interpreter(commands = commands)
Interpreter.execute('WINDOW name="\"Hello World"')