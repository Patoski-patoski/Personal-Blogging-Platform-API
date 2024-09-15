#!/usr/bin/env python3
"""app/config/__init__.py"""

import yaml
import os

# Load database configuration from config.yaml
with open(os.path.join(os.path.dirname(__file__), 'config.yaml'), 'r') as db_file:
    db_config = yaml.safe_load(db_file)

user = db_config["mysql_user"]
password = db_config["mysql_password"]
host = db_config["mysql_host"]
database = db_config["mysql_db"]
port = db_config["mysql_port"]
