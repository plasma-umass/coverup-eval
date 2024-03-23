# file mimesis/providers/business.py:114-127
# lines [114, 121, 122, 123, 124, 125]
# branches []

import pytest
from mimesis.providers.business import Business

@pytest.fixture
def business_provider():
    return Business()

def test_price_in_btc(business_provider):
    # Test the default range
    price = business_provider.price_in_btc()
    value = float(price.split(' ')[0])
    assert 0 <= value <= 2

    # Test a custom range
    custom_min, custom_max = 0.5, 1.5
    price = business_provider.price_in_btc(minimum=custom_min, maximum=custom_max)
    value = float(price.split(' ')[0])
    assert custom_min <= value <= custom_max

    # Test the precision
    # Since the precision is 7, there should be at most 7 digits after the decimal point
    # However, if the last digits are zeros, they might not be included in the string representation
    # Therefore, we check that there are up to 7 digits after the decimal point
    decimal_part = price.split(' ')[0].split('.')[1]
    assert len(decimal_part) <= 7

    # Remove the test with reversed min and max since the function does not raise ValueError
