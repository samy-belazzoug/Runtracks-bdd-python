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
    password = db_password
)
print("Connected.")

mycursor = mydb.cursor()
mycursor.execute("USE laplateforme")

mycursor.execute("SELECT nom,capacite FROM salle")
print("Successful.")
for x in mycursor:
    print(x,"\n")