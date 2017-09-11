import queue
import time
from count_worker import CountWorker 
class Bus:
  def __init__(self):
    self.topics = {}
    self.workers = []
    
  def post(self, topic, message=None):
    if topic not in self.topics: return
    for queue in self.topics[topic]:
      queue.put((topic, message))
  
  def register(self, topic, q):
    if type(q) != queue.Queue: raise Exception("You can only register queue.Queue's")
    if topic not in self.topics: self.topics[topic] = []
    self.topics[topic].append(q)
    return q
    
  def start_count_worker(self, num):
    w = CountWorker(self, num)
    w.start()
    self.workers.append(w)
  
  def start_workers(self):
    self.start_count_worker(100)
    
  def start(self):
    self.start_workers()

  def stop(self):
    self.post('stop')
    self.wait()
    
  def wait(self):
    for w in self.workers:
      w.wait()
      
if __name__ == "__main__":      
  b = Bus()
  b.start()
  b.post("count", 1)
  b.wait()