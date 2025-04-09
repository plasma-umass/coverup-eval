# file mimesis/random.py:97-105
# lines [97, 105]
# branches []

import pytest
from mimesis.random import Random

@pytest.fixture
def random_instance():
    return Random()

def test_uniform_precision(random_instance):
    a = 1.5
    b = 2.5
    precision = 2
    result = random_instance.uniform(a, b, precision)
    assert round(result, precision) == result
    assert a <= result < b

def test_uniform_default_precision(random_instance):
    a = 1.5
    b = 2.5
    result = random_instance.uniform(a, b)
    assert round(result, 15) == result
    assert a <= result < b
