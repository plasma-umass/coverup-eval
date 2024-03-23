# file mimesis/providers/business.py:92-112
# lines [92, 93, 100, 101, 102, 103, 104, 107, 108, 110, 112]
# branches []

import pytest
from mimesis.providers.business import Business


@pytest.fixture
def business_provider():
    return Business()


def test_price(business_provider):
    # Test the price method with different minimum and maximum values
    min_val = 10.00
    max_val = 1000.00
    price = business_provider.price(minimum=min_val, maximum=max_val)
    # Remove currency symbol and delimiters to convert to float
    clean_price = price.replace(business_provider._data['price-format'].replace('#', ''), '').replace(business_provider._data['numeric-thousands'], '')
    clean_price = clean_price.replace(business_provider._data['numeric-decimal'], '.')
    float_price = float(clean_price)
    # Check if the price is within the specified range
    assert min_val <= float_price <= max_val

    # Test the price method with equal minimum and maximum values
    equal_val = 500.00
    price = business_provider.price(minimum=equal_val, maximum=equal_val)
    # Remove currency symbol and delimiters to convert to float
    clean_price = price.replace(business_provider._data['price-format'].replace('#', ''), '').replace(business_provider._data['numeric-thousands'], '')
    clean_price = clean_price.replace(business_provider._data['numeric-decimal'], '.')
    float_price = float(clean_price)
    # Check if the price is equal to the specified value
    assert float_price == equal_val

    # The original code does not raise a ValueError, so we remove the incorrect test case
