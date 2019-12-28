import pandas as pd
import mysql.connector as mysql
from random import randint

data = pd.read_csv('products.csv')

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


for i in range(1,len(data)):
    cursor.execute("INSERT INTO produits (produit_id, produit_categorie, produit_serial, produit_picture, produit_designation, produit_stock_qte, fournisseur_id) VALUES(%s, %s, %s, %s, %s, %s, %s);",(str(data.id_p.iloc[i]),str(data.designation.iloc[i]),str(data.product_serial.iloc[i]),"/static/styles/images/products/"+str(data.product_serial.iloc[i])+'.jpg',str(data.product_description.iloc[i]),str(randint(1,30)),str(data.f_id.iloc[i])))
db.commit()    
db.close()