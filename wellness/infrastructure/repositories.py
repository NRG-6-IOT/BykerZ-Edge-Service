from wellness.domain.entities import VehicleMetricRecord
from wellness.infrastructure.models import VehicleMetricRecord as VehicleMetricRecordModel

class VehicleMetricRepository:
    @staticmethod
    def save(vehicle_metric_record) -> VehicleMetricRecord:
        """Save a vehicle metric record to the database.

        Args:
            vehicle_metric_record (VehicleMetricRecord): The vehicle metric record to save.

        Returns:
            VehicleMetricRecord: The saved vehicle metric record including its ID.
        """

        record = VehicleMetricRecordModel.create(
            device_id=vehicle_metric_record.device_id,
            vehicle_id=vehicle_metric_record.vehicle_id,
            latitude=vehicle_metric_record.latitude,
            longitude=vehicle_metric_record.longitude,
            CO2Ppm=vehicle_metric_record.CO2Ppm,
            NH3Ppm=vehicle_metric_record.NH3Ppm,
            BenzenePpm=vehicle_metric_record.BenzenePpm,
            temperatureCelsius=vehicle_metric_record.temperatureCelsius,
            humidityPercentage=vehicle_metric_record.humidityPercentage,
            pressureHpa=vehicle_metric_record.pressureHpa,
            impactDetected=vehicle_metric_record.impactDetected
        )

        return VehicleMetricRecord(
            device_id=vehicle_metric_record.device_id,
            vehicle_id=vehicle_metric_record.vehicle_id,
            latitude=vehicle_metric_record.latitude,
            longitude=vehicle_metric_record.longitude,
            CO2Ppm=vehicle_metric_record.CO2Ppm,
            NH3Ppm=vehicle_metric_record.NH3Ppm,
            BenzenePpm=vehicle_metric_record.BenzenePpm,
            temperatureCelsius=vehicle_metric_record.temperatureCelsius,
            humidityPercentage=vehicle_metric_record.humidityPercentage,
            pressureHpa=vehicle_metric_record.pressureHpa,
            impactDetected=vehicle_metric_record.impactDetected,
            id=record.id
        )