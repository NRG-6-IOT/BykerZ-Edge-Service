from wellness.domain.entities import VehicleMetricRecord


class VehicleMetricRecordService:
    def __init__(self):
        """Initialize the vehicle metric record service."""
        pass

    @staticmethod
    def create_record(device_id: str, vehicle_id: int, latitude: float, longitude: float,
                      CO2Ppm: float, NH3Ppm: float, BenzenePpm: float, temperatureCelsius: float,
                      humidityPercentage: float, pressureHpa: float, impactDetected: bool) -> VehicleMetricRecord:
        """Create a vehicle metric record.

        Args:
            device_id (str): The ID of the device.
            vehicle_id (int): The ID of the vehicle.
            latitude (float): The latitude of the vehicle's location.
            longitude (float): The longitude of the vehicle's location.
            CO2Ppm (float): CO2 concentration in parts per million.
            NH3Ppm (float): NH3 concentration in parts per million.
            BenzenePpm (float): Benzene concentration in parts per million.
            temperatureCelsius (float): Temperature in Celsius.
            humidityPercentage (float): Humidity percentage.
            pressureHpa (float): Atmospheric pressure in hPa.
            impactDetected (bool): Whether an impact was detected.

        Returns:
            VehicleMetricRecord: The created vehicle metric record.

        Raises:
            ValueError: If any of the input values are invalid.
        """
        try:
            vehicle_id = int(vehicle_id)
            latitude = float(latitude)
            longitude = float(longitude)
            CO2Ppm = float(CO2Ppm)
            NH3Ppm = float(NH3Ppm)
            BenzenePpm = float(BenzenePpm)
            temperatureCelsius = float(temperatureCelsius)
            humidityPercentage = float(humidityPercentage)
            pressureHpa = float(pressureHpa)
            impactDetected = bool(impactDetected)
        except (ValueError, TypeError):
            raise ValueError("Invalid data format")

        return VehicleMetricRecord(device_id, vehicle_id, latitude,
                                   longitude, CO2Ppm, NH3Ppm, BenzenePpm, temperatureCelsius,
                                   humidityPercentage, pressureHpa, impactDetected)