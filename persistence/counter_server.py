import Pyro4
import os

@Pyro4.expose
class CounterService:
    def __init__(self):
        self.count = self.load_count()
    
    def load_count(self):
        try:
            with open('counter.txt', 'r') as f:
                return int(f.read())
        except:
            return 0
    
    def save_count(self):
        with open('counter.txt', 'w') as f:
            f.write(str(self.count))
    
    def increment(self):
        self.count += 1
        self.save_count()
        return self.count
    
    def getCount(self):
        return self.count

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
ns.register("example.counter", daemon.register(CounterService))
print("Counter server ready...")
daemon.requestLoop()
