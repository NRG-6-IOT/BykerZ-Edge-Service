from iam.application.services import AuthApplicationService
from wellness.domain.services import VehicleMetricRecordService
from wellness.infrastructure.repositories import VehicleMetricRepository
from wellness.domain.entities import VehicleMetricRecord

class VehicleMetricRecordApplicationService:
    def __init__(self):
        self.vehicle_metric_repository = VehicleMetricRepository()
        self.vehicle_metric_service = VehicleMetricRecordService()
        self.iam_service = AuthApplicationService()

    # def create_vehicle_metric_record(self, device_id: str, vehicle_id: int, latitude: float, longitude: float,
    #                                  CO2Ppm: float, NH3Ppm: float, BenzenePpm: float, temperatureCelsius: float,
    #                                  humidityPercentage: float, pressureHpa: float, impactDetected: bool,
    #                                  api_key: str) -> VehicleMetricRecord:
    def create_vehicle_metric_record(self, device_id: str, vehicle_id: int, latitude: float, longitude: float,
                                     CO2Ppm: float, NH3Ppm: float, BenzenePpm: float, temperatureCelsius: float,
                                     pressureHpa: float, impactDetected: bool) -> VehicleMetricRecord:
        """
        Create a vehicle metric record submitted by a device.

        Args:
            device_id (str): Unique identifier of the device sending the metric.
            vehicle_id (int): Identifier of the vehicle associated with the device.
            latitude (float): GPS latitude in decimal degrees.
            longitude (float): GPS longitude in decimal degrees.
            CO2Ppm (float): CO2 concentration in parts per million (ppm).
            NH3Ppm (float): Ammonia (NH3) concentration in ppm.
            BenzenePpm (float): Benzene concentration in ppm.
            temperatureCelsius (float): Temperature in degrees Celsius.
            pressureHpa (float): Atmospheric pressure in hectopascals (hPa).
            impactDetected (bool): Whether an impact was detected (True/False).
            api_key (str): API key used to authenticate the device.

        Returns:
            VehicleMetricRecord: The created record instance persisted in the repository.

        Raises:
            ValueError: If the device does not exist or the api_key is invalid.
        """

        # if not self.iam_service.get_device_by_id_and_api_key(device_id, api_key):
        #    raise ValueError("Device not found or invalid API key")
        record = self.vehicle_metric_service.create_record(
            device_id, vehicle_id, latitude, longitude,
            CO2Ppm, NH3Ppm, BenzenePpm, temperatureCelsius,
            pressureHpa, impactDetected
        )
        return self.vehicle_metric_repository.save(record)