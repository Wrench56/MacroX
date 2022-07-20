import ctypes
from commands.directx.lib import structs

#http://www.flint.jp/misc/?q=dik&lang=en

def pressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = structs.Input_I()
    ii_.ki = structs.KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = structs.Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def releaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = structs.Input_I()
    ii_.ki = structs.KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = structs.Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))