from random import randint
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector as mysql

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
	
def randomfonction():
	a = ['service', 'etablissement']
	return a[randint(0,1)]
#admin admin@uemf.ma:adminadmin
passw = generate_password_hash("adminadmin",method='sha256')
cursor.execute("INSERT INTO users(user_id, user_nom, user_prenom, user_email,user_fonction, user_superieur_id,user_password,user_type) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",("admin","admin","admin","admin@uemf.ma",'admin','admin',passw,'administrateur'))
#magasinier magasinier1@uemf.ma:magasinier1
for i in range(1,3):
    cursor.execute("INSERT INTO users(user_id, user_nom, user_prenom, user_email,user_fonction, user_superieur_id,user_password,user_type) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",("magasinier"+str(i),"magasinier_nom"+str(i),"magasinier_prenom"+str(i),"magasinier"+str(i)+"@uemf.ma",randomfonction(),'magasinier'+str(i),generate_password_hash("magasinier"+str(i),method='sha256'),'magasinier'))

#validateur validateur1@uemf.ma:validateur1
for i in range(1,3):
    cursor.execute("INSERT INTO users(user_id, user_nom, user_prenom, user_email,user_fonction, user_superieur_id,user_password,user_type) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",("validateur"+str(i),"validateur_nom"+str(i),"validateur_prenom"+str(i),"validateur"+str(i)+"@uemf.ma",randomfonction(),'validateur'+str(i),generate_password_hash("validateur"+str(i),method='sha256'),'validateur'))

#utilisateur 15 user// user1@uemf.ma:useruser1
for i in range(1,15):
    if i<=5:
        cursor.execute("INSERT INTO users(user_id, user_nom, user_prenom, user_email,user_fonction, user_superieur_id,user_password,user_type) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",("user"+str(i),"user_nom"+str(i),"user_prenom"+str(i),"user"+str(i)+"@uemf.ma",randomfonction(),'validateur1',generate_password_hash("useruser"+str(i),method='sha256'),'utilisateur'))
    elif i>5 and i<=10:
        cursor.execute("INSERT INTO users(user_id, user_nom, user_prenom, user_email,user_fonction, user_superieur_id,user_password,user_type) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",("user"+str(i),"user_nom"+str(i),"user_prenom"+str(i),"user"+str(i)+"@uemf.ma",randomfonction(),'validateur2',generate_password_hash("useruser"+str(i),method='sha256'),'utilisateur'))
    else:
        cursor.execute("INSERT INTO users(user_id, user_nom, user_prenom, user_email,user_fonction, user_superieur_id,user_password,user_type) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",("user"+str(i),"user_nom"+str(i),"user_prenom"+str(i),"user"+str(i)+"@uemf.ma",randomfonction(),'validateur3',generate_password_hash("useruser"+str(i),method='sha256'),'utilisateur'))
    
db.commit()
db.close()