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
  "New research reveals potential link between coffee consumption and reduced risk of heart disease": {
        "Body": "A new study suggests that drinking coffee may lower the risk of developing heart disease. The study found that people who drank two to three cups of coffee per day had a 20% lower risk of heart disease compared to those who did not drink coffee. The researchers believe that the antioxidants and other beneficial compounds in coffee may be responsible for this protective effect.",
        "link": "https://www.medicalnewstoday.com/articles/new-research-reveals-potential-link-between-coffee-consumption-and-reduced-risk-of-heart-disease"
    },
    "Scientists discover new species of deep-sea fish off the coast of Australia": {
        "Body": "A team of scientists has discovered a new species of deep-sea fish off the coast of Australia. The fish, which has been named the 'Black-Blotched Stingray', was found at a depth of over 2,000 meters and has unique features such as its black and white coloration and a spine that is used for defense. The discovery is an exciting development for marine biology and highlights the need to continue exploring the depths of the ocean.",
        "link": "https://www.sciencedaily.com/releases/2022/03/220328104006.htm"
    },
    "Researchers find potential new treatment for type 2 diabetes": {
        "Body": "Researchers have discovered a potential new treatment for type 2 diabetes. The treatment involves a drug that targets a specific protein in the liver, which has been found to play a key role in regulating blood sugar levels. In tests on mice, the drug was able to significantly lower blood sugar levels and improve insulin sensitivity. Further research is needed to determine whether the drug is safe and effective in humans, but the findings offer hope for those living with type 2 diabetes.",
        "link": "https://www.medicalnewstoday.com/articles/researchers-find-potential-new-treatment-for-type-2-diabetes"
    },
    "New study suggests link between screen time and increased risk of depression in teenagers": {
        "Body": "A new study has found a potential link between high levels of screen time and an increased risk of depression in teenagers. The study followed over 1,000 teenagers for two years and found that those who spent more than four hours per day on screens were significantly more likely to develop symptoms of depression compared to those who spent less time on screens. The researchers suggest that this link may be due to the social isolation and lack of physical activity that often accompanies excessive screen time.",
        "link": "https://www.theguardian.com/society/2022/mar/24/link-between-screen-time-and-depression-in-teenagers-study-suggests"
    }
}
UserDatabase = {

    "john": {"email": "johndoc@doc.com", "password": "1234", "DocID": "12345"},
 
 "james" : {'email': 'james@icloud.com', 'password': '425932', 'DocID': '428809'},

"john" : {'email': 'john@icloud.com', 'password': '591493', 'DocID': '415132'},

"jennifer" : {'email': 'jennifer@gmail.com', 'password': '972472', 'DocID': '975999'},

"richard" : {'email': 'richard@icloud.com', 'password': '249470', 'DocID': '547443'},

"william" : {'email': 'william@icloud.com', 'password': '653334', 'DocID': '636128'},

"robert" : {'email': 'robert@gmail.com', 'password': '307968', 'DocID': '283225'},

"michael" : {'email': 'michael@gmail.com', 'password': '678136', 'DocID': '664056'},

"david" : {'email': 'david@icloud.com', 'password': '230031', 'DocID': '265466'},

"stephen" : {'email': 'stephen@icloud.com', 'password': '660196', 'DocID': '917119'},

"jeffrey" : {'email': 'jeffrey@icloud.com', 'password': '227062', 'DocID': '880658'},

"charles" : {'email': 'charles@icloud.com', 'password': '256935', 'DocID': '136025'},

"daniel" : {'email': 'daniel@icloud.com', 'password': '582863', 'DocID': '560825'},

"steven" : {'email': 'steven@gmail.com', 'password': '720492', 'DocID': '774657'},

"paul" : {'email': 'paul@icloud.com', 'password': '839491', 'DocID': '464418'},

"elizabeth" : {'email': 'elizabeth@gmail.com', 'password': '459807', 'DocID': '509446'},

"susan" : {'email': 'susan@gmail.com', 'password': '331193', 'DocID': '551320'},

"mary" : {'email': 'mary@gmail.com', 'password': '323856', 'DocID': '972752'},

"joseph" : {'email': 'joseph@icloud.com', 'password': '717302', 'DocID': '165582'},

"mark" : {'email': 'mark@gmail.com', 'password': '938772', 'DocID': '195681'},

"thomas" : {'email': 'thomas@icloud.com', 'password': '318568', 'DocID': '583772'},
 
 
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
    import random
    app.run(host='0.0.0.0')
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
