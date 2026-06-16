import Pyro4
import Pyro4.util

# Define valid users
VALID_USERS = {
    "admin": "password123",
    "user": "userpass"
}

@Pyro4.expose
class SecureGreeting:
    def say_hello(self, name, username=None, password=None):
        # Check authentication
        if username not in VALID_USERS or VALID_USERS[username] != password:
            raise PermissionError("Invalid credentials!")
        return f"Hello, {name}! Authenticated as {username}"

@Pyro4.expose
class SecureCalculator:
    def add(self, a, b, username=None, password=None):
        if username not in VALID_USERS or VALID_USERS[username] != password:
            raise PermissionError("Invalid credentials!")
        return a + b

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()

ns.register("secure.greeting", daemon.register(SecureGreeting))
ns.register("secure.calculator", daemon.register(SecureCalculator))

print("Secure services are ready...")
daemon.requestLoop()