import Pyro4
import time

@Pyro4.expose
class ReportService:
    def generateReport(self):
        time.sleep(10)
        return "Report generated successfully"

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
ns.register("example.report", daemon.register(ReportService))
print("Report server ready...")
daemon.requestLoop()
