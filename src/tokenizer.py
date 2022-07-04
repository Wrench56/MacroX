import re
import utils.logger
import tokens.base_token as base_token

class Tokenizer():
    ASSIGN = ':'
    TOKEN_TYPES = {
        'Identifier': '^\$[a-zA-Z]*',
        'GlobalArgument': '^\%[a-zA-Z_]*',
        'Assign': '^:',
        'DecimalNumber': '^[0-9](?![xb])',
        'HexNumber': '^0x[0-9ABCDEFabcdef]',
        'BinaryNumber': '^0b[01]',
        'String': '^"[a-zA-Z_]*"',
        'Boolean': '^false|true',
        'Add': '^\+(?![+])',
        'Minus': '^\-(?![-])',
        'Times': '^\*(?![*])',
        'Divide': '^\/(?![/])',
        'Modulo': '^\%(?![a-zA-Z0-9_])',
        'OpenCurlyBracket': '^\{',
        'CloseCurlyBracket': '^\}',
        'OpenBracket': '^\(',
        'CloseBracket': '^\)',
        'Label': '^\[[a-zA-Z0-9_]*\]',
        'If': '^if(?![$\w])',
        'While': '^while(?![$\w])'
    }
    
              

    def __init__(self) -> None:
        pass

    def read(self, path) -> list:
        with open(path, 'r', encoding='utf-8') as file:
            lst = file.readlines()
        return lst


    def tokenize(self, script=None, path=None) -> list[base_token.Token]:
        if path is not None:
            script = self.read(path)
        elif script is not None:
            script = script
        else:
            utils.logger.error('Nothing to tokenize!')

        tokens = []
        token_types = dict((v, k) for k, v in self.TOKEN_TYPES.items()) # flip dictionary

        for line in script:
            line = line.strip()
            if line == '': # Empty line, easy case
                continue
            
            if line.startswith('//'): # Comment
                continue
            
            print(f'New Line: {line}')
            while line != '':
                line = line.strip()
                for token_type in token_types.keys():
                    res = re.match(token_type, line)
                    if res:
                        tokens.append(base_token.Token(token_types[token_type], res.group(0)))
                        line = line[len(res.group(0)):].strip()
        return tokens



