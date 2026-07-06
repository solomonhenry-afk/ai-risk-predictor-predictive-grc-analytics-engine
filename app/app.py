from flask import Flask

from app.routes.dashboard import dashboard_bp


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "lighthouse-ai-risk-predictor-development-key"

    app.register_blueprint(dashboard_bp)

    return app
