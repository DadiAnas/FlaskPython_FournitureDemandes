# auth.py

from flask import Blueprint,make_response, render_template, redirect, url_for, request, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
from . import save_product_image_folder

from . import db,cursor
from functools import wraps


auth = Blueprint('auth', __name__)


def getcookies(cookie_name):
    return str(request.cookies.get(cookie_name))

# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('auth.login'))
    return wrap

def not_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return redirect(url_for('main.%s'% request.cookies.get('current_user')))
        else:
            return f(*args, **kwargs)

    return wrap


@auth.route('/login')
@not_logged_in
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    matricule = request.form.get('matricule')
    password = request.form.get('password')
    print(password)

    if '@' in matricule:
        cursor.execute("SELECT EXISTS( select * from users where user_email=\"" + matricule + "\");")  # if a user is found, we want to redirect back to new_password page so user can try again
        user = cursor.fetchone()
        if  user[0] :
            cursor.execute("select * from users where user_email=\""+matricule+"\" ;")
            user = cursor.fetchone()
    else:
        cursor.execute("SELECT EXISTS( select * from users where user_id=\"" + matricule + "\");")  # if a user is found, we want to redirect back to new_password page so user can try again
        user = cursor.fetchone()
        if user[0]!=0:
            cursor.execute("select * from users where user_id=\"" + matricule + "\" ;")
            user = cursor.fetchone()
    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database

    if user[0] ==0 or not check_password_hash(user[6], password):
        flash('Les données sont incorrects.')
        return redirect(url_for('auth.login')) # if user doesn't exist or password is wrong, reload the page
    # if the above check passes, then we know the user has the right credentials
    session['logged_in'] = True

    # make cookies
    resp = make_response(redirect(url_for('main.%s' % user[len(user)-1])))

    resp.set_cookie("user_id", user[0])
    resp.set_cookie("current_user", user[len(user)-1])
    resp.set_cookie("user_nom", user[1])
    resp.set_cookie("user_prenom", user[2])
    resp.set_cookie("user_email", user[3])
    resp.set_cookie("user_fonction", user[4])
    resp.set_cookie("user_sup", user[5])

    return resp


@auth.route('/new_password')
@not_logged_in
def signup():
    return render_template('new_password.html')

@auth.route('/new_password', methods=['POST'])
@not_logged_in
def new_password():
    matricule = request.form.get('matricule')
    email = request.form.get('email')
    password = request.form.get('password')
    cpassword = request.form.get('cpassword')
    #verify matricule and email


    cursor.execute("SELECT EXISTS( select * from users where user_id=%s);",[matricule]) # if a user is found, we want to redirect back to new_password page so user can try again
    user = cursor.fetchone()
    if(user[0] == 0):
        flash('Votre maricule n\'existe pas dans la base de donnée veuillez contacter l\'administation')
        return redirect(url_for('auth.new_password'))
    else:
        cursor.execute("select * from users where user_id=%s;",[matricule])
        user = cursor.fetchone()
        if email != user[3]:
            flash("Email incorrect.")
            return redirect(url_for('auth.new_password'))
        if (password != cpassword) :
            flash("Veuillez entrer le même mot de passe dans les deux cases.")
            return redirect(url_for('auth.new_password'))
        # modify user password
        cursor.execute("UPDATE users SET user_password = '{}' WHERE user_id = '{}' ;".format(generate_password_hash(password, method='sha256'),matricule))
        # add the new user to the database

        db.commit()
        return redirect(url_for('auth.login'))




@auth.route('/add_user')
@is_logged_in
def add_new_user():
    return render_template('administrateur.html')


@auth.route('/add_user', methods=['POST'])
@is_logged_in
def add_user():

        matricule = request.form.get('matricule')
        nom = request.form.get('nom')
        prenom = request.form.get('prenom')
        email =  request.form.get('email')
        password = request.form.get('password')
        Serv_ou_etab = request.form.get('usertype')
        superieur = request.form.get('superieur')
        type = request.form.get('usertype')
        #verify
        cursor.execute("SELECT EXISTS( select user_id from users where user_id=\"" + matricule + "\");")  # if a user is found, we want to redirect back to new_password page so user can try again
        user = cursor.fetchone()
        if user[0] :
            flash("Il y a déja un utilisateur avec le même matricule")
            return redirect(url_for('auth.add_user'))

        # Execute
        cursor.execute("INSERT INTO users(user_id, user_nom, user_prenom, user_email,user_password, user_fonction,user_superieur_id,user_type) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",(matricule,nom,prenom,email,generate_password_hash(password,method='sha256'),Serv_ou_etab,superieur,type))
        # Commit to DB
        db.commit()
        flash("L'utilisateur est bien ajouter !", 'success')
        return redirect(url_for('auth.add_user'))

