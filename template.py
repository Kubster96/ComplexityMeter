from random import randint
import time

class Template:

    table = []
    n = 0

    def init(self, n):
        self.n = n
        for i in range(0, n):
            self.table.append(randint(0, 100))

    def function(self):
        time.sleep(0.00000000000000001)

    def clean_up(self):
        self.table = []
