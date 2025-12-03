from flask import Flask
from extensions import db
from flask_migrate import Migrate

app = Flask(__name__)

# Basic config for SQLite + SQLAlchemy
app.config.setdefault('SQLALCHEMY_DATABASE_URI', 'sqlite:///tasks.db')
app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)

# Initialize extensions
# Initialize extensions
db.init_app(app)
migrate = Migrate()
migrate.init_app(app, db)

# Register routes from the separate module
from routes import register_routes
register_routes(app)

# Ensure models are imported so Flask-Migrate can detect them
import models  # noqa: F401 (import for side-effects)


if __name__ == '__main__':
    # Ensure database tables exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)