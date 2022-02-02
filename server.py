from flask import Flask, request
from aggregator import Aggregator
from flask_cors import CORS
import json
import socket, struct

aggr = Aggregator()
aggr.start()

app = Flask(__name__)
CORS(app)

@app.route('/general')
def general():
  obj = aggr.get()
  response = {}
  response['directional'] = obj['timed']
  response['total'] = {}
  response['table'] = {}
  response['bullet'] = {
    'total': obj['total']['total'],
    'incoming': obj['total']['incoming'],
    'outgoing': obj['total']['outgoing'],
    'timed': obj['timed']['total'][-1]
  }
  for program in obj['programs']:
    current = obj['programs'][program]
    response['total'][program] = current['timed']['total']
    response['table'][program] = {
      'total': current['total']['total'],
      'connections': len(current['connections']),
      'incoming': current['total']['incoming'],
      'outgoing': current['total']['outgoing']
    }
  return json.dumps(response)

@app.route('/specific')
def specific():
  program_name = request.headers['program']
  response = {}
  obj = aggr.get()
  program = obj['programs'][program_name]

  response['directional'] = program['timed']
  response['total'] = {
    'total': program['timed']['total']
  }
  response['table'] = {}
  response['bullet'] = {
    'total': program['total']['total'],
    'incoming': program['total']['incoming'],
    'outgoing': program['total']['outgoing'],
    'timed': program['timed']['total'][-1],
    
  }

  for connection in program['connections']:
    current = program['connections'][connection]
    response['table'][connection] = {
      'total': current['total']['total'],
      'protocol': list(current['protocols'].keys())[0],
      'incoming': current['total']['incoming'],
      'outgoing': current['total']['outgoing']
    }
  return json.dumps(response)

@app.route('/connection')
def connection():
  program_name = request.headers['program']
  connection_name = request.headers['conn']
  response = {}
  obj = aggr.get()
  connection = obj['programs'][program_name]['connections'][connection_name]

  response['directional'] = connection['timed']
  response['total'] = {
    'total': connection['timed']['total'],
    'TCP': connection['protocols']['TCP']['timed']['total'],
    'UDP': connection['protocols']['UDP']['timed']['total']
  }
  response['table'] = {}
  response['bullet'] = {
    'total': connection['total']['total'],
    'incoming': connection['total']['incoming'],
    'outgoing': connection['total']['outgoing'],
    'timed': connection['timed']['total'][-1],
  }

  for protocol in connection['protocols']:
    current = connection['protocols'][protocol]
    response['table'][protocol] = {
      'total': current['total']['total'],
      'incoming': current['total']['incoming'],
      'outgoing': current['total']['outgoing']
    }
  return json.dumps(response)




@app.route('/get_config')
def get_config():
  return json.dumps(aggr.config.config)

@app.route('/update_configs')
def update_configs():
  config = request.headers['config']
  value = request.headers['value']
  item_type = request.headers['type']

  if item_type == 'int':
    value = int(value)
  aggr.update_configs(config,value)
  return '200'



app.run()
