from app import db
from werkzeug.security import generate_password_hash, check_password_hash

from sqlalchemy import Column, Integer, String
#from sqlalchemy.ext.declarative import declarative_base

class User(db.Model):   
    # tablename nao estava funcionando e, para seguir em frente, 
    # eu comentei o codigo. por isso, o SQLAlchemy vai pegar o nome da classe
    # para ser o nome do objeto.
    
    #__tablename__ == "users" 
    #__name__ == "users"

    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(20), nullable=False, unique=True, index=True)
    password = Column(String(128), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def compare_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"<user: {self.username}"

class Contact(db.Model):
    #__tablename__ = "contacts"
    #__name__ == "contacts"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(35), nullable=False)
    cellphone = Column(String(15), nullable=False, unique=True)

    def __init__(self, name, cellphone):
        self.name = name
        self.cellphone = cellphone

    def __repr__(self):
        return f"<contact: {self.name}"