from peewee import Model, AutoField, CharField, FloatField, BooleanField

from shared.infrastructure.database import db


class VehicleMetricRecord(Model):
    id =AutoField()
    device_id = CharField()
    vehicle_id = FloatField()
    latitude = FloatField()
    longitude = FloatField()
    CO2Ppm = FloatField()
    NH3Ppm = FloatField()
    BenzenePpm = FloatField()
    temperatureCelsius = FloatField()
    humidityPercentage = FloatField()
    pressureHpa = FloatField()
    impactDetected = BooleanField()

    class Meta:
        database = db
        table_name = 'vehicle_metric_records'