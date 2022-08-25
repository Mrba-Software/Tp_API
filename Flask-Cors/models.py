import os
from sqlalchemy import Column, String, Integer, Boolean, create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json                                               
from sqlalchemy.sql.schema import PrimaryKeyConstraint         

database_name = "plants"
database_path ="postgres://{}:{}@{}/{}".format('student', 'student','localhost:5432', database_name)

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()



"""Plant class"""

#CREATION D'UNE CLASSE Plant MAPPE SUR LA TABLE plants_db:
class Plant(db.Model):
    __tablename__ = "plants_db"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    scientific_name = Column(String)
    is_poisonous = Column(Boolean)
    primary_color = Column(String)

#INSTENCIATION DE NOTRE CLASSE Plant
    def __init__(self, name, scientific_name, is_poisonous, primary_color):
        self.name = name
        self.scientific_name = scientific_name
        self.is_poisonous = is_poisonous
        self.primary_color = primary_color

#CREATION D'UNE METHODE POUR L'INSERTION DE DONNEES
    def insert(self):
        db.session.add(self)
        db.session.commit()

#CREATION D'UNE METHODE POUR LA MISE A JOUR DE DONNEES
    def update(self):
        db.session.commit()

#CREATION D'UNE METHODE POUR LA SUPPRESSION DE DONNEES
    def delete(self):
        db.session.delete(self)
        db.session.commit()

#FORMATAGE D'UN OBJET Plant SOUS FORME DE DICTIONNAIRE POUR FAIRE LA CORRESPONDANCE (ATTRIBUT-VALEUR)
    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "scientific_name": self.scientific_name,
            "is_poisonous": self.is_poisonous,
            "primary_color": self.primary_color,
        }
