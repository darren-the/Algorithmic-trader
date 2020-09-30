from tqdm import tqdm
from math import floor

class PBar:
    '''
    A class for displaying progress bars using tqdm.
    '''
    def __init__(self, length, desc=""):
        self.desc = desc
        self.length = length
        self.count = 0
        self.alive = True

    def update(self, i=1):
        if not self.alive:
            return
        if self.count == 0:
            self.pbar = tqdm(total=100)
            self.pbar.set_description(self.desc)
        nextCount = self.count + (i / self.length * 100)
        self.pbar.update(floor(nextCount) - floor(self.count))
        self.count = nextCount
        if self.count == 100:
            self.terminate()
    
    def terminate(self):
        if not self.alive or self.count == self.length:
            return
        while self.count < 100:
            try:
                self.pbar.update(1)
            except:
                pass
            self.count += 1
        self.alive = False
        try:
            self.pbar.close()
        except:
            pass