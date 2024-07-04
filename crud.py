import functools
from flask import Flask, request, flash, redirect, url_for, render_template, session
from modelos import Login, Livro, Feedback
from funcoes import FormularioUsuario, LivroForm
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, current_user
from flask_wtf import CSRFProtect
from flask_bcrypt import check_password_hash
from admin_credentials import ADMIN_USERNAME, ADMIN_PASSWORD
from app import app
from db import db
from utils import bcrypt
        
def requires_admin_login(view_function):
    @functools.wraps(view_function)
    def decorated_function(*args, **kwargs):
        if 'usuario_id' not in session:
            return redirect(url_for('admin_login'))
        return view_function(*args, **kwargs)
    return decorated_function
        
def get_usuario_from_session():
    return session.get('usuario')
        
@app.context_processor
def inject_usuario():
    usuario = get_usuario_from_session()  # Get the usuario from the session
    return dict(usuario=usuario)
        
@app.route('/crud_login', methods=['GET', 'POST'])
def crud_login():    
    # Get the current user's id
    form = FormularioUsuario()
    clientes_ids = session.get('clientes')
    if clientes_ids is not None:
        clientes = Login.query.filter(Login.id.in_(clientes_ids)).all()
    else:
        clientes = []
        
    if request.method == 'POST':
        operation = request.form.get('operation')

        if operation == 'create':
            nome = request.form.get('nome')
            email = request.form.get('email')
            senha = request.form.get('senha')
            hashed_senha = bcrypt.generate_password_hash(senha).decode('utf-8')
            novo_usuario = Login(nome=nome, email=email, senha=hashed_senha)
            db.session.add(novo_usuario)
            db.session.commit()
            flash('Usuário criado com sucesso!')

        elif operation == 'read':
            usuarios = Login.query.all()
            flash('Usuário lido com sucesso!')
            return render_template('lista_usuarios.html', form=form, clientes=clientes, usuarios=usuarios)

        elif operation == 'update':
            id = request.form.get('id')
            novo_nome = request.form.get('nome')
            novo_email = request.form.get('email')
            nova_senha = request.form.get('senha')
            usuario = Login.query.get(id)
            usuario.nome = novo_nome
            usuario.email = novo_email
            if nova_senha:  
                hashed_nova_senha = bcrypt.generate_password_hash(nova_senha).decode('utf-8')
                usuario.senha = hashed_nova_senha
            db.session.commit()
            flash('Usuário atualizado com sucesso!')

        elif operation == 'delete':
            id = request.form.get('id')
            usuario = Login.query.get(id)
            db.session.delete(usuario)
            db.session.commit()
            flash('Usuário deletado com sucesso!')
    
    return render_template('crud_login.html', form=form, clientes=clientes)

@app.route('/crud_livros', methods=['GET', 'POST'])
def crud_livros():
    form = LivroForm()
    clientes_ids = session.get('clientes')
    if clientes_ids is not None:
        clientes = Login.query.filter(Login.id.in_(clientes_ids)).all()
    else:
        clientes = []
    operation = None
    
    if form.validate_on_submit():
        operation = request.form['operation']
        
        if operation == 'create':
            livro = Livro(
            cliente_id = form.cliente_id.data,
            ISBN = form.ISBN.data,
            titulo = form.titulo.data,
            autor = form.autor.data,
            editora = form.editora.data,
            ano_publicacao = form.ano_publicacao.data,
            categoria = form.categoria.data,
            quantidade = form.quantidade.data,
            preco = form.preco.data,
            imagem=form.imagem.data,
            palavrinha=form.palavrinha.data
            )
            db.session.add(livro)
            db.session.commit()
            flash('Livro criado com sucesso!')
            # Redirect back to the same page to clear the form fields
            return redirect(url_for('crud_livros'))
        else:
            flash('Erro: cliente_id não encontrado na sessão.')
            pass

    elif operation == 'read':
        livros = Livro.query.all()
        return render_template('crud_livros.html', form=form, livros=livros, clientes=clientes)
        
    elif operation == 'update':
        # Update a book
        livro = Livro.query.get(form.id.data)
        if livro:
            livro.cliente_id = form.cliente_id.data
            livro.ISBN = form.ISBN.data
            livro.titulo = form.titulo.data
            livro.autor = form.autor.data
            livro.editora = form.editora.data
            livro.ano_publicacao = form.ano_publicacao.data
            livro.categoria = form.categoria.data
            livro.quantidade = form.quantidade.data
            livro.preco = form.preco.data
            livro.imagem = form.imagem.data
            livro.palavrinha = form.palavrinha.data
            db.session.commit()
            flash('Livro atualizado com sucesso!')
            pass

    elif operation == 'delete':
        livro_id = request.form['id']
        livro = Livro.query.get(livro_id)
        if livro:
            db.session.delete(livro)  # Delete the book
            db.session.commit()
            flash('Livro deletado com sucesso!')
    else:
        flash('Erro: livro não encontrado.')

    return render_template('crud_livros.html', form=form, clientes=clientes)

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    form = FormularioUsuario()
    if form.validate_on_submit():
        proxima = request.form.get('next')
        app.logger.debug(f'Próxima rota: {proxima}')
        usuario = Login.query.filter_by(email=form.email.data).first()
        if usuario:
            if check_password_hash(usuario.senha, form.senha.data) and usuario.email == ADMIN_USERNAME:
                # Armazena o ID do usuário na sessão
                session['usuario_id'] = usuario.id
                session['clientes'] = [cliente.id for cliente in Login.query.all()]
                # Adiciona o nome do usuário na sessão
                session['usuario_nome'] = usuario.nome
                flash(f'{usuario.nome} logado com sucesso!')
                app.logger.debug(f'Usuário logado com sucesso: {usuario.nome}')
                return redirect(proxima) if proxima else redirect(url_for('crud_livros'))
            else:
                flash('Senha incorreta.')
                app.logger.debug('Senha incorreta.')
        else:
            flash('Usuário não encontrado.')
            app.logger.debug('Usuário não encontrado.')
    return render_template('admin_login.html', form=form, proxima=url_for('crud_livros'))

@app.route('/admin_logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    flash('Logout de administrador realizado com sucesso!')
    return redirect(url_for('login'))

    
@app.route('/delete_usuario/<int:id>', methods=['POST'])
def delete_usuario(id):
    # Deleta entradas em Feedback
    Feedback.query.filter_by(usuario_id=id).delete()

    # Deleta entradas em Livros
    Livro.query.filter_by(usuario_id=id).delete()

    # Depois, delete o usuário
    Login.query.filter_by(id=id).delete()
    db.session.commit()

    return redirect(url_for('crud_login'))

@app.route('/livro', methods=['GET', 'POST'])
def livro():
    form = LivroForm()
    clientes = Login.query.all()
    return render_template('livro.html', form=form, clientes=clientes)