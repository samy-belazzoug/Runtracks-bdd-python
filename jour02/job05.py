import mysql.connector

mydb = mysql.connector.connect(

    host = "localhost",
    user = "root",
    password = ""

)

mycursor = mydb.cursor()
mycursor.execute("USE laplateforme;")

mycursor.execute("SELECT SUM(superficie) FROM etage;")
myresult = mycursor.fetchone()
resultat = myresult[0]
print("La superficie de La Plateforme est de",resultat,"m2")