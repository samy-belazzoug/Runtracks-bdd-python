import mysql.connector
from dotenv import load_dotenv
import os
import subprocess

load_dotenv()
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAMElp")

mydb = mysql.connector.connect(
    host = db_host,
    user = db_user,
    password = db_password
)
print("Connected.")

mycursor = mydb.cursor()
mycursor.execute("USE laplateforme")

sql = "INSERT INTO etage (nom,numero,superficie) VALUES (%s,%s,%s)"
val = [
    ("RDC",0,500),
    ("R+1",1,500)
]

#mycursor.executemany(sql,val)
#mydb.commit()

#print("Entries successfully added.")
#print(mycursor.rowcount,"was inserted.")

mycursor.execute("SELECT * FROM etage")
for x in mycursor:
    print(x,"\n")

sql = "INSERT INTO salle (nom,id_etage,capacite) VALUES (%s,%s,%s)"
val = [
    ("Lounge",1,100),
    ("Studio son",1,5),
    ("Broadcasting",2,50),
    ("Bocal pPeda",2,4),
    ("Coworking",2,80),
    ("Studio Video",2,5)
]

#mycursor.executemany(sql,val)
#mydb.commit()

#print("Entries successfully added.")
#print(mycursor.rowcount,"was inserted.")

mycursor.execute("SELECT * FROM salle")
for x in mycursor:
    print(x,"\n")

"""EXPORTATION DE LA BASE DE DONNEES"""

#nom du fichier de sauvegarde
backup_file = f"{db_name}_backup.sql"

#Construire la commande mysqldump
cmd = f"mysqldump -h {db_host} -u {db_user} -p{db_password} {db_name} > {backup_file}"

#Execution de la commande
try:
    subprocess.run(cmd,shell=True,check=True)
    print(f"Sauvegarde reussie : {backup_file}")
except subprocess.CalledProcessError as e:
    print(f"Erreur lors de l'export : {e}")