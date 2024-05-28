from create_app import db


class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state_province = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    postal_code = db.Column(db.String(20), nullable=False)
    rent = db.Column(db.Float, nullable=False)
    deposit = db.Column(db.Float, nullable=False)
    bathrooms = db.Column(db.Float, nullable=False)
    size = db.Column(db.Integer, nullable=False)
    furnished = db.Column(db.Boolean, nullable=False)
    term = db.Column(db.String(50), nullable=False)
    availability = db.Column(db.String(50), nullable=False)
    utilities_included = db.Column(db.String(120), nullable=False)
    property_features = db.Column(db.String(500), nullable=True)
    building_features = db.Column(db.String(500), nullable=True)
    community_features = db.Column(db.String(500), nullable=True)
    tenants = db.relationship('Tenant', backref='property', lazy=True)

    def __init__(self, address, city, state_province, country, postal_code, rent, deposit, bathrooms, size, furnished, term, availability, utilities_included, property_features, building_features, community_features):
        self.address = address
        self.city = city
        self.state_province = state_province
        self.country = country
        self.postal_code = postal_code
        self.rent = rent
        self.deposit = deposit
        self.bathrooms = bathrooms
        self.size = size
        self.furnished = furnished
        self.term = term
        self.availability = availability
        self.utilities_included = utilities_included
        self.property_features = property_features
        self.building_features = building_features
        self.community_features = community_features

    def to_dict(self):
        return {
            'id': self.id,
            'address': self.address,
            'city': self.city,
            'state_province': self.state_province,
            'country': self.country,
            'postal_code': self.postal_code,
            'rent': self.rent,
            'deposit': self.deposit,
            'bathrooms': self.bathrooms,
            'size': self.size,
            'furnished': self.furnished,
            'term': self.term,
            'availability': self.availability,
            'utilities_included': self.utilities_included,
            'property_features': self.property_features.split(','),
            'building_features': self.building_features.split(','),
            'community_features': self.community_features.split(','),
            'tenants': [tenant.to_dict() for tenant in self.tenants]
        }
