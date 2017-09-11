import queue
import threading
class Worker:
  def __init__(self, bus):
    self.bus = bus
    self.queue = queue.Queue()
    self.cbs = {}
    self.register('stop')
    
  def register(self, topic):
    self.bus.register(topic, self.queue)
    
  def start(self):
    self.thread = threading.Thread(target=self.run)
    self.thread.daemon = True
    self.thread.start()
  
  def wait(self):
    self.thread.join()
    
  def run(self):
    while True:
      topic, msg = self.queue.get()
      if topic == 'stop':
        break
      self.handle(topic, msg)
  
  def handle(self, topic, msg):
    print("Received message {}".format(topic))