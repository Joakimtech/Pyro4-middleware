import Pyro4
import Pyro4.errors

def test_connection(username, password):
    try:
        greeting = Pyro4.Proxy("PYRONAME:secure.greeting")
        result = greeting.say_hello("Student", username, password)
        print(f"Success with {username}: {result}")
        
        calculator = Pyro4.Proxy("PYRONAME:secure.calculator")
        calc_result = calculator.add(15, 10, username, password)
        print(f"Calculator result: 15 + 10 = {calc_result}")
        
    except PermissionError as e:
        print(f"Access denied for {username}: {e}")
    except Pyro4.errors.CommunicationError:
        print("Server not available!")

print("Testing valid credentials...")
test_connection("admin", "password123")

print("\nTesting valid credentials (user)...")
test_connection("user", "userpass")

print("\nTesting invalid credentials...")
test_connection("admin", "wrongpassword")

print("\nTesting unknown user...")
test_connection("hacker", "hackpass")
