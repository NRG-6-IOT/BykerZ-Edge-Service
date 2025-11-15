"""
Database initialization and connection management for the Smart Band application.
"""
from peewee import SqliteDatabase

# Initialize the SQLite database
db = SqliteDatabase('bykerz_iot.db')

def init_db()->None:
    """
    Initialize the database and create tables if they do not exist.

    """
    from iam.infrastructure.models import Device
    from wellness.infrastructure.models import VehicleMetricRecord

    db.connect()
    db.create_tables([Device, VehicleMetricRecord], safe=True)
    db.close()

