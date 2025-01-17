from flask import Flask

from adapters.drivers.http.controllers.auth_controller import auth_bp
from src.adapters.drivens.infra.settings.env import ENV
from src.adapters.drivens.infra.database.config import db
from src.core.domain.application.services.auth_service import AuthService

app = Flask(__name__)
env = ENV()
app.config['SQLALCHEMY_DATABASE_URI'] = env.CONNECT_STRING
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

auth_service = AuthService()

app.register_blueprint(auth_bp(auth_service))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print("Database initialized successfully!")
    app.run(host='0.0.0.0',debug=True,port=env.PORT)
