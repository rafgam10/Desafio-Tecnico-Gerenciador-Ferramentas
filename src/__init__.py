from flask import Flask
from .settings.config import Config
from .settings.extensions import db, migrate, jwt, swagger


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    swagger.init_app(app)

    from src.models.tools_model import Tool

    try:

        with app.app_context():
            db.create_all()

        from .routes import register_routes

        register_routes(app)

        from src.routes.tools_routes import tools_bp

        app.register_blueprint(tools_bp)

    except Exception:
        pass

    return app
