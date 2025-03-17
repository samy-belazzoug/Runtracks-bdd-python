import mysql.connector

mydb = mysql.connector.connect(

    host = "localhost",
    user = "root",
    password = "F1W11Bel13002_"

)
mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE workinrh;")
#mycursor.execute("SHOW DATABASES;")
# for x in mycursor:
#     print(x)
mycursor.execute("USE workinrh;")

#mycursor.execute("CREATE TABLE employe(id INT AUTO_INCREMENT PRIMARY KEY,nom VARCHAR(255),prenom VARCHAR(255),salaire DECIMAL,id_service INT);")
sql = "INSERT INTO employe (prenom,nom,salaire) VALUES (%s, %s, %s)"
val = [
    ("John","Highway",3400),
    ("Ulys","Himmer",2900),
    ("Pascal","Grafrer",3300),
    ("Lewis","Enderbourg",1890),
    ("Samy","Belazzoug",774),
    ("Joris","Marinktov",3600),
    ("Xio","Junpang",3200),
    ("Eric","Ngambuyen",2800),
    ("Oren","Ölsmussen",5000),
    ("Mac","Freddor",3900),
    ("Iris","Belguysen",3100),
    ("Mala","Migatun",3010),
    ("Maurrisse","Holoré",3600),
    ("Mohammed","Messayen",3900),
    ("Jim","Spieler",3000),
    ("Khaled","En-Anas",4000)
]


#mycursor.execute("CREATE TABLE service(id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255));")

sql1 = "INSERT INTO service (nom) VALUES (%s)"
val1 = [
    [("Senior Software Developper")],
    [("Software Developper")],
    [("Data Analyst")],
    [("Human Ressources")],
    [("Software Developper Apprentice")],
    [("Senior Full-stack Developper")],
    [("Business developper")],
    [("Junior ML engineer")],
    [("Chief information security officer")],
    [("Pentester")],
    [("Junior Python developper")],
    [("SEO optimiser")],
    [("DevOps engineer")],
    [("Database administrator")],
    [("Graphic designer")],
    [("Senior Data Scientist")]
]


mycursor.execute("DROP TABLE service")
mycursor.execute("DROP TABLE employe")

mycursor.execute("CREATE TABLE service(id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255));")
mycursor.execute("CREATE TABLE employe(id INT AUTO_INCREMENT PRIMARY KEY,nom VARCHAR(255),prenom VARCHAR(255),salaire DECIMAL,id_service INT);")
sql2 = "DELETE * FROM service"
mydb.commit()
sql3 = "DELETE * FROM employe"
mydb.commit()

#EMPLOYE
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount,"was inserted.")

#SERVICE
mycursor.executemany(sql1,val1)
mydb.commit()
print(mycursor.rowcount,"was inserted.")

mycursor.execute("SELECT * FROM employe WHERE salaire > 3000")
for x in mycursor:
    print(x)

mycursor.execute("SELECT * FROM service")
for x in mycursor:
    print(x)

sql = "SELECT \
  employe.nom AS user, \
  service.nom AS profession \
  FROM employe \
  RIGHT JOIN service ON employe. = employe.nom"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)