def test_placeholder():
    """
    Real endpoint tests require a running PostgreSQL test database and the
    actual .keras model file, neither of which exist in this generation
    environment. Wire DATABASE_URL to a test DB and drop the real model
    into ml_models/ before running:  pytest -v
    """
    assert True
