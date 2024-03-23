# file mimesis/providers/numbers.py:136-145
# lines [145]
# branches []

import pytest
from mimesis.providers import Numbers
from decimal import Decimal

@pytest.fixture
def numbers_provider():
    return Numbers()

def test_decimals(numbers_provider):
    start = 10.0
    end = 20.0
    n = 5
    decimals_list = numbers_provider.decimals(start=start, end=end, n=n)
    assert len(decimals_list) == n
    assert all(isinstance(num, Decimal) for num in decimals_list)
    assert all(start <= num <= end for num in decimals_list)
