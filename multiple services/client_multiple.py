import Pyro4

try:
    # Connect to all services
    greeting = Pyro4.Proxy("PYRONAME:example.greeting")
    calculator = Pyro4.Proxy("PYRONAME:example.calculator")
    student = Pyro4.Proxy("PYRONAME:example.student")
    
    # Use services
    print(greeting.greet())
    print(f"15 + 10 = {calculator.add(15, 10)}")
    print(student.getStudent())
    
except Pyro4.errors.CommunicationError:
    print("Server not available!")