@auth.route("/modify_user",methods = ["Post"])
@is_logged_in
def modify_user():
    nom = request.form.get('nom')
    prenom = request.form.get('prenom')
    email = request.form.get('email')
    cursor.execute("update users set user_nom = '{}',user_prenom = '{}',user_email = '{}' where user_id = '{}' ".format(nom,prenom,email,getcookies('user_id')))

    db.commit()
    return redirect(url_for('auth.logout'))

@auth.route('/products_menu')
@is_logged_in
def products_menu():
    cursor.execute("SELECT * FROM produits;")
    products = tuple(cursor)
    return render_template('products.html',products=products,
                           current_user = request.cookies.get('current_user'))

@auth.route('/products_menu')
@is_logged_in
def products_rederict():
    return redirect(url_for('auth.products_menu'))

@auth.route('/find_product',methods=['POST'])
@is_logged_in
def search():
    productafind = request.form.get('productafind')
    query_string = "SELECT * FROM produits WHERE produit_designation LIKE %s ORDER BY produit_id ASC"
    cursor.execute(query_string, ('%' + productafind + '%',))
    foundedproducts = tuple(cursor)

    return render_template("find_product.html",products = foundedproducts,
                           current_user = request.cookies.get('current_user'))

@auth.route('/find_product')
@is_logged_in
def products_search():
    return redirect(url_for('auth.find_product'))

@auth.route('/view_demandes')
@is_logged_in
def view_demandes():
    query = "SELECT * From demandes where magasinier_id = %s Order by demande_date desc"
    cursor.execute(query, ('%' + getcookies('user_id') + '%',))
    demandes = tuple(cursor)

    return render_template("view_demandes.html",demandes = demandes,
                           current_user = request.cookies.get('current_user'))

@auth.route('/view_demandes')
@is_logged_in
def view_demandes_redirect():
    return redirect(url_for('auth.view_demandes'))

@auth.route('/demander')
@is_logged_in
def demander():
    cursor.execute('select * from produits where produit_id =%s'% str(getcookies('product_id')))
    product = cursor.fetchone()
    cursor.execute("select produit_stock_qte from produits where produit_id = '{}' ".format(getcookies('product_id')))
    qte = int(cursor.fetchone()[0])

    return render_template('/demander.html',
                           qte = qte,
                           product = product
                           ,product_id = getcookies('product_id'),
                           current_user = getcookies('current_user'))

@auth.route('/demander/product_id=<int:product_id>')
@is_logged_in
def demander_redirect(product_id):
    resp = make_response(redirect(url_for('auth.demander',product_id = product_id)))
    resp.set_cookie("product_id", str(product_id))
    return resp

@auth.route('/success',methods=['POST'])
@is_logged_in
def add_demande():
    qte = request.form.get('qte',type=int)
    cursor.execute("select produit_stock_qte from produits where produit_id = '{}' ".format(getcookies('product_id')))
    qte_total = int(cursor.fetchone()[0])
    if not isinstance(qte, int) or 0 > qte or qte > qte_total:
        flash("verifier la quantité demandée")
        return redirect(url_for('auth.demander',product_id = getcookies("product_id")))
    cursor.execute("INSERT INTO `demandes` (`demandeur_id`, `demande_statut`, `validateur_id`) VALUES ('{}', 'attente de validation', '{}');".format(getcookies('user_id'), getcookies('user_sup')))
    demande_id = cursor.lastrowid
    cursor.execute("INSERT INTO `gdemandes`.`produits_demandes` ( `demande_id`, `produit_id`, `qte_demander`) VALUES ('{}', '{}', '{}');".format(demande_id,getcookies('product_id'),qte))
    db.commit()
    flash("votre demande a été bien prise en compte")
    return redirect(url_for("auth.products_menu"))

@auth.route('/success')
@is_logged_in
def add_demmande_rederict():
    return redirect(url_for('auth.success'))


@auth.route('/valider=<int:demand_id>',methods = ["Post"])
@is_logged_in
def validee_redirect(demand_id):
    cursor.execute("UPDATE `demandes` SET `demande_statut` = 'chez le magasinier' WHERE (`demande_id` = '{}');".format(demand_id))
    db.commit()

    return redirect(url_for('main.%s'%getcookies('current_user')))

