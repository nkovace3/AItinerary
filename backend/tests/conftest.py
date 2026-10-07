"""
Shared pytest fixtures.

`db_session` gives each test its own isolated SQLAlchemy session backed by
the real database (the same one docker-compose/.env point at). Isolation is
achieved with SQLAlchemy's "join an external transaction" pattern: we open
one connection-level transaction per test, bind the session to it with
`join_transaction_mode="create_savepoint"`, and roll the whole thing back at
teardown. Repository functions call `db.commit()` internally — that only
commits a SAVEPOINT under the hood, so nothing ever actually lands in the
database, and tests never pollute or depend on each other.

Requires the Postgres container (docker-compose.yml) to be running.
"""

import pytest
from sqlalchemy.orm import Session

from database import engine


@pytest.fixture
def db_session():
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection, join_transaction_mode="create_savepoint")

    yield session

    session.close()
    transaction.rollback()
    connection.close()
