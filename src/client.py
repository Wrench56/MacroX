import interpreter
import keyboard
from utils import terminate, debugger

keyboard.add_hotkey('ctrl+q', terminate.terminate_by_hand)
keyboard.add_hotkey('ctrl+t', debugger.print_threads)
 
Interpreter = interpreter.Interpreter(path='C:\\Users\\Mark\\Documents\\macrox\\sample\\interrupts.mox')
Interpreter.start()