class VehicleMetricRecord:
    """Entity representing a vehicle metric record.

    Attributes:
        id (int): Unique identifier for the vehicle metric record.
        device_id (str): Identifier for the device that recorded the vehicle metrics.
        vehicle_id (int): Identifier for the vehicle.
        latitude (float): Latitude of the vehicle's location.
        longitude (float): Longitude of the vehicle's location.
        CO2Ppm (float): CO2 concentration in parts per million.
        NH3Ppm (float): NH3 concentration in parts per million.
        BenzenePpm (float): Benzene concentration in parts per million.
        temperatureCelsius (float): Temperature in Celsius.
        humidityPercentage (float): Humidity percentage.
        pressureHpa (float): Atmospheric pressure in hPa.
        impactDetected (bool): Flag indicating if an impact was detected.
    """
    def __init__(self, device_id: str, vehicle_id: int, latitude: float,
                 longitude: float, CO2Ppm: float, NH3Ppm: float, BenzenePpm: float, temperatureCelsius: float,
                 humidityPercentage: float, pressureHpa: float, impactDetected: bool, id: int = None):
        """Initialize a VehicleMetricRecord instance.

        Args:
            device_id (str): Identifier for the device that recorded the vehicle metrics.
            vehicle_id (int): Identifier for the vehicle.
            latitude (float): Latitude of the vehicle's location.
            longitude (float): Longitude of the vehicle's location.
            CO2Ppm (float): CO2 concentration in parts per million.
            NH3Ppm (float): NH3 concentration in parts per million.
            BenzenePpm (float): Benzene concentration in parts per million.
            temperatureCelsius (float): Temperature in Celsius.
            humidityPercentage (float): Humidity percentage.
            pressureHpa (float): Atmospheric pressure in hPa.
            impactDetected (bool): Flag indicating if an impact was detected.
            id (int, optional): Unique identifier for the vehicle metric record. Defaults to None.
        """
        self.id = id
        self.device_id = device_id
        self.vehicle_id = vehicle_id
        self.latitude = latitude
        self.longitude = longitude
        self.CO2Ppm = CO2Ppm
        self.NH3Ppm = NH3Ppm
        self.BenzenePpm = BenzenePpm
        self.temperatureCelsius = temperatureCelsius
        self.humidityPercentage = humidityPercentage
        self.pressureHpa = pressureHpa
        self.impactDetected = impactDetected
