from create_app import db
from models.property import Property
from services.aws_s3_service import upload_file_to_s3


def add_property(data):
    new_property = Property(
        address=data['address'],
        city=data['city'],
        state_province=data['state_province'],
        country=data['country'],
        postal_code=data['postal_code'],
        rent=data['rent'],
        deposit=data['deposit'],
        bathrooms=data['bathrooms'],
        size=data['size'],
        furnished=data['furnished'],
        term=data['term'],
        availability=data['availability'],
        utilities_included=data['utilities_included'],
        property_features=','.join(data['property_features']),
        building_features=','.join(data['building_features']),
        community_features=','.join(data['community_features']),
        picture_urls=''
    )
    db.session.add(new_property)
    db.session.commit()
    return new_property

def upload_property_pictures(property_id, pictures):
    property = Property.query.get(property_id)
    if not property:
        return None, "Property not found"

    picture_urls = property.picture_urls.split(',') if property.picture_urls else []
    for picture in pictures:
        picture_url = upload_file_to_s3(picture, os.getenv('S3_BUCKET'))
        if picture_url:
            picture_urls.append(picture_url)

    property.picture_urls = ','.join(picture_urls)
    db.session.commit()
    return property, None

def get_properties():
    properties = Property.query.all()
    return [property.to_dict() for property in properties]
