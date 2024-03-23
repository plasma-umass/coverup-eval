# file mimesis/random.py:97-105
# lines [97, 105]
# branches []

import pytest
from mimesis.random import Random

@pytest.fixture
def mock_random(mocker):
    mocker.patch('mimesis.random.random_module.Random.random', return_value=0.5)

def test_uniform_with_precision(mock_random):
    random_instance = Random()
    result = random_instance.uniform(1.0, 2.0, precision=2)
    assert result == 1.50, "The result should be 1.50 with precision 2"
