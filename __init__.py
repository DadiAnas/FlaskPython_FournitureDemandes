# init.py
import mysql.connector as mysql
from flask import Flask
from flask_login import LoginManager 
from flask_material import Material
from os import curdir
# init SQLAlchemy so we can use it later in our models
save_product_image_folder = curdir+"/static/styles/images/products/"
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
cursor = db.cursor(buffered=True)

def create_app():
    app = Flask(__name__, static_url_path='/static')
    Material(app)
    app.config['UPLOAD_FOLDER'] = '/static/styles/images/products'
    app.config['MAX_CONTENT_PATH'] = '25,165,824'
    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        cursor = db.cursor()
        # since the user_id is just the primary key of our user table, use it in the query for the user
        cursor.execute("select * from users where matricule="+user_id+" ;")
        for row in cursor:
            return row

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