@auth.route('/refuser=<int:demand_id>',methods = ["Post"])
@is_logged_in
def refuser_redirect(demand_id):
    cursor.execute("UPDATE `gdemandes`.`demandes` SET `demande_statut` = 'refuser' WHERE (`demande_id` = '{}');".format(demand_id))
    db.commit()
    return redirect(url_for('main.validateur'))

@auth.route('/adv=<int:demand_id>',methods = ["Post"])
@is_logged_in
def adv_redirect(demand_id): #attend de validation
    cursor.execute("UPDATE `gdemandes`.`demandes` SET `demande_statut` = 'attente de validation' WHERE (`demande_id` = '{}');".format(demand_id))
    db.commit()
    return redirect(url_for('main.validateur'))

@auth.route('/annuler=<int:demand_id>',methods = ["Post"])
@is_logged_in
def annuler_redirect(demand_id):
    cursor.execute("DELETE FROM `gdemandes`.`demandes` WHERE (`demande_id` = '{}');".format(demand_id))
    cursor.execute("DELETE FROM `gdemandes`.`produits_demandes` WHERE (`demande_id` = '{}');".format(demand_id))
    db.commit()
    return redirect(url_for('main.%s'%getcookies("current_user")))

@auth.route('/cloturer=<int:demand_id>,produit=<int:product_id>,qte_clouturee=<int:qte_clouturee>',methods = ["Post"])
@is_logged_in
def cloturer_redirect(demand_id,product_id,qte_clouturee):
    cursor.execute("UPDATE `gdemandes`.`demandes` SET `demande_statut` = 'cloturée' WHERE (`demande_id` = '{}');".format(demand_id))
    cursor.execute("select produit_stock_qte from produits where produit_id = %s "%product_id)
    current_product_qte = cursor.fetchone()
    cursor.execute("update produits set produit_stock_qte = '{}' where produit_id = '{}'".format(current_product_qte[0]-qte_clouturee,product_id))
    db.commit()
    return redirect(url_for('main.magasinier'))

@auth.route("/upload=<int:product_id>",methods = ["Post"])
@is_logged_in
def upload(product_id):
    qte_to_add = request.form.get('product'+str(product_id))
    cursor.execute("update produits set produit_stock_qte = '{}' where produit_id = '{}'".format(str(qte_to_add),product_id))

    try: 
        file = request.files['file']
    except:
        file= None
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(save_product_image_folder, filename))
        cursor.execute("update produits set produit_picture = '{}' where produit_id = '{}'".format('/static/styles/images/products/'+filename,product_id))
        return redirect(url_for('main.magasinier'))

    return redirect(url_for('main.magasinier'))

@auth.route("/add_new_product",methods = ["Post"])
@is_logged_in
def add_new_product():
    produit_categorie = request.form.get('newcategorie')
    produit_serial = request.form.get('newserial')
    produit_designation = request.form.get('newdesignation')
    produit_stock_qte = request.form.get('newqte')
    cursor.execute("INSERT INTO produits ( produit_categorie, produit_serial, produit_designation, produit_stock_qte) VALUES( %s, %s, %s, %s);",( produit_categorie, produit_serial, produit_designation, produit_stock_qte))

    try:
        file = request.files['file']
    except:
        file = None
    if file:
        filename = secure_filename(file.filename)
        try:
            file.save(os.path.join(save_product_image_folder, filename))
        except:
            pass
        product_id = cursor.lastrowid
        cursor.execute("update produits set produit_picture = '{}' where produit_id = '{}'".format('/static/styles/images/products/'+filename,product_id))
        db.commit()
        return redirect(url_for('main.magasinier'))
    db.commit()
    return redirect(url_for('main.magasinier'))

@auth.route("/delete_product=<int:product_id>",methods = ["Post"])
@is_logged_in
def delete_product(product_id):
    print(product_id)
    cursor.execute("delete from produits where produit_id ='{}' ".format(product_id))
    db.commit()
    return redirect(url_for('main.magasinier'))

@auth.route('/logout')
@is_logged_in
def logout():
    session.clear()
    resp = make_response(redirect(url_for('auth.login')))

    resp.set_cookie("user_id", expires=0)
    resp.set_cookie("current_user", expires=0)
    resp.set_cookie("user_nom",expires=0)
    resp.set_cookie("user_prenom", expires=0)
    resp.set_cookie("user_email", expires=0)
    resp.set_cookie("user_fonction", expires=0)
    resp.set_cookie("user_sup", expires=0)
    resp.set_cookie("product_id", expires=0)
    return resp