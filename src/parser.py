import nodes
from utils import logger

class Parser():
    SEARCH_FORS = {
        'Add': nodes.BinaryOperations,
        'Minus': nodes.BinaryOperations,
        'Times': nodes.BinaryOperations,
        'Divide': nodes.BinaryOperations,
        'Assign': nodes.AssignNode
    }

    def __init__(self, tokens) -> None:
        self.tokens = tokens

    def parse(self) -> list: # Just sort tokens by priority. Then just parse normally without any complication
        nodes = []

        self.tokens = self.sort_tokens(self.tokens)
        if not self.sanity_check(self.tokens):
            logger.error('Parser\'s sanity check failed!')

        prev_i = 0
        for i, token in enumerate(self.tokens):
            if token.token == 'Newline':
                nodes.append(self.next_node(self.tokens[prev_i:i]))
                prev_i = i
        
        return nodes

    def next_node(self, remaining_tokens: list) -> nodes.BaseNode:
        print(remaining_tokens)
        for i, token in enumerate(remaining_tokens):
            for sftoken in self.SEARCH_FORS:
                if token.token is sftoken:
                    if i+1 != 2:
                        logger.error(f'Unknown operation, the parser missed something at line: {remaining_tokens}')

                    node = self.SEARCH_FORS[sftoken]
                    
                    op = token.token
                    left = remaining_tokens[i-1].part

                    if len(remaining_tokens[i+1:]) > 1: # Should be [2:] tbh (and the next line)
                        right = self.next_node(remaining_tokens[i+1:]) # 1.: right, 2.: operation, ... etc.
                    else:
                        right = remaining_tokens[2].part

                    return node(op, left, right) # Returns a non-evaluated node object
        

    def sort_tokens(self, token_list: list) -> list: # TODO: Finish this!!
        return token_list
    
    def sanity_check(self, tokens) -> bool: # TODO: Finish this!!
        return True
