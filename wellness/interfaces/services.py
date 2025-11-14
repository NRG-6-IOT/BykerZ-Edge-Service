from flask import Blueprint, request, jsonify

from iam.interfaces.services import authenticate_request
from wellness.application.services import VehicleMetricRecordApplicationService

wellness_api = Blueprint('wellness_api', __name__)

vehicle_metric_service = VehicleMetricRecordApplicationService()

@wellness_api.route('/api/v1/metrics', methods=["POST"])
def create_vehicle_metric_record():
    """
    Endpoint to create a new vehicle metric record.
    Expects a JSON payload with device_id, vehicle_id, latitude, longitude,
    CO2Ppm, NH3Ppm, BenzenePpm, temperatureCelsius, humidityPercentage,
    pressureHpa, impactDetected.
    Requires an X-API-Key header with the API key.

    :return: A JSON response with the created vehicle metric record with its ID.
    201 if the record is created successfully, else 400 if the request is invalid or authentication fails.
    """

    auth_result = authenticate_request()
    if auth_result:
        return auth_result
    data = request.json
    try:
        device_id = data["device_id"]
        vehicle_id = data["vehicle_id"]
        latitude = data["latitude"]
        longitude = data["longitude"]
        CO2Ppm = data["CO2Ppm"]
        NH3Ppm = data["NH3Ppm"]
        BenzenePpm = data["BenzenePpm"]
        temperatureCelsius = data["temperatureCelsius"]
        humidityPercentage = data["humidityPercentage"]
        pressureHpa = data["pressureHpa"]
        impactDetected = data["impactDetected"]

        record = vehicle_metric_service.create_vehicle_metric_record(
            device_id, vehicle_id, latitude, longitude, CO2Ppm, NH3Ppm,
            BenzenePpm, temperatureCelsius, humidityPercentage, pressureHpa,
            impactDetected, request.headers.get("X-API-Key")
        )

        return jsonify({
            "id": record.id,
            "device_id": record.device_id,
            "vehicle_id": record.vehicle_id,
            "latitude": record.latitude,
            "longitude": record.longitude,
            "CO2Ppm": record.CO2Ppm,
            "NH3Ppm": record.NH3Ppm,
            "BenzenePpm": record.BenzenePpm,
            "temperatureCelsius": record.temperatureCelsius,
            "humidityPercentage": record.humidityPercentage,
            "pressureHpa": record.pressureHpa,
            "impactDetected": record.impactDetected
        }), 201
    except KeyError as e:
        return jsonify({"error": f"Missing field: {str(e)}"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400