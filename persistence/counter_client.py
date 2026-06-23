import Pyro4

counter = Pyro4.Proxy("PYRONAME:example.counter")

print(f"Current count: {counter.getCount()}")

for i in range(5):
    new_count = counter.increment()
    print(f"Incremented to: {new_count}")

print(f"Final count: {counter.getCount()}")
