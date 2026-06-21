import Pyro4

@Pyro4.expose
class CalculatorService:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
ns.register("example.calculator", daemon.register(CalculatorService))
print("Calculator service with error handling is ready...")
daemon.requestLoop()
