from flask import Flask,request
import json
from flask_cors import CORS
d={}

UserDatabase='UserDB.json'
def ReadDB():

    try:
        f = open (UserDatabase, "r")
        d= json.loads(f.read())
        f.close()
    except:
        f = open (UserDatabase, "w")
        f.write('{}')
        f.close()
        f = open (UserDatabase, "r")
        d= json.loads(f.read())
        f.close()
    return d
        


app=Flask(__name__)
CORS(app)
    # fetch(`http://127.0.0.1:5000/Signup/${document.getElementById('name').value}/${document.getElementById('email').value}/${document.getElementById('password').value}`)

@app.route('/Signup/<name>/<email>/<password>' ,methods=['GET'])
def Signup(name,email,password):
    d=ReadDB()
    name=name.replace(' ', '').lower()
    email=email.replace(' ', '').lower()
    if name not in d:
        print('Saved')
        d[name]={
            
            'email':email,
            'password':password,
            
        }
        with open(UserDatabase, 'w') as f:
            json.dump(d, f)
        return json.dumps("Signed Up")
    else:
        print('Already Present')
        
        return json.dumps("User Already Present")

@app.route('/Login/<name>/<email>/<password>')
def login(name,email,password):
    d=ReadDB()
    print(f'Email:{email}')
    name=name.replace(' ', '').lower()
    email=email.replace(' ', '').lower()
    print(f'Email:{email}')
    print('Called')
    try:
        if d[name]['password']==password and d[name]['email']==email:
            print('Present')
            return json.dumps('Present')
        
        else:
            print('Wrong Password')
            
            return json.dumps('Not')
    except:
            print('not Present')
        
            return json.dumps('Not')
        
if __name__=='__main__':
    app.run(debug=True)