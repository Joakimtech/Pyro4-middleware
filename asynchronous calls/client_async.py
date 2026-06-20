import Pyro4
import time

print("Synchronous call:")
start = time.time()
report = Pyro4.Proxy("PYRONAME:example.report")
result = report.generateReport()
print(f"Result: {result}")
print(f"Time taken: {time.time() - start:.2f}s")

print("\nAsynchronous call:")
start = time.time()
async_proxy = Pyro4.Proxy("PYRONAME:example.report")
async_result = async_proxy.generateReport(0)

print("Request sent...")
for i in range(5):
    print(f"Performing other work... {i+1}/5")
    time.sleep(1)

print(async_result.value)
print(f"Time taken: {time.time() - start:.2f}s")
