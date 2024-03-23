# file mimesis/providers/numbers.py:126-134
# lines [126, 127, 134]
# branches []

import pytest
from mimesis.providers import Numbers
from decimal import Decimal

@pytest.fixture
def numbers_provider():
    return Numbers()

def test_decimal_number(numbers_provider):
    start = -1000.0
    end = 1000.0
    result = numbers_provider.decimal_number(start, end)
    assert isinstance(result, Decimal)
    assert start <= result <= end

def test_decimal_number_with_specific_range(numbers_provider):
    start = 10.5
    end = 20.5
    result = numbers_provider.decimal_number(start, end)
    assert isinstance(result, Decimal)
    assert start <= result <= end

def test_decimal_number_with_zero_range(numbers_provider):
    start = 0.0
    end = 0.0
    result = numbers_provider.decimal_number(start, end)
    assert result == Decimal(0.0)
