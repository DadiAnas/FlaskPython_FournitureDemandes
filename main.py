# main.py

from flask import Blueprint, render_template
from .auth import is_logged_in,getcookies,not_logged_in,db,cursor
from .statistics import line_labels, line_values,title
import pygal
main = Blueprint('main', __name__)


@main.route('/')
@not_logged_in
def index():
    return render_template('login.html')

@main.route('/administrateur')
@is_logged_in
def administrateur():
    return render_template('administrateur.html',current_user = getcookies('current_user'))

@main.route('/utilisateur')
@is_logged_in
def utilisateur():
    ''' ******************** demandes details ************************************** '''
    cursor.execute("select * from demandes where demandeur_id = '{}';".format(getcookies('user_id')))
    demandes = list(cursor.fetchall())


    produits = []
    quantites = []
    for row in demandes:
        cursor.execute("select produit_id,qte_demander from produits_demandes where demande_id = '{}'".format(row[0]))
        produits_id = list(cursor.fetchall())

        for rows in produits_id:
            quantites.append(rows[1])
            cursor.execute("select * from produits where produit_id ='{}' ".format(rows[0]))
            produit = cursor.fetchone()
            produits.append(produit)

    ''' ******************** Chart details ************************************** '''
    line_chart = pygal.HorizontalBar()
    line_chart.title = 'Statistiques'
    #get table of products id and all quantite demanded by user
    cursor.execute("SELECT produits.produit_designation,sum(produits_demandes.qte_demander) from users natural join produits natural join demandes natural join produits_demandes where users.user_id = '{}' and demandes.demandeur_id = '{}' and demandes.demande_statut = 'cloturée' group by produit_id;".format(getcookies('user_id'),getcookies('user_id')))
    productid_quantites = list(cursor.fetchall())

    #get products demanded description

    for product in productid_quantites:
        line_chart.add(str(product[0]), product[1])

    line_chart.render()
    graph_data = line_chart.render_data_uri()
    return render_template('utilisateur.html',
        graph_data = graph_data,
        current_user = getcookies('current_user'),
        user_nom = getcookies('user_nom'),
        user_prenom = getcookies('user_prenom'),
        user_id = getcookies('user_id'),
        produits=produits,
        quantites=quantites,
        demandes = demandes
                           )

@main.route('/magasinier')
@is_logged_in
def magasinier():
    cursor.execute("select * from demandes where demande_statut in ('chez le magasinier','cloturée');")
    demandes = list(cursor.fetchall())

    produits = []
    quantites = []
    users = []
    for row in demandes:
        cursor.execute("select produit_id,qte_demander from produits_demandes where demande_id = '{}'".format(row[0]))
        produits_id = list(cursor.fetchall())
        cursor.execute("select * from users where user_id = '{}'".format(row[1]))
        user = cursor.fetchone()
        users.append(user)
        for rows in produits_id:
            quantites.append(rows[1])
            cursor.execute("select * from produits where produit_id ='{}' ".format(rows[0]))
            produit = cursor.fetchone()
            produits.append(produit)


    cursor.execute("select * from produits;")
    Allproduits = list(cursor.fetchall())
    # charts ************************************
    treemap = pygal.Treemap()
    treemap.title = 'ARBRE DES DEMANDES DES ٍVALIDATEURS'

    cursor.execute("select distinct validateur_id from demandes")
    validateurs = cursor.fetchall()
    for validateur in validateurs:
        cursor.execute("select distinct users.user_nom,sum(produits_demandes.qte_demander) from users natural join demandes natural join produits_demandes where users.user_id = validateur_id and validateur_id = '{}' and demande_statut = 'cloturée' ".format(validateur[0]))
        nom_qte = cursor.fetchone()
        if nom_qte[1]:
            treemap.add(nom_qte[0], [nom_qte[1]])

    treemap.render()
    graph_data = treemap.render_data_uri()
    return render_template('magasinier.html',
                           current_user=getcookies('current_user'),
                           user_nom=getcookies('user_nom'),
                           user_prenom=getcookies('user_prenom'),
                           user_id=getcookies('user_id'),
                           demandes=demandes,
                           produits=produits,
                            Allproduits =Allproduits,
                           quantites=quantites,
                           users=users,
                           graph_data = graph_data,
                           )

@main.route('/validateur')
@is_logged_in
def validateur():
    cursor.execute("select * from demandes where validateur_id = '{}';".format(getcookies('user_id')))
    demandes = list(cursor.fetchall())

    produits = []
    quantites = []
    users = []
    for row in demandes:
        cursor.execute("select produit_id,qte_demander from produits_demandes where demande_id = '{}'".format(row[0]))
        produits_id = list(cursor.fetchall())

        cursor.execute("select * from users where user_id = '{}'".format(row[1]))
        user = cursor.fetchone()
        users.append(user)
        for rows in produits_id:
            quantites.append(rows[1])
            cursor.execute("select * from produits where produit_id ='{}' ".format(rows[0]))
            produit = cursor.fetchone()
            produits.append(produit)

    #charts ************************************
    pie_chart = pygal.Pie()
    pie_chart.title = 'Les demandes de votre equipe (en %)'

    cursor.execute("select distinct demandeur_id from demandes");
    demandeurs = cursor.fetchall()
    for demandeur in demandeurs:
        cursor.execute("select  users.user_nom,sum(qte_demander) from users natural join demandes as dd natural join produits_demandes as pd where dd.demande_id = pd.demande_id and dd.demandeur_id ='{}' and users.user_id = dd.demandeur_id and dd.demande_statut = 'cloturée' and dd.validateur_id = '{}' ".format(demandeur[0],getcookies('user_id')))
        nom_qte = cursor.fetchone()
        if nom_qte[1]:
            pie_chart.add(nom_qte[0],nom_qte[1])

    pie_chart.render()
    graph_data = pie_chart.render_data_uri()
    return render_template('validateur.html',
                           current_user=getcookies('current_user'),
                           user_nom=getcookies('user_nom'),
                           user_prenom=getcookies('user_prenom'),
                           user_id=getcookies('user_id'),
                           demandes = demandes,
                           produits = produits,
                           quantites = quantites,
                           users = users,
                           graph_data = graph_data)

@main.route('/profile')
@is_logged_in
def profile():
    return render_template('profile.html',
                           current_user=getcookies('current_user'),
                           user_nom=getcookies('user_nom'),
                           user_prenom=getcookies('user_prenom'),
                           user_id=getcookies('user_id'),
                           user_email=getcookies('user_email'),
                           user_fonction = getcookies('user_fonction')
                           )
