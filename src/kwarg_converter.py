import logger

def convert(command: str) -> dict:

    STRING = False
    KEY = True

    key_string = ""
    value_string = ""
    s_counter = 0
    i = 0

    kwargs = {}

    for char in command:
        i += 1
        if char == '"':
            if STRING:
                STRING = False
            else:
                STRING = True
            continue
        if char == "=" and not STRING:
            KEY = False
            continue
        
        if char != " ":
            if KEY:
                key_string += char
            else: 
                value_string += char

        if i == len(command):
            if STRING:
                # auto-close with warning!
                logger.warning('Did not find a closing ". Auto-placed one. This can lead to bugs...')
                logger.warning(f'The command causing the error: {command}')
            STRING = False
            char = " "


        if char == " " and not STRING:
            if not KEY:
                kwargs[key_string] = value_string
                value_string = ""
            else:
                kwargs[s_counter] = key_string
                s_counter += 1

            key_string = ""
            
            KEY = True
            continue
        
        
    
    return kwargs