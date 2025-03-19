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
#mycursor.execute("CREATE DATABASE working")
mycursor.execute("USE working")

#mycursor.execute("CREATE TABLE employe (id INT AUTO_INCREMENT,nom VARCHAR(255),prenom VARCHAR(255),salaire DECIMAL(2),id_service INT,PRIMARY KEY (id))")
#mycursor.execute("ALTER TABLE employe MODIFY COLUMN salaire DECIMAL(6,2)")

sql = "INSERT INTO employe (nom,prenom,salaire,id_service) VALUES (%s,%s,%s,%s)"
val = [
    ("Belazzoug","Samy",774,5),
    ("Serreau","Phillipe",1900,4),
    ("Kleinburg","Nico",2400,3),
    ("Yang","Xin",3350,2),
    ("Oyarzabal","Moreno",5000,1)
]

#mycursor.executemany(sql,val)
#mydb.commit()

# print("Entries successfully added.")
# print(mycursor.rowcount,"was inserted.")

# mycursor.execute("SELECT * FROM employe WHERE salaire > 3000")
# for x in mycursor:
#     print(x,"\n")

#mycursor.execute("CREATE TABLE service (id INT AUTO_INCREMENT,nom VARCHAR(255),PRIMARY key (id))")
data = ("INSERT INTO service (nom) VALUES (%s)")
values = [
    [('Chief Technical Officier')],
    [('Lead developper')],
    [('Software developper')],
    [('Junior developper')],
    [('Apprentice Software Developper')]
]

#mycursor.executemany(data,values)
#mydb.commit()

# print("Entries successfully added.")
# print(mycursor.rowcount,"was inserted.")

#mycursor.execute("ALTER TABLE service ADD FOREIGN key (id) REFERENCES employe(id)")


#mycursor.execute("SELECT * FROM employe")
joining = "SELECT employe.nom AS employe, service.nom AS profession FROM employe INNER JOIN service ON employe.id_service = service.id" 

mycursor.execute(joining)
myresult = mycursor.fetchall()

for x in myresult:
    print(x,"\n")

class employe:
    def __init__(self):
        pass