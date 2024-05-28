from create_app import db
from models.property import Property
from models.tenant import Tenant


def add_tenant(name, email, property_id=None):
    if Tenant.query.filter_by(email=email).first():
        return None, "Tenant with this email already exists"
    new_tenant = Tenant(name=name, email=email, property_id=property_id)
    db.session.add(new_tenant)
    db.session.commit()
    return new_tenant, None

def get_tenants():
    tenants = Tenant.query.all()
    return [tenant.to_dict() for tenant in tenants]

def assign_tenant_to_property(tenant_id, property_id):
    tenant = Tenant.query.get(tenant_id)
    if not tenant:
        return None, "Tenant not found"
    property = Property.query.get(property_id)
    if not property:
        return None, "Property not found"
    tenant.property_id = property_id
    db.session.commit()
    return tenant, None
