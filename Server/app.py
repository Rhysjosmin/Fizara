from flask import Flask, jsonify, request, url_for,render_template
import json
import random
from DB.DB import *
from DB.Yogasanas import *
from MySQL.app import Pharmacy
from flask_cors import CORS
from PIL import Image
Doctor = ''
USER = ''


app = Flask(__name__)
CORS(app)
# fetch(`http://127.0.0.1:5000/Signup/${document.getElementById('name').value}/${document.getElementById('email').value}/${document.getElementById('password').value}`)


app.config['UPLOAD_FOLDER'] = './Server/DB/Images'

app.register_blueprint(Pharmacy,url_prefix='/Pharmacy')

def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)

@app.route('/Yogasanas/<page>')
def YogasanasDBFlask(page):
    return Yogasanas[page]

@app.route('/Home', methods=['GET'])
def HomePage():  # pragma: no cover
    return render_template('index.html')


@app.route('/')
def index():
    links = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append(f'<a href="{url}">{rule.endpoint}</a>')
    string = ''
    for link in links:
        string = string+link+'</br>'
    return string

# http://127.0.0.1:5000/Signup/Rhys/rhys123@gail.com/1324


@app.route('/Signup/<name>/<email>/<password>', methods=['GET'])
@app.route('/Signup/<name>/<email>/<password>/<DocID>', methods=['GET'])
def Signup(name, email, password, DocID=None):
    global AppointmentDB, UserDatabase

    name = name.replace(' ', '').lower()
    email = email.replace(' ', '').lower()
    if name not in UserDatabase:
        print('Saved')
        if (DocID):
            UserDatabase[name] = {

                'email': email,
                'password': password,
                'DocID': DocID

            }
            AppointmentDB[name.capitalize()] = {}

        else:
            UserDatabase[name] = {
                'email': email,
                'password': password,
                'Calorie': [0],
                'Todo': [
                    'Eat 5 Calories', 'Sleep 8 hours', '2 Sets of 10 pushups', 'Take Paracetamol At 8 AM', 'Take Insulin'
                ]
            }

        if (DocID):
            return json.dumps("Signed Up Doctor")
        else:
            return json.dumps("Signed Up User")
    else:
        print('Already Present')

        return json.dumps("User Already Present")


@app.route('/Login/<name>/<email>/<password>')
def login(name, email, password):

    # print(f'Email:{email}')
    name = name.replace(' ', '').lower()
    email = email.replace(' ', '').lower()
    # print(f'Email:{email}')
    # print('Called')
    try:

        if UserDatabase[name]['password'] == password and UserDatabase[name]['email'] == email:
            print('Present')
            try:
                if (UserDatabase[name]['DocID']):
                    return json.dumps('Doctor')
            except:
                return json.dumps('User')

        else:
            print('Wrong Password')

            return json.dumps('Not')
    except:
        print('not Present')

        return json.dumps('Not')


@app.route('/<Doctor>/Appointments')
def Appointments(Doctor):
    if Doctor in AppointmentDB:
        return json.dumps(AppointmentDB[Doctor])
    else:
        # NotPresent = {'Present': 'False'}
        return json.dumps(AppointmentDB['John'])


@app.route('/<User>/Todo')
def Todo(User):
    if User in UserDatabase:
        return json.dumps(UserDatabase[User]['Todo'])
        # return json.dumps(TodoDB[User])
    else:
        return 'Not Found'


@app.route('/News')
def News():
    return json.dumps(NewsDB)


@app.route('/Doctors')
def Doctors():
    return json.dumps(list(AppointmentDB.keys()))


@app.route('/SetRating/<User>/<value>')
def SetRate(User, value):
    # print(AppointmentDB[User])
    Ratings[User] = value
    print(Ratings)
    return '0'


@app.route('/AppointmentDB')
def _AppointmentDB():
    return json.dumps(AppointmentDB)


TempStorageDB={}
# SERVER_URL+'/TempList/'+Math.round(Math.random()*1000
@app.route('/TempList/<ID>/<Data>')
def TempList(ID,Data):
    TempStorageDB[ID]=Data
    print(TempStorageDB)
    return 'OK'

@app.route('/TempList/Display/<ID>', methods=['GET'])
def TempListDisp(ID):
   
    return TempStorageDB[ID]
@app.route('/TempList/Display/', methods=['GET'])
def TempListDispNOID():
   
    return json.dumps(TempStorageDB)




@app.route('/UserDB')
def _UserDB():
    return json.dumps(UserDatabase)


@app.route('/MakeAppointment', methods=['GET', 'POST'])
def MakeAppointment():
    message = request.json.get('message')
    doctor_name = request.json.get('doctor_name')
    user_name = request.json.get('user_name')
    AppointmentDB[doctor_name][user_name] = {'Reason': message,
                                             'Date': '12/3/23',
                                             'Time': '15:00'}
    print(AppointmentDB[doctor_name])
    # do something with message and doctor_name, e.g. send an email or store in a database

    return 'Message sent successfully!'


@app.route('/ClearAppointments/<Doc>')
def ClearAppointments(Doc):
    AppointmentDB[Doc] = {}
    return '0'


@app.route('/ClearAppointments')
def _ClearAppointments():
    for i in AppointmentDB:
        AppointmentDB[i] = {}
    return '0'

# ${SERVER_URL}/AppendCalorie/${USER}/${
#           document.getElementById("CalorieInput").value
#         }


@app.route('/AppendCalorie/<User>/<int:Value>')
def AppendCalorie(User, Value):
    UserDatabase[User.lower()]['Calorie'].append(Value)
    return '0'


@app.route('/<User>/AverageCalorie')
def AverageCalories(User):
    Calories = UserDatabase[User.lower()]['Calorie']
    return json.dumps(round(sum(Calories)/len(Calories), 3))


if __name__ == '__main__':
    import random
    app.run(host='0.0.0.0',debug=True )
    # for key in AppointmentDB:
    #     Domains=[
    #         '@gmail.com',
    #         '@icloud.com',

    #     ]
    #     d={
    #         f'{key.lower()}':{
    #             "email":f'{key.lower()}{Domains[random.randint(0,len(Domains)-1)]}',
    #             "password":str(random.randint(100000, 999999)),
    #             "DocID":str(random.randint(100000, 999999))
    #        }
    #        }

    #     print('"'+key.lower()+'" : '+str(d[key.lower()])+',\n')
