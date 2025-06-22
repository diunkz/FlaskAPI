from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

print(app.config['SECRET_KEY'])
print(['SQLALCHEMY_DATABASE_URI'])
print(['SWAGGER'])
print(['CACHE_TYPE'])

class User(db.model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullale=False)
    password = db.Column(db.String(120), nullable=False)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    time_minutes = db.Column(db.Integer, nullable=False) 

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Banco de Dados criado!")
