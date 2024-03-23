# file mimesis/providers/numbers.py:22-32
# lines [22, 23, 32]
# branches []

import pytest
from mimesis.providers import Numbers

@pytest.fixture
def numbers_provider():
    return Numbers()

def test_float_number(numbers_provider):
    start = 10.5
    end = 20.5
    precision = 2
    result = numbers_provider.float_number(start=start, end=end, precision=precision)
    assert start <= result <= end
    assert len(str(result).split('.')[1]) <= precision

def test_float_number_default_precision(numbers_provider):
    start = 0.0
    end = 1.0
    result = numbers_provider.float_number(start=start, end=end)
    assert start <= result <= end
    assert len(str(result).split('.')[1]) <= 15
