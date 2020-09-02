import os, jwt
from flask import Flask,jsonify,request,render_template

app = Flask(__name__)

stores = [{
    'name': 'My Store',
    'items': [{'name':'my item', 'price': 15.99 }]
}]

@app.route('/')
def home():
  return render_template('index.html')
  
  
def verify_token(func):

    def wrapper(*args, **kwargs):
        error = {"error": "Unauthorised request"}
        auth_header = request.headers.get('Authorization', None)
        if auth_header is None:
            return error, 401
        try:
            with open('keys/rsa_public.pem') as fp:
                secret = fp.read()
            token = auth_header.split(' ')[-1].strip()
            payload = jwt.decode(token, secret, algorithm='RS256')
            print(payload)
        except jwt.ExpiredSignatureError:
            return error, 401
        except Exception as ex:
            return error, 401

        return func(*args, **kwargs)

    return wrapper

#post /store data: {name :}
@app.route('/store' , methods=['POST'])
@verify_token
def create_store():
  request_data = request.get_json()
  new_store = {
    'name':request_data['name'],
    'items':[]
  }
  stores.append(new_store)
  return jsonify(new_store)
  #pass

#get /store/<name> data: {name :}
@app.route('/store/<string:name>')
def get_store(name):
  for store in stores:
    if store['name'] == name:
          return jsonify(store)
  return jsonify ({'message': 'store not found'})
  #pass

#get /store
@app.route('/store')
def get_stores():
  return jsonify({'stores': stores})
  #pass

#post /store/<name> data: {name :}
@app.route('/store/<string:name>/item' , methods=['POST'])
def create_item_in_store(name):
  request_data = request.get_json()
  for store in stores:
    if store['name'] == name:
        new_item = {
            'name': request_data['name'],
            'price': request_data['price']
        }
        store['items'].append(new_item)
        return jsonify(new_item)
  return jsonify ({'message' :'store not found'})
  #pass

#get /store/<name>/item data: {name :}
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
  for store in stores:
    if store['name'] == name:
        return jsonify( {'items':store['items'] } )
  return jsonify ({'message':'store not found'})




    
  # set the port dynamically with a default of 3000 for local development
port = int(os.getenv('PORT', '5000'))

# start the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)