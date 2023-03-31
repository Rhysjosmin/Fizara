from flask import Flask, request, url_for
import json
import random

from flask_cors import CORS
Doctor = ''
USER = ''
d = {}
AppointmentDB = {
    'James': {
    },
    'John': {
    },
    'Jennifer': {
    },
    'Richard': {
    },
    'William': {
    },
    'Robert': {
    },
    'Michael': {
    },
    'David': {
    },
    'Stephen': {
    },
    'Jeffrey': {
    },
    'Charles': {
    },
    'Daniel': {
    },
    'Steven': {
    },
    'Paul': {
    },
    'Elizabeth': {
    },
    'Susan': {
    },
    'Mary': {
    },
    'Elizabeth': {
    },
    'Joseph': {
    },
    'Mark': {
    },
    'Thomas': {
    },

}
TodoDB = {

    'Mary': [
        'Eat 5 Calories', 'Sleep 8 hours', '2 Sets of 10 pushups', 'Take Paracetamol At 8 AM', 'Take Insulin', 'Eat Food', 'Drink Water', 'Take Medicine'
    ],
    'Anya': [
        'Dont Eat 5 Calories', 'Sleep 8 hours', '2 Sets of 20 Pullups', 'Take Insulin'
    ],
    'Penelope': [
        'Eat 5 Calories', 'Sleep 8 hours', '2 Sets of 10 pushups', 'Take Paracetamol At 8 AM', 'Take Insulin'
    ],
    'Adriana': [
        'Eat 3 Calories', 'Sleep 5 hours', '2 Sets of 10 pushups', 'Take Paracetamol At  AM', 'Take Insulin'
    ],
    'Emily': [
        'Eat 5 Calories', 'Sleep 8 hours', '2 Sets of 10 pushups', 'Take Paracetamol At 8 AM', 'Take Insulin'
    ],
    'Jane': [
        'Eat 5 Calories', 'Sleep 8 hours', '2 Sets of 10 pushups', 'Take Paracetamol At 8 AM', 'Take Insulin'
    ],
    'Ava': [
        'Eat 5 Calories', 'Sleep 8 hours', '2 Sets of 10 pushups', 'Take Paracetamol At 8 AM', 'Take Insulin'
    ],
    'Megan': [
        'Eat 5 Calories', 'Sleep 8 hours', '2 Sets of 10 pushups', 'Take Paracetamol At 8 AM', 'Take Insulin'
    ],
    'Irene': [
        'Eat 5 Calories', 'Sleep 8 hours', '2 Sets of 10 pushups', 'Take Paracetamol At 8 AM', 'Take Insulin'
    ],



}
Ratings = {}
NewsDB = {
    'In Conversation: Is the ketogenic diet right for autoimmune conditions?': {
        'Body': 'The ketogenic diet is often labelled controversial due to its low carb, high fat nature. However, it is also touted as one of the best diets for weight loss, improving insulin sensitivity, and controlling seizures. But could this diet also have the potential to help inflammatory autoimmune conditions and reduce chronic pain?',
        'link': 'https://www.medicalnewstoday.com/articles/in-conversation-is-the-ketogenic-diet-right-for-autoimmune-conditions'
    },
    'Gout may be caused by deficiency of a protein found in joint fluid': {
        'Body': 'Gout, a common form of inflammatory arthritis, can cause intense pain, swelling, and stiffness in the joints.',
        'link': 'https://www.medicalnewstoday.com/articles/new-look-at-an-ancient-disease-study-finds-novel-treatment-targets-for-gout'
    },
    'New study suggests potential link between air pollution and dementia': {
        'Body': 'A recent study has found a potential link between exposure to air pollution and an increased risk of developing dementia. The study analyzed data from over 13,000 people in the UK and found that those living in areas with higher levels of air pollution were more likely to develop dementia than those in cleaner areas.',
        'link': 'https://www.theguardian.com/society/2022/feb/21/air-pollution-linked-to-increased-risk-of-dementia-major-study-suggests'
    },
    'Scientists discover new speciesrt of ancient human in Israel': {
        'Body': 'Scientists have discovered a new species of ancient human in Israel, dating back around 140,000 years. The fossils were found in a cave and are believed to belong to a previously unknown group of humans, who may have interbred with Neanderthals and modern humans.',
        'link': 'https://www.bbc.com/news/science-environment-61654780'
    },
    'Scientists discover new specierees of ancient human in Israel': {
        'Body': 'Scientists have discovered a new species of ancient human in Israel, dating back around 140,000 years. The fossils were found in a cave and are believed to belong to a previously unknown group of humans, who may have interbred with Neanderthals and modern humans.',
        'link': 'https://www.bbc.com/news/science-environment-61654780'
    },
    'Scientists discover new speci77es of ancient human in Israel': {
        'Body': 'Scientists have discovered a new species of ancient human in Israel, dating back around 140,000 years. The fossils were found in a cave and are believed to belong to a previously unknown group of humans, who may have interbred with Neanderthals and modern humans.',
        'link': 'https://www.bbc.com/news/science-environment-61654780'
    },
    'Scientists discover new species o54654f ancient human in Israel': {
        'Body': 'Scientists have discovered a new species of ancient human in Israel, dating back around 140,000 years. The fossils were found in a cave and are believed to belong to a previously unknown group of humans, who may have interbred with Neanderthals and modern humans.',
        'link': 'https://www.bbc.com/news/science-environment-61654780'
    },
}
UserDatabase = {

    "john": {"email": "johndoc@doc.com", "password": "1234", "DocID": "12345"},
    "user": {
        'email': 'user@email.com',
        'password': '1234',
        'Calorie': [1,2,3,4,5,6,7,8,9,10,11,102,13,14,15,16,17,18,19,20],
        'Todo': [
            'Eat 5 Calories', 'Sleep 8 hours', '2 Sets of 10 pushups', 'Take Paracetamol At 8 AM', 'Take Insulin'
        ]}
}

Reason = [
    'Checkup',
    'X-Ray',
    'Blood Test',
    'Ultrasound'
]


UseDB = {}

app = Flask(__name__)
CORS(app)
# fetch(`http://127.0.0.1:5000/Signup/${document.getElementById('name').value}/${document.getElementById('email').value}/${document.getElementById('password').value}`)


def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


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
def AppendCalorie(User,Value):
    UserDatabase[User.lower()]['Calorie'].append(Value)
    return '0'

@app.route('/<User>/AverageCalorie')
def AverageCalories(User):
    Calories=UserDatabase[User.lower()]['Calorie']
    return json.dumps(round(sum(Calories)/len(Calories),3))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
