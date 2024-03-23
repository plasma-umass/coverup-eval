# file mimesis/providers/business.py:40-49
# lines [40, 46, 47, 48]
# branches []

import pytest
from mimesis.providers.business import Business


@pytest.fixture
def business_provider():
    return Business()


def test_company_type_full_coverage(business_provider):
    # Test for abbreviated company type
    company_type_abbr = business_provider.company_type(abbr=True)
    assert company_type_abbr.isupper(), "Abbreviated company type should be uppercase"

    # Test for full company type
    company_type_full = business_provider.company_type(abbr=False)
    assert not company_type_full.isupper(), "Full company type should not be uppercase"

    # Clean up is not necessary as the Business provider does not modify any external state
