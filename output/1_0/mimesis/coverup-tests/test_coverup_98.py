# file mimesis/providers/business.py:33-38
# lines [33, 38]
# branches []

import pytest
from mimesis.providers.business import Business

@pytest.fixture
def business_provider():
    return Business()

def test_company(business_provider):
    company_name = business_provider.company()
    assert company_name in business_provider._data['company']['name']
