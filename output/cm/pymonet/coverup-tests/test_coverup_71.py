# file pymonet/either.py:14-15
# lines [14, 15]
# branches []

import pytest
from pymonet.either import Either

@pytest.fixture
def either_instance():
    return Either('test_value')

def test_either_initialization(either_instance):
    assert either_instance.value == 'test_value', "Either did not initialize with the correct value"
