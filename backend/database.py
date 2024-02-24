import os
import sqlalchemy
from sqlalchemy.orm import Session


engine = sqlalchemy.create_engine("postgresql+psycopg2://postgres:MasterYoshi1!@152.23.211.102:5432", echo=True)
"""SQLAlchemy database engine for app"""


def db_session():
    """Generator function for SQLAlchemy Sessions."""
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()