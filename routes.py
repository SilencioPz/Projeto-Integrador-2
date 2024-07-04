import os
from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory, send_file, jsonify, abort, current_app
from modelos import *
from funcoes import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from werkzeug.security import generate_password_hash
from datetime import datetime, date
from flask_login import login_user, login_required, current_user
from relatorio import generate_pdf
from app import app
from db import db
from utils import bcrypt
from config import GOOGLE_MAPS_API_KEY

def some_function():
    # Use bcrypt here
    bcrypt.generate_password_hash('password')

def test_connection():
    connection = None
    try:
        engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
        connection = engine.connect()
    except Exception as e:
        print("Erro ao conectar com o banco de dados: ", e)
        return False
    else:
        print("Conectado com sucesso!")
        return True
    finally:
        if connection:  # Verifique se connection não é None antes de fechar
            connection.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = FormularioCriarUsuario()
    if form.validate_on_submit():
        # Process the form data here
        nome = form.nome.data
        email = form.email.data
        senha = form.senha.data

        # Cria o hash da senha
        hashed_senha = bcrypt.generate_password_hash(senha).decode('utf-8')
        
        carinha = Login(nome=nome, email=email, senha=hashed_senha)
        db.session.add(carinha)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('criar.html', titulo='Novo Usuário Quié Isso Livros:', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = FormularioUsuario()
    if form.validate_on_submit():
        return redirect(url_for('autenticar'))
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima, form=form)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    form = FormularioUsuario(request.form)
    usuario = Login.query.filter_by(email=form.email.data).first()
    if usuario and bcrypt.check_password_hash(usuario.senha, form.senha.data):
        # Log in the user
        login_user(usuario)
        flash(f'{usuario.nome} logado com sucesso!')
        proxima = request.form.get('proxima')
        if proxima:
            return redirect(proxima)
        return redirect(url_for('principal'))
    else:
        flash('E-mail ou senha inválidos.')
        return redirect(url_for('login'))

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session['usuarioLogado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('login'))

@app.route('/criar', methods=['GET', 'POST'])
def criar():
    form = FormularioCriarUsuario()
    if form.validate_on_submit():
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        # Cria o hash da senha
        hashed_senha = bcrypt.generate_password_hash(senha).decode('utf-8')
        
        carinha = Login(nome=nome, email=email, senha=hashed_senha)
        db.session.add(carinha)
        db.session.commit()
        return redirect(url_for('login'))
    else:
        return render_template('criar.html', form=form)

def obter_caminho_imagem(livro_id):
    if livro_id == 1:
        return 'fotografias/livro1.jpg'
    elif livro_id == 2:
        return 'fotografias/livro2.jpg'

@app.route('/principal', methods=['GET', 'POST'])
def principal():
    if not current_user.is_authenticated:
        return redirect(url_for('login', proxima=url_for('principal')))
    else:
        # Recupere o nome do usuário da sessão
        usuario_nome = current_user.nome
        form = LivroForm()
        if form.validate_on_submit():
            flash('Imagem enviada com sucesso!')
            return redirect(url_for('lista_livros'))
        api_key = current_app.config['GOOGLE_MAPS_API_KEY']
        return render_template('principal.html', titulo='Quié Isso Livros', form=form, usuario_nome=usuario_nome, api_key=api_key)

@app.route('/fotografias/<filename>')
def imagem(filename):
    try:
        image_path = os.path.join(app.config['FOTOGRAFIAS_PATH'], filename)
        return send_file(image_path, mimetype='image/png')
    except FileNotFoundError:
        flash('Imagem não encontrada.', 'danger')
        return redirect(url_for('lista_livros'))
    
@app.route('/carrossel/<carousel_name>')
def carrossel(carousel_name):
    if carousel_name == 'programacao':
        livros = Livro.query.filter_by(category='programacao').all()
    elif carousel_name == 'aventura':
        livros = Livro.query.filter_by(category='aventura').all()
    elif carousel_name == 'romance':
        livros = Livro.query.filter_by(category='romance').all()
    elif carousel_name == 'comedia':
        livros = Livro.query.filter_by(category='comedia').all()
    elif carousel_name == 'ficcao':
        livros = Livro.query.filter_by(category='ficcao').all()
    elif carousel_name == 'literatura_estrangeira':
        livros = Livro.query.filter_by(category='literatura_estrangeira').all()
    elif carousel_name == 'poesia':
        livros = Livro.query.filter_by(category='poesia').all()
    else:
        abort(404)  # Return 404 error if carousel_name is not recognized

    return render_template('carrossel.html', livros=livros, carousel_name=carousel_name)

#Rota para alterar as cores das seções
@app.template_filter('bg_class')
def bg_class(carousel_name):
    bg_classes = {
        'programacao': 'bg-info',
        'aventura': 'bg-success',
        'romance': 'bg-warning',
        'comedia': 'bg-danger',
        'ficcao': 'bg-primary',
        'literatura_estrangeira': 'bg-secondary',
        'poesia': 'bg-dark'
    }
    return bg_classes.get(carousel_name, 'bg-light')

#Rota da barra de pesquisa, para facilidades
@app.route('/pesquisar', methods=['GET', 'POST'])
def pesquisar():
    if request.method == 'POST':
        termo_pesquisa = request.form.get('termo_pesquisa')
    else:
        termo_pesquisa = request.args.get('pesquisa')
    resultados = Livro.query.filter(Livro.palavrinha.contains(termo_pesquisa)).all()
    if not resultados:
        return render_template('resultados.html', resultados="pesquisa não encontrada")
    else:
        return render_template('resultados.html', resultados=resultados)

#Rota dos comentários dos usuários
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if not current_user.is_authenticated:
        return redirect(url_for('login', proxima=url_for('feedback')))

    if request.method == 'POST':
        feedback = request.form['feedback']
        novo_feedback = Feedback(cliente_id=current_user.id, opiniao=feedback)
        db.session.add(novo_feedback)
        db.session.commit()
        flash('Obrigado pelo seu feedback!')
        return redirect(url_for('principal'))
    return render_template('feedback.html')

#Rota para as categorias de livros do site
@app.route('/livros/<categoria>')
def livros_categoria(categoria):
    # Limite de 7 livros por categoria 
    livros = Livro.query.filter_by(categoria=categoria).limit(7).all()
    return render_template('seu_template.html', livros=livros, categoria=categoria)

@app.route('/formulario')
def escolhe_livros():
    form = LivroForm()
    listaLivros = Livro.query.all()
    livros = []
    for livro in listaLivros:
        livro.imagemCaminho = url_for('imagem', filename=livro.imagem) if livro.imagem else url_for('static', filename='default.png')
        livros.append((str(livro.id), livro.titulo))
    form.candidato_id.choices = livros
    return render_template('escolhe_livros.html', titulo='Lista de Livros', livros=listaLivros, form=form)

@app.route('/lista_livros', defaults={'id': None})
@app.route('/lista_livros/<int:id>')
def lista_livros(id):
    form = LivroForm()
    if id:
        livro = Livro.query.get(id)
        if livro:
            livros = [livro]  
        else:
            livros = []  
    else:
        livros = Livro.query.all()  
    return render_template('lista_livros.html', form=form, livros=livros)
    
import os

@app.route('/relatorio', methods=['GET'])
def relatorio():
    livros = Livro.query.all()  # Obtenha todos os livros do banco de dados
    filepath = generate_pdf(livros)
    return send_file(open(filepath, 'rb'), 
                    mimetype='application/pdf', 
                    as_attachment=True, 
                    download_name='relatorio.pdf')