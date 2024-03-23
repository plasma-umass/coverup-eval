# file mimesis/providers/address.py:66-72
# lines [66, 72]
# branches []

import pytest
from mimesis.providers.address import Address
from mimesis import Generic

@pytest.fixture
def address():
    return Generic('en').address

def test_street_number_default(address):
    # Test the default maximum value
    number = address.street_number()
    assert number.isdigit()
    assert 1 <= int(number) <= 1400

def test_street_number_custom_max(address):
    # Test a custom maximum value
    custom_max = 2000
    number = address.street_number(maximum=custom_max)
    assert number.isdigit()
    assert 1 <= int(number) <= custom_max

def test_street_number_edge_case(address):
    # Test the edge case where maximum is 1
    number = address.street_number(maximum=1)
    assert number == '1'
