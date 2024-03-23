# file mimesis/providers/numbers.py:47-54
# lines [47, 54]
# branches []

import pytest
from mimesis.providers import Numbers

@pytest.fixture
def numbers_provider():
    return Numbers()

def test_integer_number(numbers_provider):
    # Test the default range
    default_num = numbers_provider.integer_number()
    assert -1000 <= default_num <= 1000

    # Test a custom range
    start, end = 10, 20
    custom_num = numbers_provider.integer_number(start, end)
    assert start <= custom_num <= end

    # Test the edge cases
    edge_num_start = numbers_provider.integer_number(start, start)
    assert edge_num_start == start

    edge_num_end = numbers_provider.integer_number(end, end)
    assert edge_num_end == end

    # Test with negative range
    negative_num = numbers_provider.integer_number(-20, -10)
    assert -20 <= negative_num <= -10

    # Test with start greater than end
    with pytest.raises(ValueError):
        numbers_provider.integer_number(100, 10)
