import Pyro4

greeting = Pyro4.Proxy("PYRONAME:example.greeting")
result = greeting.say_hello("Student")
print(result)
