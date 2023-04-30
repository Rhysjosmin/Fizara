import mysql.connector

def DeleteDB_Pharmacy():
    DatabaseConnection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ROOT",

    )

    DB=DatabaseConnection.cursor()
    DB.execute('DROP DATABASE Pharmacy')
    print('Database Deleted')
def B():
    DatabaseConnection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ROOT",
        database="Pharmacy"
    )

    DB=DatabaseConnection.cursor()
    DB.execute('SELECT * FROM Items')
    r=DB.fetchall()
    print(r)
    
    
def C():
    # "ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY"
    DatabaseConnection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ROOT",
        database="Pharmacy"
    )

    DB=DatabaseConnection.cursor()
    DB.execute("SELECT Id FROM Items")
    r=DB.fetchall()
    print(r)
DeleteDB_Pharmacy()