# file mimesis/providers/numbers.py:56-71
# lines [56, 57, 71]
# branches []

import pytest
from mimesis.providers.numbers import Numbers

@pytest.fixture
def numbers_provider():
    return Numbers()

def test_integers(numbers_provider):
    start = -5
    end = 5
    n = 10
    result = numbers_provider.integers(start=start, end=end, n=n)
    assert len(result) == n
    assert all(start <= num <= end for num in result)
