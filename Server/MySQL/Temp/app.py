import base64
import json
import os
from flask import Blueprint, jsonify, redirect, request, current_app
import mysql.connector
from werkzeug.utils import secure_filename
from PIL import Image as _Image

UPLOAD_FOLDER = '/DB/Images'

Pharmacy = Blueprint('Admin', __name__)


ALLconfig = [
    {
        'host': "localhost",
        'user': "root",
        'password': "ROOT",
        'database': "Pharmacy"

    },
    {
        'host': "pharmacy-2889.7s5.cockroachlabs.cloud",
        'user': "rhysjosmin",
        'password': "ta_SLcvMvDt-YlCC-MSH2Q",
        'database': "defaultdb",
        'port': 26257

    },
]
config = ALLconfig[0]
try:
    DatabaseConnection = mysql.connector.connect(
        host=config['host'],
        user=config['user'],
        password=config['password'],


        database=config['database']
    )
except:
    DatabaseConnection = mysql.connector.connect(
        host=config['host'],
        user=config['user'],
        password=config['password'],
    )

    Database = DatabaseConnection.cursor()
    Database.execute('CREATE DATABASE Pharmacy')
    DatabaseConnection.commit()
    DatabaseConnection.close()
    DatabaseConnection = mysql.connector.connect(
        host=config['host'],
        user=config['user'],
        password=config['password'],
        database=config['database']
    )
    Database = DatabaseConnection.cursor()
    Database.execute(
        'CREATE TABLE Items (Name VARCHAR(255), Image LONGBLOB, Price VARCHAR(255))')
    DatabaseConnection.commit()
    DatabaseConnection.close()
finally:
    DatabaseConnection = mysql.connector.connect(
        host=config['host'],
        user=config['user'],
        password=config['password'],
        database=config['database']
    )

    Database = DatabaseConnection.cursor()


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
    
    
    with open(filepath, 'rb') as f:
        Image = f.read()
    CreateItem = "INSERT INTO Items (Name,Image,Price) VALUES (%s,%s,%s)"
    Item = [Name, Image, Price]
    Database.execute(CreateItem, Item)
    DatabaseConnection.commit()
    return request.url


@Pharmacy.route('/Items')
def Items():
    Database.execute("SELECT * FROM Items")

    Results = Database.fetchall()

    items = []
    for row in Results:
        item = {
      
            'Name': row[0],
            'Image': base64.b64encode(row[1]).decode('utf-8'),
            'Price': row[2],
        }
        items.append(item)

    return jsonify(items)


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
