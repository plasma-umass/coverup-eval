# file mimesis/providers/business.py:51-59
# lines [51, 56, 57, 58]
# branches []

import pytest
from mimesis.providers.business import Business

@pytest.fixture
def business_provider():
    return Business()

def test_copyright(business_provider, mocker):
    # Mock the company and company_type methods to return predictable values
    mocker.patch.object(business_provider, 'company', return_value='TestCompany')
    mocker.patch.object(business_provider, 'company_type', return_value='LLC')

    # Call the method under test
    result = business_provider.copyright()

    # Assert that the result is as expected
    assert result == '© TestCompany, LLC'

    # Cleanup is handled by the mocker fixture, which undoes all patches after the test
