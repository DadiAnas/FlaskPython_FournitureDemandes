import mysql.connector as mysql
 

F_number=5

def db():
    host = "localhost"
    user = "root"
    password = ""#settings.MYSQL_DATABASE_PASSWORD
    database = 'Gdemandes'

    config = {
        'user': user,
        'password': password,
        'host': host,
        'database': database,
        'raise_on_warnings': True
    }

    return  mysql.connect(**config)
db = db()
cursor = db.cursor()

for i in range(1,F_number):
    cursor.execute("INSERT INTO fournisseur(fournisseur_id,fournisseur_nom,fournisseur_phone,fournisseur_email,fournisseur_website,fournisseur_address) VALUES(%s, %s, %s, %s, %s, %s);",(str(i),'fournisseur'+str(i),'212'+str(i),'email@'+str(i)+'.com','www/'+str(i),'N'+str(i)))
db.commit()  
db.close()