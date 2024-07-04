from flask_login import LoginManager, UserMixin
from app import app
from sqlalchemy.orm import mapped_column
from sqlalchemy import Column, String,Integer, Text, DECIMAL, Date, ForeignKey
from db import db

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class Login(db.Model, UserMixin):
    __tablename__ = 'cliente'
    id = mapped_column(Integer, autoincrement=True, primary_key=True)
    nome = mapped_column(String(100), nullable=False)
    email = mapped_column(String(100), nullable=False)
    senha = mapped_column(String(255), nullable=False)
    livros = db.relationship('Livro', backref='cliente', lazy=True)
    feedbacks = db.relationship('Feedback', backref='cliente', lazy=True)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

class Livro(db.Model):
    __tablename__ = 'livros'
    id = Column(Integer, autoincrement=True, primary_key=True)
    cliente_id = Column(Integer, ForeignKey('cliente.id'), nullable=False)
    ISBN = mapped_column(Text, nullable=False) 
    titulo = mapped_column(Text, nullable=False) 
    autor = mapped_column(Text, nullable=False)
    editora = mapped_column(Text, nullable=False)
    ano_publicacao = mapped_column(Date, nullable=False)
    categoria = mapped_column(Text, nullable=False) 
    quantidade = mapped_column(Integer, nullable=False)
    preco = mapped_column(DECIMAL(10,2), nullable=False) 
    imagem = mapped_column(Text, nullable=False) 
    palavrinha = mapped_column(Text, nullable=False)

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = Column(Integer, autoincrement=True, primary_key=True)
    cliente_id = Column(Integer, ForeignKey('cliente.id'), nullable=False)
    opiniao = mapped_column(Text, nullable=False)