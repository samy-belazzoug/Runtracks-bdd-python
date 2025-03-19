import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

mydb = mysql.connector.connect(
    host = db_host,
    user = db_user,
    password = db_password)
print("Connected.")

mycursor = mydb.cursor()
mycursor.execute("USE laplateforme")

mycursor.execute("CREATE TABLE etage (id INT AUTO_INCREMENT,nom VARCHAR(255),numero INT,superficie INT, PRIMARY KEY (id))")
mycursor.execute("CREATE TABLE salle (id INT AUTO_INCREMENT,nom VARCHAR(255),id_etage INT,capacite INT,PRIMARY KEY (id))")
print("Table successfully created.")