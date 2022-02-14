
import os
from flask_migrate import Migrate
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote_plus
from dotenv import load_dotenv
def create_app(test_config=None):
    projet_iai = Flask(__name__, instance_relative_config=True)
load_dotenv()
projet_iai=Flask(__name__)

motdepasse=quote_plus(os.getenv('password'))
hostname=os.getenv('host')

projet_iai.config['SQLALCHEMY_DATABASE_URI']='postgres://fdabotokurwmjr:5240f118c58464662c94a9590dc8e5414084ffe3d8bae2f191ee811b6db87214@ec2-54-158-26-89.compute-1.amazonaws.com:5432/dfvq3u9a7iqrqm'
projet_iai.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(projet_iai)
migrate=Migrate(projet_iai,db)
@projet_iai.after_request
def after_request(response):
 response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
 response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTION')
 return response
class Categorie(db.Model):
    __tablename__='CATEGORIES'
    id=db.Column(db.Integer,primary_key=True)
    libelle_categorie=db.Column(db.String(50),nullable=False)
    Livre=db.relationship("Livre",backref="Categorie",lazy=True)
    def __init__(self,libelle_categorie):
        self.libelle_categorie=libelle_categorie
    def insert(self):
        db.session.add(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def format(self):
        return{
        'ID': self.id,
        'Libelle categories :': self.libelle_categorie
        }
class Livre(db.Model):
    __tablename__='LIVRES'
    id=db.Column(db.Integer,primary_key=True,unique=True)
    isbn=db.Column(db.String(30),nullable=False,unique=True)
    titre=db.Column(db.String(40),nullable=False)
    date_publication=db.Column(db.DateTime,nullable=False)
    auteur=db.Column(db.String(50),nullable=False)
    editeur=db.Column(db.String(50),nullable=False)
    categorie_id=db.Column(db.Integer,db.ForeignKey(Categorie.id),nullable=False)
    def __init__(self,isbn,titre,date_publication,auteur,editeur,categorie_id):
        self.isbn=isbn,
        self.titre=titre,
        self.date_publication=date_publication,
        self.auteur=auteur,
        self.editeur=editeur,
        self.categorie_id=categorie_id

    def insert(self):
        db.session.add(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def format(self):
        return{
        'ID': self.id,
        'ISBN': self.isbn,
        'TITRE': self.titre,
        'Date de la publication' :self.date_publication,
        'AUTEUR ' : self.auteur,
        'EDITEUR ': self.editeur,
        'categorie': self.categorie_id
        }
db.create_all()

@projet_iai.route('/')
def BG():
    return 'ANANI azui'
#################################################  
        # la liste des livres
#################################################
@projet_iai.route('/Livres',methods=['GET'])
def liste_livre():
        try:
            livre = Livre.query.all()
            livre=[l.format() for l in livre]
            return jsonify(livre)
        except:
            abort(404)
        finally:
            db.session.close()
#################################################  
        # Chercher un livre  par son id
#################################################
@projet_iai.route('/Livres/<int:id>',methods=['GET'])
def rechercher_livre_id(id):
    livre = Livre.query.get(id)
    if livre is None:
        abort(404)
    else:
        return livre.format()
           
#####################################
  #la liste des categories
#####################################
@projet_iai.route('/categories',methods=['GET'])
def liste_categories():
        try:
            categorie = Categorie.query.all()
            categorie=[l.format() for l in categorie]
            return jsonify(categorie)
        except:
            abort(404)
        finally:
            db.session.close()
################################################
  # Lister la liste des livres d'une categorie
################################################
@projet_iai.route('/categories/<int:id>/Livres',methods=['GET'])
def listes_livres_categorie(id):
    try:
        liste2=Livre.query.filter_by(categorie_id=id).all()
        liste2=[l.format() for l in liste2]
        return jsonify(liste2)
    except:
       abort(404)
    finally:
        db.session.close()
###############################################
   #chercher une categorie par son id
###############################################
@projet_iai.route('/categories/<int:id>',methods=['GET'])
def rechercher_categorie_id(id):
    categorie = Categorie.query.get(id)
    if categorie is None:
        abort(404)
    else:
        return categorie.format()
############################
    # Supprimer un livre
############################
@projet_iai.route('/Livres/<int:id>', methods=['DELETE'])
def del_livre(id):
        try:
            livre = Livre.query.get(id)
            livre.delete()
            return jsonify({
                'success': True,
                'id_Livre': id,
                'new_total': livre.query.count()
            })
        except:
            abort(404)
        finally:
            db.session.close()

#############################
    # Supprimer une categorie
#############################

@projet_iai.route('/categories/<int:id>', methods=['DELETE'])
def del_categories(id):
        try:
            categorie = Categorie.query.get(id)
            categorie.delete()
            return jsonify({
                'success': True,
                'status': 200,
                'id_cat': id,
                'total_categories': Categorie.query.count()
            })
        except:
            abort(404)
        finally:
            db.session.close()

###########################################
    # Modifier les informations d'un livre
###########################################

@projet_iai.route('/Livres/<int:id>', methods=['PATCH'])
def modifier_livre(id):
        body = request.get_json()
        livre = Livre.query.get(id)
        try:
            if 'titre' in body and 'auteur' in body and 'editeur' in body:
                livre.titre = body['titre']
                livre.auteur = body['auteur']
                livre.editeur = body['editeur']
                livre.update()
                return jsonify({
                'success':True,
                 'Livre' :livre.format()
                 })
        except:
            abort(404)
        finally:
           db.session.close()
########################################
 # Modifier le libellé d'une categorie
########################################

@projet_iai.route('/categories/<int:id>', methods=['PATCH'])
def change_name(id):
        body = request.get_json()
        cate = Categorie.query.get(id)
        try:
            if 'libelle_categorie' in body:
                cate.libelle_categorie = body['libelle_categorie']
                cate.update()
                return jsonify({
                'success':True,
                 'categorie': cate.format()
                })
        except:
            abort(404)
