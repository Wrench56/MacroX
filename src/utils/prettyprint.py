def print_tokens(tokens: list):
    padding = 0
    for token in tokens:
        if len(token.token) > padding:
            padding = len(token.token)
        

    for i, token in enumerate(tokens):
        print(f'{str(i).rjust(len(str(len(tokens))))}: {token.token.ljust(padding)} {token.part}')