import base64
import json
import os
from flask import Blueprint, jsonify, redirect, request, current_app
import mysql.connector
from werkzeug.utils import secure_filename
from PIL import Image as _Image

UPLOAD_FOLDER = '/DB/Images'

Pharmacy = Blueprint('Admin', __name__)


PharmacyDB = [
    {"Image": "./Server/DB/Images/polyethylene-glycol-250x250.webp",
    "Name": "Polyethylene glycol pegred powder",
    "Price": "180"},
    {"Image": "./Server/DB/Images/novorapid-flexpens-500x500.webp",
    "Name": "Novorapid Flexpens",
    "Price": "2050.3"},
    {"Image": "./Server/DB/Images/pediasure-complete-500x500.webp",
    "Name": "Pediasure Complete",
    "Price": "750"},
    {"Image": "./Server/DB/Images/hcg-pregnancy-test-kit-500x500.webp",
    "Name": "Pregnancy Test Kit",
    "Price": "453"},
    {"Image": "./Server/DB/Images/health-d-500x500 (1).webp",
    "Name": "Health-D",
    "Price": "500"},
    {"Image": "./Server/DB/Images/cinnarizine-tablets-500x500.webp",
    "Name": "Cinnarizine Tablets",
    "Price": "200"},
    {"Image": "./Server/DB/Images/coxiblu-90-tablets-500x500.webp",
    "Name": "Coxiblu 90 Tablets",
    "Price": "300"},
    {"Image": "./Server/DB/Images/Paracetamol-500-MG-Tablet-manufcaturer-india-Taj-Life-Sciences-6-scaled.webp",
    "Name": "Paracetamol-500-MG-Tablet",
    "Price": "260"},
    {"Image": "./Server/DB/Images/rosuvastatin-10mg-fenofibrate-145mg-medicine-500x500.webp",
    "Name": "Rosuvastatin 10mg Fenofibrate 145mg Medicine",
    "Price": "300"},
    {"Image": "./Server/DB/Images/atazor-200-tablets-500x500.webp",
    "Name": "Atazor 200 Tablets",
    "Price": "300"},
   
]


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
    # Database.execute("SELECT * FROM Items")

    # Results = Database.fetchall()

    # items = []
    # for row in Results:
    #     item = {

    #         'Name': row[0],
    #         'Image': base64.b64encode(row[1]).decode('utf-8'),
    #         'Price': row[2],
    #     }
    #     items.append(item)

    return PharmacyDB


# @app.route('/api/items')
# def api_items():
#     # Execute the SQL query to retrieve all items
#     cursor = mydb.cursor()
#     cursor.execute("SELECT * FROM Items")
#     result = cursor.fetchall()

#     # Convert the query result to a list of dictionaries
#     items = []
#     for row in result:
#         item = {
#             'Name': row[0],
#             'Image': base64.b64encode(row[1]).decode('utf-8'),
#             'Price': row[2]
#         }
#         items.append(item)

#     # Return the data as JSON
#     return jsonify(items)
