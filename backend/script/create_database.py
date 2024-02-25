"""Create database in blank development environment.

This script is used in the developer container setup process. Its sole purpose
is to create a postgres database from database connection environment variables.

Usage: python3 -m script.create_database
"""

import sqlalchemy
import sys

engine = sqlalchemy.create_engine("postgresql+psycopg2://postgres@localhost:5432", echo=True)



with engine.connect() as connection:
    connection.execute(
        sqlalchemy.text("COMMIT")
    )  # Hack: CREATE DATABASE cannot begin inside a transaction.
    database = "pearlhacks"
    stmt = sqlalchemy.text(f"CREATE DATABASE {database}")
    connection.execute(stmt)