# file mimesis/providers/business.py:85-90
# lines [85, 90]
# branches []

import pytest
from mimesis.providers.business import Business

@pytest.fixture
def business_provider():
    return Business()

def test_cryptocurrency_symbol(business_provider):
    symbol = business_provider.cryptocurrency_symbol()
    assert symbol.isupper()  # Assuming cryptocurrency symbols are uppercase
