import threading
import globals
from utils import logger, debugger

class InterruptQueue():
    def __init__(self):
        self.stack = []
        self.threads = []
        self.running = False
        self.threads_running = False

        self.interrupt = False

    def add(self, label, interrupt_obj):
        self.interrupt = True
        label_obj = globals.JH.get(label)
        self.stack.append(label_obj)
        if not self.running:
            self.run_thread = threading.Thread(target=self.run, args=(interrupt_obj,))
            self.run_thread.setName('Interrupt Queue Thread')
            self.run_thread.start()

    def add_thread(self, thread, interrupt_obj):
        self.interrupt = True
        self.threads[thread] = interrupt_obj
        if not self.threads_running:
            self.check_thread = threading.Thread(target=self.check_threads)
            self.check_thread.setName('Interrupt Thread-checking Thread')
            self.check_thread.start()


    def run(self, interrupt_obj):
        self.running = True
        while True:
            if len(self.stack) == 0:
                break
            label = self.stack[0]
            label.evaluate(jump=True, ignore_int=True)
            interrupt_obj.resume()
            self.stack.pop(0)
        
        self.interrupt = False
        self.running = False

    def check_threads(self):
        self.threads_running = True
        while True:
            if len(self.threads.keys()) == 0:
                break
            for thread in self.threads.keys():
                if thread.is_alive() is False:
                    self.threads[thread].resume()
                    self.threads[thread] = None
        
        self.interrupt = False
        self.threads_running = False