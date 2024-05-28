import pandas as pd

from create_app import db
from models.property import Property


def import_properties_from_csv(file_path):
    """
    Import properties from a CSV file into the database.

    :param file_path: Path to the CSV file
    :return: List of imported properties
    """
    data = pd.read_csv(file_path)
    properties = []

    for _, row in data.iterrows():
        property = Property(address=row['address'], rent=row['rent'])
        db.session.add(property)
        properties.append(property)

    db.session.commit()
    return properties
