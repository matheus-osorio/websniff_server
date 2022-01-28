import json

class Configurator:
  def __init__(self):
    f = open('saved_configs.txt', 'r')
    self.config = json.loads(f.read())
    f.close()

  def save(self, obj = {}):
    self.config.update(obj)
    f = open('saved_configs.txt', 'w')
    f.write(json.dumps(self.config,indent=2))
    f.close()
  
  def __getattr__(self, name):
    if name in self.config:
      return self.config[name]
    else:
      return getattr(self, name)



