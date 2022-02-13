# Livre API VERSION 1
l'API nous permettra de gerer les livres d'une bibliothèque.  
## Commençons

### Installation des Dépendances

#### Python 3.10.1
#### pip 21.2.4 from C:\Users\hp\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10.1)

Suivez les instructions suivantes pour installer l'ancienne version de python sur la plateforme [python docs](https://www.python.org/downloads/windows/#getting-and-installing-the-latest-version-of-python)

#### Dépendances de PIP

Pour installer les dépendances, rentrer dans le dossier projet_iai et ouvrer votre cmd puis exécuter la commande suivante:

```bash ou powershell ou cmd
pip install -r requirement.txt
or
pip3 install -r requirement.txt
```

Nous passons donc à l'installation de tous les packages se trouvant dans le fichier `requirement.txt`.

##### clé de Dépendances

- [Flask](http://flask.pocoo.org/)  est un petit framework web Python léger, qui fournit des outils et des fonctionnalités utiles qui facilitent la création d’applications web en Python.

- [SQLAlchemy](https://www.sqlalchemy.org/) est un toolkit open source SQL et un mapping objet-relationnel écrit en Python et publié sous licence MIT. SQLAlchemy a opté pour l'utilisation du pattern Data Mapper plutôt que l'active record utilisés par de nombreux autres ORM

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Démarrer le serveur

Pour démarrer le serveur sur Linux ou Mac, executez:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
Pour le démarrer sur Windows, executez:

```bash
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
``` 

## API REFERENCE

Getting starter

Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://localhost:5000; which is set as a proxy in frontend configuration.

## Type d'erreur
Les erreurs sont renvoyées sous forme d'objet au format Json:
{
    "success":False
    "error": 404
    "message":"Ressource non disponible"
}

L'API vous renvoie 4 types d'erreur:
. 400: Bad request ou ressource non disponible
. 500: Internal server error
. 404: Not found

## Endpoints
. ## GET/Livres

    GENERAL:
        Cet endpoint retourne la liste des objets livres 
    
        
    EXEMPLE: curl http://localhost:5000/Livres
```
        {
    "Livres":[
    {
        "AUTEUR ": "Ferdinand Oyono",
        "Date de la publication": "Mon, 25 Dec 2000 00:00:00 GMT",
        "EDITEUR ": "gbemou",
        "ID": 2,
        "ISBN": "10SS",
        "TITRE": "Le vieux nègre et la médaille",
        "categorie": 1
    },
    {
        "AUTEUR ": "gbemou",
        "Date de la publication": "Sun, 10 Dec 2006 00:00:00 GMT",
        "EDITEUR ": "florent",
        "ID": 7,
        "ISBN": "14gb",
        "TITRE": "Sous l'orage",
        "categorie": 2
    },
    {
        "AUTEUR ": "Ferdinand oyono",
        "Date de la publication": "Sun, 10 Dec 2006 00:00:00 GMT",
        "EDITEUR ": "GBEMOU",
        "ID": 10,
        "ISBN": "13gb",
        "TITRE": "le vieux nègre et la medaille",
        "categorie": 2
    }
]
```

.##GET/Livres(id)
  GENERAL:
  Cet endpoint permet de récupérer les informations d'un livre particulier s'il existe par le biais de l'ID.

    EXEMPLE: http://localhost:5000/books/2
```
 {
    "AUTEUR ": "Ferdinand Oyono",
    "Date de la publication": "Mon, 25 Dec 2000 00:00:00 GMT",
    "EDITEUR ": "gbemou",
    "ID": 2,
    "ISBN": "10SS",
    "TITRE": "Le vieux nègre et la médaille",
    "categorie": 1
}
```


. ## DELETE/Livres(id)

    GENERAL:
        Supprimer un livre si l'ID existe. Retourne l'ID du livre supprimé, la valeur du succès et le nombre de livres qui restent .

        EXEMPLE: curl -X DELETE http://localhost:5000/Livres/10
{
    "id_Livre": 10,
    "new_total": 2,
    "success": true
}
```

. ##PATCH/Livres(id)
  GENERAL:
  Cet endpoint permet de mettre à jour, le titre, l'auteur, et l'éditeur du livre.
  Il retourne un livre mis à jour.

  EXEMPLE.....Avec Patch
  ``` curl -X PATCH http://localhost:5000/books/1 -H "Content-Type:application/json" -d '{
  "titre":"une vie de boy",
  "auteur":"Ferdinand Oyono",
  "editeur":"Florent"
}
  ```
  ```
 {
    "Livre": {
        "AUTEUR ": "Ferdinand Oyono",
        "Date de la publication": "Mon, 25 Dec 2000 00:00:00 GMT",
        "EDITEUR ": "Florent",
        "ID": 2,
        "ISBN": "10SS",
        "TITRE": "une vie de boy",
        "categorie": 1
    },
    "success": true
}
    ```

. ## GET/categories

    GENERAL:
        Cet endpoint retourne la liste des categories de livres. 
    
        
    EXEMPLE: curl http://localhost:5000/categories

[
    {
        "ID": 1,
        "Libelle categories :": "roman"
    },
    {
        "ID": 4,
        "Libelle categories :": "roman"
    },
    {
        "ID": 5,
        "Libelle categories :": "roman"
    },
    {
        "ID": 6,
        "Libelle categories :": "press"
    },
    {
        "ID": 7,
        "Libelle categories :": "loisirs"
    },
    {
        "ID": 2,
        "Libelle categories :": "bande dessinee"
    }
]
```

.##GET/categories(id)
  GENERAL:
  Cet endpoint permet de récupérer les informations d'une categorie si elle existe par le biais de l'ID.

    EXEMPLE: http://localhost:5000/categories/2
```
{
    "ID": 2,
    "Libelle categories :": "bande dessinee"
}
```

. ## DELETE/categories (categories_id)

    GENERAL:
        Supprimer une categorie si l'ID existe. Retourne l'ID da la catégorie supprimé, la valeur du succès et le nouveau total.
        NB: si il exite un livre qui appartient à la categorie qu'on veut supprimer on aura une erreur 404 car il ne faudrait pas 
        oublier la contrainte de clé primaire.On ne peut pas avoir un livre qui existe dans une categorie inexistante.   

        EXEMPLE: curl -X DELETE http://localhost:5000/categories/5
```
{
    "id_cat": 5,
    "status": 200,
    "success": true,
    "total_categories": 5
}
```

. ##PATCH/categories(id)
  GENERAL:
  Cet endpoint permet de mettre à jour le libelle ou le nom de la categorie.
  Il retourne la categorie avec une nouvelle nom.

  EXEMPLE.....Avec Patch
  ``` curl -X PATCH 'http://localhost:5000/categories/4' -H "Content-Type:application/json" -d '{
    "libelle_categorie":"Livre de programmation"
}
  ```
  ```
{
    "categorie": {
        "ID": 2,
        "Libelle categories :": "Livre de programmation"
    },
    "success": true
}

.##GET/categories(id)/Livres
  GENERAL:
  Cet endpoint permet de lister les livres appartenant à une categorie donnée.
  Il renvoie la classe de la categorie et les livres l'appartenant.

    EXEMPLE: http://localhost:5000/categories/2/Livres
```
[
    {
        "AUTEUR ": "gbemou",
        "Date de la publication": "Sun, 10 Dec 2006 00:00:00 GMT",
        "EDITEUR ": "florent",
        "ID": 7,
        "ISBN": "14gb",
        "TITRE": "Sous l'orage",
        "categorie": 2
    }
]
```

