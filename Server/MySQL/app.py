import base64
import json
import os
from flask import Blueprint, jsonify, redirect, request, current_app
import mysql.connector
from werkzeug.utils import secure_filename
from PIL import Image as _Image

UPLOAD_FOLDER = '/DB/Images'

Pharmacy = Blueprint('Admin', __name__)


PharmacyDB=[]

@Pharmacy.route('/AddItem', methods=['POST', 'GET'])
def Additem():
    Name = request.form['Name']
    Image = request.files['Image']
    Price = request.form['Price']

    filename = secure_filename(Image.filename)
    filepath = current_app.config['UPLOAD_FOLDER']+'/'+filename
    Image.save(filepath)
    
    im=_Image.open(filepath)
    resized=im.resize((500, 500))
    resized.save(filepath)
    
    
    # with open(filepath, 'rb') as f:
    #     Image = 'f.read()'
    item={
        
    'Image':filepath,
    'Name':Name,
    'Price':Price
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
