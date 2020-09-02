import os
import sys
import configparser
from flask import Flask,jsonify,request,render_template
import requests
app = Flask(__name__)

ENV_CONFIG = {
    'dev': 'dev',
    'prod': 'prod',
    'staging': 'staging'
}

def load_env_configuration(env):
    if not env:
        print('Please define the ENV')
        sys.exit(1)
    config = configparser.RawConfigParser()
    print(env)
    config.read((os.path.join(os.getcwd(), 'config/%s.cfg' % ENV_CONFIG[env])))
    return config


global configp


#get /app2
@app.route('/app2')
def get_stores():
  url = configp.get('urls', 'store_url')
  print(url)
  resp = requests.get(url)
  if resp.status_code == 200:
    data = resp.json()
    return data
	
  return "error", resp.status_code
  #pass


    
  # set the port dynamically with a default of 3000 for local development
port = int(os.getenv('PORT', '5004'))

# start the app
if __name__ == '__main__':
    env = sys.argv[1]
    configp = load_env_configuration(env)
    app.run(host='0.0.0.0', port=port)