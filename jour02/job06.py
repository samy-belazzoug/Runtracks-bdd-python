import mysql.connector

mydb = mysql.connector.connect(

    host = "localhost",
    user = "root",
    password = ""

)

mycursor = mydb.cursor()
mycursor.execute("USE laplateforme;")

mycursor.execute("SELECT SUM(capacite) FROM salle;")
myresult = mycursor.fetchone()
resultat = myresult[0]
print("La capacité de toutes les salles est de",resultat)