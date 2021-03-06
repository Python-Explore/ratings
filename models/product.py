from db import db

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    rate = db.Column(db.Integer)
    name = db.Column(db.String(100))

    def __init__(self,id,rate,name):
        self.id = id
        self.rate = rate
        self.name = name

    def json(self):
        return {'name': self.name, 'rate': self.price}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()