import pytest
from ml_flask_restx.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


@pytest.fixture()
def data_dict():
    return {
            'sepal_length': 0,
            'sepal_width': 0,
            'petal_length': 0,
            'petal_width': 0,
        }