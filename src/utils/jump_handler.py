from utils import logger

class JumpHandler():
    def __init__(self) -> None:
        self.jumps = {}

    def setup_jump(self, label, node):
        self.jumps[label[1:-1]] = node

    def jump(self, label):
        if label in self.jumps.keys():
            return self.jumps[label].evaluate(jump=True)
        else:
            logger.error(f'Jump label {label} does not exist, but you tried to jump to there!')
    
    def get(self, label) -> object:
        if label in self.jumps.keys():
            return self.jumps[label]
        else:
            logger.error(f'Jump label {label} does not exist, but you tried to access it!')