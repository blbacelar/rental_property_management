from create_app import create_app, db
from models.property import Property
from models.tenant import Tenant

app = create_app()

with app.app_context():
    db.create_all()
    print("Database initialized!")
