import worker

class CountWorker(worker.Worker):
  def __init__(self, bus, max):
    super().__init__(bus)
    self.max = max
    self.register("count")
  
  def handle(self, topic, msg):
    if msg < self.max:
      out = msg + 1
      print("Worker {} posting {}".format(self.max, out))
      self.bus.post("count", out)
    else:
      print("STOP")
      self.bus.post("stop")
