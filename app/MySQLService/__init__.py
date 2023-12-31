from flask import Flask
from models.DBConnection import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABAST_URI'] = 'mysql://mysql-wokemoralistgaming25.alwaysdata.net:3306/wokemoralistgaming25_projetdockerfinal'