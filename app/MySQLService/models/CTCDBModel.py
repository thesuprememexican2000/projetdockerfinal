from models.DBConnection import db


class CTCDBModel(db.Model):
    __tablename__ = 'CTC'
    
    id = db.Column(db.Integer, primary_key=True)
    min = db.Column(db.Integer)
    max = db.Column(db.Integer)
    rate = db.Column(db.Double)