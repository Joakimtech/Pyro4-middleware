import Pyro4

@Pyro4.expose
class GreetingService:
    def greet(self):
        return "Hello Student"

@Pyro4.expose
class CalculatorService:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

@Pyro4.expose
class StudentService:
    def getStudent(self):
        return "Student Name: Alice"

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()

# Register all services
ns.register("example.greeting", daemon.register(GreetingService))
ns.register("example.calculator", daemon.register(CalculatorService))
ns.register("example.student", daemon.register(StudentService))

print("All services are ready...")
daemon.requestLoop()
