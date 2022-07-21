from multiprocessing.dummy.connection import families
from nodes import bases
from tokens import base_token
from utils import logger
import globals
import threading

class InterruptNode(bases.InstructionNode):
    KIND = 'InterruptNode'
    def __init__(self, label, condition, int_type) -> None:
        self.label = label[1:] #! Since first char is "~"!
        self.condition = condition

        self.int_type = int_type

        self.sync_int = False
        self.queued_int = True
        self.thread = None
        self.kill = False

        self.parse_interrupt_type()
        
    def evaluate(self, ignore_int = False):
        super().evaluate(ignore_int)
        if self.thread is None:
            logger.info('Starting condition checker thread...')
            self.thread = threading.Thread(target=self.check_condition)
            self.thread.start()

    def check_condition(self):
        while not self.kill:
            #for thread in threading.enumerate(): 
            #    logger.info(thread.name)
            if isinstance(self.condition, bases.Node):
                value = self.condition.evaluate()
            elif isinstance(self.condition, base_token.Token):
                if self.condition.token == 'Identifier':
                    value = globals.VH.get(self.condition.part)
                #elif self.condition.token == 'Label':
                #    value = globals.JH.jump(self.condition.part)
                elif self.condition.token == 'Boolean':
                    value = self.condition
            else:
                logger.error(f'Condition type was not recognized. The condition was: {self.condition}')
            
            if value is True:
                if not self.sync_int:
                    globals.interrupt = True
                
                if self.queued_int:
                    globals.IQ.add(self.label)
                else:
                    logger.info('Threading...')
                    label_obj = globals.JH.get(self.label)
                    interrupt_label_thread = threading.Thread(target=label_obj.evaluate, kwargs={'jump': True, 'ignore_int': True}).start()
                    globals.IQ.add_thread(interrupt_label_thread)
            
    def parse_interrupt_type(self):
        for char in self.int_type:
            if char == 's': # Synchronized-Interrupt
                self.sync_int = True
            elif char == 'q': # Queued-Interrupt
                self.queued_int = True
            elif char == 'i':
                break
