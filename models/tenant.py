from create_app import db


class Tenant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'), nullable=True)

    def __init__(self, name, email, property_id=None):
        self.name = name
        self.email = email
        self.property_id = property_id

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'property_id': self.property_id
        }
