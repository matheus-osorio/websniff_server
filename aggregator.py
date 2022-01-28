from sniff import Sniff
from utils import get_entries
from holder import Holder
from threading import Thread, Timer
from configurator import Configurator
class Aggregator:
  def __init__(self):
    self.config = Configurator()
    self.sniffer = Sniff(self.add_value)
    self.holder = Holder(max_hold = self.config.max_hold)

  def add_value(self, pct):
    program, connection, protocol, incoming, outgoing = get_entries(pct,[
    'proc_name',
    'Ip',
    't_protocol',
    'incoming',
    'outgoing'
    ])

    self.holder.prepare(program, connection, protocol)
    if incoming:
      self.holder.insert(program, connection, protocol, 'incoming',incoming)
    if outgoing:
      self.holder.insert(program, connection, protocol, 'outgoing',outgoing)
  
  def start(self):
    Timer(1.0,self.update_holder).start()
    t = Thread(target=self.sniffer.start)
    t.daemon = True
    t.start()
    
  def update_holder(self):
    self.holder.update()
    Timer(self.config.update_schedule,self.update_holder).start()
  
  def get(self):
    return self.holder.value
    


aggr = Aggregator()
aggr.start()


  