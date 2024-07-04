import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from db import db
from utils import bcrypt
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
app.config.from_pyfile("config.py")
db.init_app(app)
bcrypt.init_app(app)

from modelos import Login, Livro, Feedback
from routes import *
from crud import *

login_manager = LoginManager()
login_manager.init_app(app)
csrf = CSRFProtect(app)
csrf.init_app(app)

print(app.config['SQLALCHEMY_DATABASE_URI'])

# flask login
login_manager.login_view = 'admin_login'

@login_manager.user_loader
def load_user(id):
    try:
        return Login.query.get_or_404(id)
    except HTTPException:
        return None

if __name__ == '__main__':
    app.run(debug=True)