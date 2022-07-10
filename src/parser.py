import nodes
from utils import logger
from tokens.base_token import Token

class Parser():
    SEARCH_FORS = {
        'Add': nodes.BinaryOperations,
        'Minus': nodes.BinaryOperations,
        'Times': nodes.BinaryOperations,
        'Divide': nodes.BinaryOperations,
        'Assign': nodes.AssignNode,
        'Equals': nodes.LogicalOperations,
        'NotEquals': nodes.LogicalOperations,
        'Greater': nodes.LogicalOperations,
        'Less': nodes.LogicalOperations,
        'GreaterEquals': nodes.LogicalOperations,
        'LessEquals': nodes.LogicalOperations,
        'While': nodes.WhileNode,
        'If': nodes.IfNode,
        'ElseIf': nodes.IfNode,
        'Else': None,
        'OpenCurlyBracket': None,
        'CloseCurlyBracket': None,
        'Break': nodes.BreakNode

    }

    def __init__(self, tokens) -> None:
        self.tokens = tokens

        self.body_flag = False
        self.block_ptr = None

    def parse(self) -> list: # Just sort tokens by priority. Then just parse normally without any complication
        nodes = []
        body = []

        self.tokens = self.preprocess(self.tokens)
        prev_i = 0
        for i, token in enumerate(self.tokens):
            if token.token == 'Newline':
                node = self.next_node(self.tokens[prev_i:i])
                if node != None:
                    if not self.body_flag:
                        nodes.append(node)
                    else:
                        body.append(node)
                if body != [] and not self.body_flag: # add to ptr
                    self.block_ptr.set_body(body)
                    body.clear()

                prev_i = i+1

        return nodes

    def next_node(self, remaining_tokens: list) -> nodes.BaseNode:
        for i, token in enumerate(remaining_tokens):
            for sftoken in self.SEARCH_FORS:
                if token.token is sftoken:  
                    if sftoken in ['If', 'While', 'ElseIf']:
                        if len(remaining_tokens[1:]) > 1:
                            cond = self.next_node(remaining_tokens[1:])
                        else:
                            cond = remaining_tokens[1].part

                        node = self.SEARCH_FORS[sftoken](cond)
                        if sftoken == 'ElseIf':
                            self.block_ptr.set_body(node) # ! IfNode.set_body() should automatically adjust the if-body and else-body (once if-body fills up, switch to else-body) 
                        self.block_ptr = node
                        if sftoken == 'ElseIf':
                            node = None # We don't want to see this in the regular nodes list!

                        return node
                    elif sftoken == 'Else': # I should do bug-checks here
                        pass
                    elif sftoken == 'OpenCurlyBracket':
                        self.body_flag = True
                        return None
                    elif sftoken == 'CloseCurlyBracket':
                        self.body_flag = False
                        return None
                    elif sftoken == 'Break':
                        return nodes.BreakNode()
                    else:
                        if i+1 > 2:
                            logger.error(f'Unknown operation, the parser missed something at line: {remaining_tokens}')

                        node = self.SEARCH_FORS[sftoken]
                        
                        op = token.token
                        left = remaining_tokens[i-1].part

                        if len(remaining_tokens[i+1:]) > 1:
                            right = self.next_node(remaining_tokens[i+1:]) # 1.: right, 2.: operation, ... etc.
                        else:
                            right = remaining_tokens[2].part

                        return node(op, left, right) # Returns a non-evaluated node object

    def preprocess(self, tokens):
        tokens = self.sort_tokens(tokens)
        if not self.sanity_check(tokens):
            logger.error('Parser\'s sanity check failed!')
        
        ret_tokens = []
        for i, token in enumerate(tokens):
            if token.token == 'OpenCurlyBracket':
                ret_tokens.append(Token('Newline', '\\n'))
                ret_tokens.append(token)
                ret_tokens.append(Token('Newline', '\\n'))
                
            elif token.token == 'CloseCurlyBracket':
                ret_tokens.append(Token('Newline', '\\n'))
                ret_tokens.append(token)
                ret_tokens.append(Token('Newline', '\\n'))
            else:
                ret_tokens.append(token)

        return ret_tokens

    def sort_tokens(self, token_list: list) -> list: # TODO: Finish this!!
        return token_list
    
    def sanity_check(self, tokens) -> bool: # TODO: Finish this!!
        return True
