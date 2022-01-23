from flask import Flask
from aggregator import Aggregator
import json
aggr = Aggregator()
aggr.start()

app = Flask(__name__)

@app.route('/')
def index():
  return json.dumps(aggr.get())


app.run()
