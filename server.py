from flask import Flask, request
from aggregator import Aggregator
from flask_cors import CORS
import json
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
  response['total'] = {}
  response['table'] = {}
  response['bullet'] = {
    'total': program['total']['total'],
    'incoming': program['total']['incoming'],
    'outgoing': program['total']['outgoing'],
    'timed': program['timed']['total'][-1]
  }
  for connection in program['connections']:
    current = program['connections'][connection]
    response['total'][connection] = current['timed']['total']
    response['table'][connection] = {
      'total': current['total']['total'],
      'incoming': current['total']['incoming'],
      'outgoing': current['total']['outgoing']
    }
  return json.dumps(response)

app.run()
