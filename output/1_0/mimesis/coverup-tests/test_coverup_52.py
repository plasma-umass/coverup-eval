# file mimesis/providers/business.py:28-31
# lines [28, 29, 31]
# branches []

import pytest
from mimesis.providers.business import Business
from mimesis import Generic

@pytest.fixture
def business_provider():
    return Business()

def test_business_meta(business_provider):
    assert business_provider.Meta.name == 'business'
