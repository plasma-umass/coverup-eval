# file mimesis/providers/transport.py:61-69
# lines [61, 69]
# branches []

import pytest
from mimesis.providers.transport import Transport
from mimesis.data import CARS

@pytest.fixture
def transport():
    return Transport()

def test_car(transport):
    car = transport.car()
    assert car in CARS
