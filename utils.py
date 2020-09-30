from tqdm import tqdm
from math import floor

tLength = {'1m': 60000, '5m': 300000, '15m': 900000, '30m': 1800000, '1h': 3600000, '3h': 10800000, '6h': 21600000, 
    '12h': 43200000, '1D': 86400000, '7D': 604800000, '14D': 1209600000}

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

def max_range(start, end, t, _max=10000):
    diff = int((float(end) - float(start)) / tLength[t])
    if diff > _max:
        end = float(start) + tLength[t] * _max
    return str(start), str(end)

def list_to_float(_list):
    for i in range(len(_list)):
        _list[i] = float(_list[i])

def num_candles(start, end, t):
    return round((end - start) / tLength[t])

