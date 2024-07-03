import logging
import logging.config


from blog_platform.api import api_v1
from flask import Flask, request
from sqlalchemy_utils import create_database, database_exists

from blog_platform.config import config_by_name
from blog_platform.core.database.db import db
from blog_platform.utils.error_handlers import register_error_handlers

def make_app(config_name=None):
    config = config_by_name[config_name]
    app = Flask(config.APP_NAME)
    # register_error_handlers(app)

    db_connection_uri = f"{config.DB_DIALECT}://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"
    app.config['SQLALCHEMY_DATABASE_URI'] = db_connection_uri
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        "pool_size": 30,
        "max_overflow": 15,
        "pool_recycle": 60,
        "pool_pre_ping": True
    }

    if not database_exists(db_connection_uri):
        create_database(db_connection_uri)

    db.init_app(app)
    app.config.from_object(config)
    app.register_blueprint(api_v1)

    # logging.basicConfig(level=logging.DEBUG)
    # logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=False)
    logger = logging.getLogger(__name__)
    with app.app_context():
        # logging.config.fileConfig(app.config.get('LOG_CONFIG_PATH'))
        db.create_all()

    return app


def main():
    app = make_app('dev')
    host = "0.0.0.0"
    port = "5000"
    app.run(host=host, port=port, debug=False)


if __name__ == "__main__":
    main()
