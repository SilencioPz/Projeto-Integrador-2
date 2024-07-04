import os
from flask import request, render_template
from app import app
from db import db
from utils import bcrypt
from wtforms import SubmitField, IntegerField
from flask_wtf import FlaskForm 
from wtforms import SelectField, StringField, IntegerField, SubmitField, PasswordField, DecimalField, validators, DateField
from wtforms.validators import DataRequired, Length, Email, Regexp
from modelos import Login

class FormularioUsuario(FlaskForm):
    email = StringField('Email:', [
        validators.DataRequired(),
        Email(message='E-mail inválido'),
        Regexp(r'^[^@]+@gmail\.com|[^@]+@outlook\.com|[^@]+@yahoo\.com$', message='Domínio de e-mail inválido')
    ])
    senha = PasswordField('Senha:', [
        validators.DataRequired(),
        Length(min=8, max=60, message='Senha deve ter entre 8 e 60 caracteres')
    ])
    logar = SubmitField('Logar')
    
class FormularioCriarUsuario(FlaskForm):
    nome = StringField('Nome:', [
        validators.DataRequired(),
        Length(min=2, max=100, message='Nome deve ter entre 2 e 100 caracteres')
    ])
    email = StringField('E-mail:', [
        validators.DataRequired(),
        Email(message='E-mail inválido'),
        Regexp(r'^[^@]+@gmail\.com|[^@]+@outlook\.com|[^@]+@yahoo\.com$', message='Inválido domínio de e-mail')
    ])
    senha = PasswordField('Senha:', [
        validators.DataRequired(),
        Length(min=8, max=60, message='Senha deve ter entre 8 e 60 caracteres')
    ])
    submit = SubmitField('Salvar')

def get_cliente_choices():
    return [(c.id, c.nome) for c in Login.query.all()]

class LivroForm(FlaskForm):
    id = IntegerField('ID do Livro')
    cliente_id = SelectField('Cliente ID', validators=[DataRequired()], coerce=int, choices=get_cliente_choices)
    ISBN = StringField('ISBN', validators=[DataRequired()])
    titulo = StringField('Título', validators=[DataRequired()])
    autor = StringField('Autor', validators=[DataRequired()])
    editora = StringField('Editora', validators=[DataRequired()])
    ano_publicacao = DateField('Ano de Publicação', format='%Y-%m-%d', validators=[DataRequired()])
    categoria = StringField('Categoria', validators=[DataRequired()])
    quantidade = IntegerField('Quantidade', validators=[DataRequired()])
    preco = DecimalField('Preço', validators=[DataRequired()])
    imagem = StringField('Imagem', validators=[DataRequired()])
    palavrinha = StringField('Palavrinha', validators=[DataRequired()])
    operation = SelectField('Operação', validators=[DataRequired()], choices=[
        ('create', 'Criar'),
        ('read', 'Ler'),
        ('update', 'Atualizar'),
        ('delete', 'Deletar')
    ])
    submit = SubmitField('Salvar')
    
def recuperaImagem(id):
    for filename in os.listdir(app.config['FOTOGRAFIAS']):
        if f'foto{id}' in filename:
            return filename
    return 'livro.png'

def deletaArquivo(id):
    arquivo = recuperaImagem(id)
    if arquivo != 'livro.png':
        os.remove(os.path.join(app.config['FOTOGRAFIAS'], arquivo))