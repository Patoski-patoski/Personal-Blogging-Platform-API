#!/usr/bin/env python3
"""app/__init__.py"""

from flask import Flask
from .config import db_config

def create_app():
    app = Flask(__name__)

    # Add configuration from YAML
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql://{db_config['mysql_user']}:{db_config['mysql_password']}"
        f"@{db_config['mysql_host']}:{db_config['mysql_port']}/{db_config['mysql_db']}"
    )

    # May import Blueprints here if any

    return app
