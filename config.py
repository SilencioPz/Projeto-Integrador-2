import os
from app import app

SECRET_KEY = 'projeto-integrador-2'

SQLALCHEMY_DATABASE_URI = \
    '{SGDB}://{usuario}:{senha}@{servidor}:{porta}/{database}'.format(
        SGDB = 'mysql+pymysql',
        usuario = 'bruno',
        senha = '1234',
        servidor = 'localhost',
        porta ='3306',
        database = 'db_quie_isso'
    )
    
app.config['FOTOGRAFIAS_PATH'] = os.path.join('static', 'fotografias')

GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')