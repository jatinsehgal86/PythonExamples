import os
from flask import Flask,jsonify,request

app = Flask(__name__)

stores = [{
    'name': 'Store1',
    'items': [{'name':'item1', 'price': 15.99 },
	{'name':'item2', 'price': 20 }]
},
{
    'name': 'Store2',
    'items': [{'name':'item1', 'price': 21 },
	{'name':'item2', 'price': 22 }]
}]


#get /store
@app.route('/store')
def get_stores():
  return jsonify({'stores': stores})
  #pass
  
  
  #post /store data: {name :}
@app.route('/store' , methods=['POST'])
def create_store():
  request_data = request.get_json()
  new_store = {
    'name':request_data['name'],
    'items':[]
  }
  stores.append(new_store)
  return jsonify(stores)
  #pass
  
  #get /store/<name> data: {name :}
@app.route('/store/<string:name>')
def get_store(name):
  for store in stores:
    if store['name'] == name:
          return jsonify(store)
  return jsonify ({'message': 'store not found'})
  #pass
  
   # set the port dynamically with a default of 3000 for local development
port = int(os.getenv('PORT', '9094'))

# start the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)