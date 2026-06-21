import Pyro4
import Pyro4.errors

try:
    calculator = Pyro4.Proxy("PYRONAME:example.calculator")
    
    # Test valid division
    result = calculator.divide(10, 2)
    print(f"10 / 2 = {result}")
    
    # Test divide by zero - this will raise an exception
    try:
        result = calculator.divide(10, 0)
        print(f"10 / 0 = {result}")
    except ValueError as e:
        print(f"Error caught: {e}")
    
    # Test non-existent method
    try:
        result = calculator.multiply(5, 3)
    except Pyro4.errors.ProtocolError as e:
        print(f"Method not found error: {e}")
        
except Pyro4.errors.CommunicationError:
    print("Server is down! Please check if server is running.")
