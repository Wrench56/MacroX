class DirectXChars():
    chars = {
        'ESC': 1,
        '1': 2,
        '2': 3,
        '3': 4,
        '4': 5,
        '5': 6,
        '6': 7,
        '7': 8,
        '8': 9,
        '9': 10,
        '0': 11,
        '-': 12,
        '=': 13,
        'BCK': 14,
        'TAB': 15,
        'Q': 16,
        'W': 17,
        'E': 18,
        'R': 19,
        'T': 20,
        'Y': 21,
        'U': 22,
        'I': 23,
        'O': 24,
        'P': 25,
        '[': 26,
        ']': 27,
        'ENT': 28,
        'LCL': 29,
        'A': 30,
        'S': 31,
        'D': 32,
        'F': 33,
        'G': 34,
        'H': 35,
        'J': 36,
        'K': 37,
        'L': 38,
        ';': 39,
        '\'': 40,
        '~': 41,
        'LSH': 42,
        '\\': 43,
        'Z': 44,
        'X': 45,
        'C': 46,
        'V': 47,
        'B': 48,
        'N': 49,
        'M': 50,
        ',': 51,
        '.': 52,
        '/': 53,
        'RSH': 54,
        'NM*': 55,
        'LAT': 56,
        ' ': 57,
        'CPL': 58,
        'F1_': 59,
        'F2_': 60,
        'F3_': 61,
        'F4_': 62,
        'F5_': 63,
        'F6_': 64,
        'F7_': 65,
        'F8_': 66,
        'F9_': 67,
        'F10': 68,
        'NML': 69,
        'SCL': 70,
        'NM7': 71,
        'NM8': 72,
        'NM9': 73,
        'NM-': 74,
        'NM4': 75,
        'NM5': 76,
        'NM6': 77,
        'NM+': 78,
        'NM1': 79,
        'NM2': 80,
        'NM3': 81,
        'NM0': 82,
        'NM.': 83,
        'F11': 87,
        'F12': 88,
        'NME': 156,
        'RCR': 157,
        'NM/': 181,
        'RLT': 184,
        'HOM': 199,
        'UAR': 200,
        'PUP': 201,
        'LAR': 203,
        'RAR': 205,
        'END': 207,
        'DAR': 208,
        'PDN': 209,
        'INS': 210,
        'DEL': 211,
        'LMB': 256,
        'RMB': 257,
        'MMB': 258,
        'MB3': 259,
        'MB4': 260,
        'MB5': 261,
        'MB6': 262,
        'MB7': 263,
        'MWU': 264,
        'MWD': 265


    }

class SpecialAsciiChars():
    chars = {
        'ESC': 27,
        'TAB': 9
    }

def string2ascii(string) -> int:
    skip_count = 0
    ret_lst = []
    for i, char in enumerate(string):
        if skip_count > 0:
            skip_count -= 1
            continue
        if char == '#':
            if len(string)-1 >= i+3:
                ord_ = SpecialAsciiChars.chars.get(str(string[i+1]+string[i+2]+string[i+3]))
                if ord_:
                    skip_count = 3
                else:
                    ord_ = ord(char)
        else:
            ord_ = ord(char)

        ret_lst.append(ord_)
    
    return ret_lst

def string2directx(string, auto_cap=False):
    skip_count = 0
    ret_lst = []

    for i, char in enumerate(string):
        if skip_count > 0:
            skip_count -= 1
            continue
        if char == '#':
            if len(string)-1 >= i+3:
                ord_ = DirectXChars.chars.get(str(string[i+1].upper()+string[i+2].upper()+string[i+3].upper()))
                if ord_:
                    skip_count = 3
                else:
                    ord_ = DirectXChars.chars.get(char.upper())
                    if auto_cap and char == char.upper():
                        # MAX VALUE FOR DIRECTX KEYS: 0xDF
                        # SO I ADD 1000 FOR EVERY CHAR THAT NEEDS SHIFT!
                        ord_ += 1000

        else:
            ord_ = DirectXChars.chars.get(char.upper())
            if auto_cap and char == char.upper():
                # MAX VALUE FOR DIRECTX KEYS: 0xDF
                # SO I ADD 1000 FOR EVERY CHAR THAT NEEDS SHIFT!
                ord_ += 1000
        ret_lst.append(ord_)
    
    return ret_lst