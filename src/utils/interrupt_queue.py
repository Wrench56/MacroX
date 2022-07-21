import threading
import globals
from utils import logger

class InterruptQueue():
    def __init__(self):
        self.stack = []
        self.threads = []
        self.running = False
        self.threads_running = False

        self.interrupt = False

    def add(self, label):
        self.interrupt = True
        label_obj = globals.JH.get(label)
        self.stack.append(label_obj)
        if not self.running:
            logger.info('Starting IQ\'S run()')
            threading.Thread(target=self.run).start()

    def add_thread(self, thread):
        self.interrupt = True
        self.threads.append(thread)
        if not self.threads_running:
            threading.Thread(target=self.check_threads).start()

    def run(self):
        self.running = True
        while True:
            if len(self.stack) == 0:
                break
            label = self.stack[0]
            label.evaluate(jump=True, ignore_int=True)
            self.stack.pop(0)
            logger.info(self.stack)
        
        self.interrupt = False
        self.running = False
        logger.info('RUN FINISHED')

    def check_threads(self):
        self.threads_running = True
        while True:
            if len(self.threads) == 0:
                break
            for i, thread in enumerate(self.threads):
                if thread.is_alive() is False:
                    self.threads.pop(i)
        
        self.interrupt = False
        self.threads_running = False
        logger.info('CHECK_THREADS FINISHED')