import os, jwt
from flask import Flask,request


app = Flask(__name__)


#post /login data: {username :}
@app.route('/login' , methods=['POST'])
def login():
   #assuming the user has got authenticated in this method. We are going to generate the JWT now
  request_data = request.get_json()
  payload = [
  {
    'username': request_data['username'],
    'id': request_data['id']
  }
]
  
  with open('keys/rsa_private.pem') as fp:
      secret = fp.read()
  token = jwt.encode({'data' : payload}, secret, algorithm='RS256')
  return {"status": "SUCCESS", "token": token.decode('utf-8')}
  
  #pass

 # set the port dynamically with a default of 3000 for local development
port = int(os.getenv('PORT', '9090'))

# start the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
