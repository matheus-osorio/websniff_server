class Holder:
  def __init__(self):
    self.value = self.make_default('programs')
  
  def make_default(self,name = None, extra = {}):
    obj = {
      'timed': {
        'incoming': [0],
        'outgoing': [0],
        'total': [0]
      },
      'total': {
        'incoming': 0,
        'outgoing': 0,
        'total': 0
      }
    }

    if name:
      obj[name] = {}
    
    obj.update(extra)
    return obj
  
  def prepare(self, program, connection, protocol): 
    value = self.value['programs']
    if program not in value:
      value[program] = self.make_default('connections')
    value = value[program]['connections']
    if connection not in value:
      value[connection] = self.make_default('protocols')
    value = value[connection]['protocols']
    if protocol not in value:
      value['TCP'] = self.make_default(None, {
        'counting': {
          'incoming': 0,
          'outgoing': 0,
          'total': 0
        }
      })
      value['UDP'] = self.make_default(None, {
        'counting': {
          'incoming': 0,
          'outgoing': 0,
          'total': 0
        }
      })

  def get(self, entries):
    default_entries = ['programs','connections','protocols']
    obj = self.value
    max_len = min(len(entries), len(default_entries))
    for values in enumerate(entries):
      index, value = values
      if index < max_len:
        obj = obj[default_entries[index]]
      obj = obj[value]

    return obj

  def insert(self, program, connection, protocol, direction, value):
    obj = self.get([program,connection,protocol,'counting'])
    obj[direction] += value
    obj['total'] += value
  
  def update(self):
    total_in = 0
    total_out = 0
    for program_name in self.value['programs']:
      program = self.get([program_name])
      program_in = 0
      program_out = 0

      for connection_name in program['connections']:
        connection = self.get([program_name, connection_name])
        conn_in = 0
        conn_out = 0

        for protocol_name in connection['protocols']:
          protocol = self.get([program_name, connection_name, protocol_name])
          prot_counting = protocol['counting']
          protocol['counting'] = {
          'incoming': 0,
          'outgoing': 0,
          'total': 0
          }
          prot_in = prot_counting['incoming']
          prot_out = prot_counting['outgoing']

          conn_in += prot_in
          conn_out += prot_out
          self.update_total(protocol, prot_in, prot_out)
        
        self.update_total(connection, conn_in, conn_out)
        program_in += conn_in
        program_out += conn_out
      
      self.update_total(program, program_in, program_out)
      total_in += program_in
      total_out += program_out
    
    self.update_total(self.value, total_in, total_out)
  
  def update_total(self, level, total_in, total_out):
    total = level['total']
    timed = level['timed']
    total_all = total_in + total_out
    total['incoming'] += total_in
    total['outgoing'] += total_out
    total['total'] += total_all

    timed['incoming'].append(total_in)
    timed['outgoing'].append(total_out)
    timed['total'].append(total_all)


  



