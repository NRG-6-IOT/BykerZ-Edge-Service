from flask import Flask

from iam.application.services import AuthApplicationService
from iam.interfaces.services import iam_api
from shared.infrastructure.database import init_db
from wellness.interfaces.services import wellness_api

app = Flask(__name__)

app.register_blueprint(iam_api)
app.register_blueprint(wellness_api)

first_request = True

@app.before_request
def setup():

    global first_request
    if first_request:
        first_request = False
        init_db()
        auth_application_service = AuthApplicationService()
        auth_application_service.get_or_create_test_device()

@app.route('/')
def about_edge_service():
    return "Bykerz IoT Edge Service - Bykerz Application"

if __name__ == '__main__':
    app.run(debug=True)