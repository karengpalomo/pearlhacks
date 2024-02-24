"""Reset the database by dropping all tables, creating tables, and inserting demo data."""

import sys
from sqlalchemy.orm import Session
from ..database import engine
from .. import entities

# python3 -m backend.script.reset_database

__authors__ = ["Kris Jordan"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"



# python3 -m backend.script.reset_database

# Reset Tables
entities.EntityBase.metadata.drop_all(engine)
entities.EntityBase.metadata.create_all(engine)