import interpreter
import keyboard
from utils import terminate

keyboard.add_hotkey('ctrl+q', terminate.terminate_by_hand)
 
Interpreter = interpreter.Interpreter(path='C:\\Users\\Mark\\Documents\\macrox\\sample\\interrupts.mox')
Interpreter.start()