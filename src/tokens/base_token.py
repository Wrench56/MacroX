class Token():
    def __init__(self, token_type, part):
        self.token = token_type
        
        if token_type == 'DecimalNumber':
            self.part = int(part)
        else:
            self.part = part

    def __repr__(self) -> str:
        if self.token:
            return f"Token <{self.token}> <{self.part}>"
        else:
            return "Token <NONE> <NONE>"
        
    def __str__(self) -> str:
        return self.__repr__()

    
