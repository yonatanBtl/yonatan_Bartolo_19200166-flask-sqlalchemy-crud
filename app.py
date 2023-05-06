from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION_URI

#conexion con la base de datos

app = Flask(__name__)

# settings
app.secret_key = 'mysecret'
print(DATABASE_CONNECTION_URI)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# no cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

SQLAlchemy(app)

app.register_blueprint(contacts)
#permite el registro del blueprint contacts en la aplicación app de Flask.
