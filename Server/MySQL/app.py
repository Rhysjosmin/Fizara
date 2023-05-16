import base64
import json
import os
from flask import Blueprint, jsonify, redirect, request, current_app
from flask_cors import CORS
from werkzeug.utils import secure_filename
from PIL import Image as _Image
import sys


UPLOAD_FOLDER = '/DB/Images'

Pharmacy = Blueprint('Admin', __name__)

request_headers = {}
request_headers['Access-Control-Allow-Origin'] = '*'
request_headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE'
request_headers['Access-Control-Allow-Headers'] = 'Content-Type'


PharmacyDB = [
    {"Image": "./Server/DB/Images/Polyethylene glycol pegred powder - 1.jpg",
     "Name": "Polyethylene glycol pegred powder",
     "Price": "180"},
    {"Image": "./Server/DB/Images/Novorapid Flexpens - 1.jpg",
     "Name": "Novorapid Flexpens",
     "Price": "2050.3"},
    {"Image": "./Server/DB/Images/Pediasure Complete - 1.jpg",
     "Name": "Pediasure Complete",
     "Price": "750"},
    {"Image": "./Server/DB/Images/hcg-pregnancy-test-kit-500x500.webp",
     "Name": "Pregnancy Test Kit",
     "Price": "453"},
    {"Image": "./Server/DB/Images/health-d.webp",
     "Name": "Health-D",
     "Price": "500"},
    {"Image": "./Server/DB/Images/cinnarizine tablets.jpg",
     "Name": "Cinnarizine Tablets",
     "Price": "200"},
    {"Image": "./Server/DB/Images/Coxiblu 90 Tablets .jpg",
     "Name": "Coxiblu 90 Tablets",
     "Price": "300"},
    {"Image": "./Server/DB/Images/Paracetamol-500-MG-Tablet-manufcaturer-india-Taj-Life-Sciences-6-scaled.webp",
     "Name": "Paracetamol-500-MG-Tablet",
     "Price": "260"},
    {"Image": "./Server/DB/Images/rosuvastatin-10mg-fenofibrate-145mg-medicine-500x500.webp",
     "Name": "Rosuvastatin 10mg Fenofibrate 145mg Medicine",
     "Price": "300"},
    {"Image": "./Server/DB/Images/atazor 200.webp",
     "Name": "Atazor 200 Tablets",
     "Price": "300"},
    {"Image": "./Server/DB/Images/Amoxicillin Capsules.jpg",
        "Name": "Amoxicillin Capsules", "Price": "50"},
    {"Image": "./Server/DB/Images/Ibuprofen Tablets - 5.jpg",
        "Name": "Ibuprofen Tablets", "Price": "30"},
    {"Image": "./Server/DB/Images/Acetaminophen Tablets .jpg",
        "Name": "Acetaminophen Tablets", "Price": "25"},
    {"Image": "./Server/DB/Images/Omeprazole Capsules - 1.jpg",
        "Name": "Omeprazole Capsules", "Price": "75"},
    {"Image": "./Server/DB/Images/Metformin Tablets - 1.jpg",
        "Name": "Metformin Tablets", "Price": "40"},
    {"Image": "./Server/DB/Images/Ciprofloxacin Tablets .jpeg",
        "Name": "Ciprofloxacin Tablets", "Price": "60"},
    {"Image": "./Server/DB/Images/Levothyroxine Tablets.jpeg",
        "Name": "Levothyroxine Tablets", "Price": "35"},
    {"Image": "./Server/DB/Images/Lisinopril Tablets.jpeg",
        "Name": "Lisinopril Tablets", "Price": "45"},
    {"Image": "./Server/DB/Images/Losartan Tablets.jpeg",
        "Name": "Losartan Tablets", "Price": "50"},
    {"Image": "./Server/DB/Images/Simvastatin Tablets.jpeg",
        "Name": "Simvastatin Tablets", "Price": "70"},
    {"Image": "./Server/DB/Images/Aspirin Tablets.jpg",
        "Name": "Aspirin Tablets", "Price": "20"},
    {"Image": "./Server/DB/Images/Naproxen Tablets.jpeg",
        "Name": "Naproxen Tablets", "Price": "35"},
    {"Image": "./Server/DB/Images/Loratadine Tablets - 1.jpg",
        "Name": "Loratadine Tablets", "Price": "30"},



]

TempStorageDB = {
    
        "468234": [
            {
                "Name": "Novorapid Flexpens",
                "Price": 2050.3
            },
            {
                "Name": "Novorapid Flexpens",
                "Price": 2050.3
            },
            {
                "Name": "Novorapid Flexpens",
                "Price": 2050.3
            },
            {
                "Name": "Novorapid Flexpens",
                "Price": 2050.3
            }]
        
    
}
# SERVER_URL+'/TempList/'+Math.round(Math.random()*1000


@Pharmacy.route('/TempList/<ID>/<Data>')
def TempList(ID, Data):
    TempStorageDB[ID] = Data
    print(TempStorageDB)
    return 'OK'


@Pharmacy.route('/TempList/Display/<ID>', methods=['GET'])
def TempListDisp(ID):

    return TempStorageDB[ID]


@Pharmacy.route('/TempList/Display/', methods=['GET'])
def TempListDispNOID():

    return json.dumps(TempStorageDB)


@Pharmacy.route('/AddItem', methods=['POST', 'GET'])
def Additem():
    Name = request.form['Name']
    Image = request.files['Image']
    Price = request.form['Price']

    filename = secure_filename(Image.filename)
    filepath = current_app.config['UPLOAD_FOLDER']+'/'+filename
    Image.save(filepath)

    im = _Image.open(filepath)
    resized = im.resize((500, 500))
    resized.save(filepath)

    # with open(filepath, 'rb') as f:
    #     Image = 'f.read()'
    item = {

        'Image': filepath,
        'Name': Name.capitalize(),
        'Price': Price
    }
    PharmacyDB.append(item)
    # CreateItem = "INSERT INTO Items (Name,Image,Price) VALUES (%s,%s,%s)"
    # Item = [Name, Image, Price]
    # Database.execute(CreateItem, Item)
    # DatabaseConnection.commit()
    return request.url


@Pharmacy.route('/Items')
def Items():

    return PharmacyDB


OrdersDB = [

]


@Pharmacy.route('/PlaceOrder', methods=['POST'])
def PlaceOrder():
    OrdersDB.append({'name': request.get_json()['name'],
                     'date': request.get_json()['date'],
                     'phone': request.get_json()['phone'],
                     'address': request.get_json()['address'],
                     'status': request.get_json()['status'],
                     'sessionId': request.get_json()['SessionID'],
                     'products': TempStorageDB[request.get_json()['SessionID']],
                     })
    
    
    print(request.headers)
    print(request.get_json()['name'])
    return json.dumps({'Status':'Done'})


@Pharmacy.route('/Orders')
def Orders():
    return json.dumps(OrdersDB)
