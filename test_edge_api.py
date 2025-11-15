import requests
import time
import random
from iam.application.services import AuthApplicationService

# Configuración
DEVICE_ID = "bykerz-iot-001"
EDGE_API_URL = "http://localhost:5000/api/v1/metrics"


def get_jwt_token():
    """Obtiene el JWT token usando el servicio IAM del proyecto"""
    auth_service = AuthApplicationService()
    device = auth_service.get_device_by_id(DEVICE_ID)

    if not device:
        print(f"✗ Error: Dispositivo {DEVICE_ID} no encontrado")
        print("  Asegúrate de que el dispositivo exista en la base de datos")
        return None

    return device.jwt_token


def generate_mock_data():
    """Genera datos simulados de sensores"""
    return {
        "device_id": DEVICE_ID,
        "vehicle_id": 1,
        "latitude": -12.046374 + random.uniform(-0.001, 0.001),
        "longitude": -77.042793 + random.uniform(-0.001, 0.001),
        "CO2Ppm": round(random.uniform(400, 500), 2),
        "NH3Ppm": round(random.uniform(20, 35), 2),
        "BenzenePpm": round(random.uniform(3, 10), 2),
        "temperatureCelsius": round(random.uniform(20, 30), 2),
        "humidityPercentage": round(random.uniform(60, 80), 2),
        "pressureHpa": round(random.uniform(1010, 1020), 2),
        "impactDetected": random.choice([True, False])
    }


def send_metric(jwt_token):
    """Envía una métrica al Edge Service"""
    data = generate_mock_data()
    headers = {
        "Authorization": f"Bearer {jwt_token}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(EDGE_API_URL, json=data, headers=headers, timeout=5)
        print(f"✓ Enviado - Status: {response.status_code}")
        print(f"  Datos: CO2={data['CO2Ppm']:.1f}ppm, Temp={data['temperatureCelsius']:.1f}°C, "
              f"Impact={data['impactDetected']}")
        print(f"  Response: {response.json()}\n")
    except requests.Timeout:
        print(f"✗ Error: Timeout al conectar con {EDGE_API_URL}\n")
    except requests.RequestException as e:
        print(f"✗ Error de conexión: {e}\n")
    except Exception as e:
        print(f"✗ Error inesperado: {e}\n")


if __name__ == "__main__":
    print("=== Simulador de métricas IoT ===")
    print(f"Dispositivo: {DEVICE_ID}")
    print(f"Edge API: {EDGE_API_URL}\n")

    # Obtener token JWT del dispositivo
    print("Obteniendo token JWT...")
    jwt_token = get_jwt_token()

    if not jwt_token:
        print("\n✗ No se pudo obtener el token. Verifica que el Edge Service esté ejecutándose.")
        exit(1)

    print(f"✓ Token obtenido: {jwt_token[:20]}...\n")
    print("Iniciando envío de métricas (Ctrl+C para detener)\n")

    try:
        while True:
            send_metric(jwt_token)
            time.sleep(5)  # Envía cada 5 segundos
    except KeyboardInterrupt:
        print("\n\n✓ Simulador detenido")
