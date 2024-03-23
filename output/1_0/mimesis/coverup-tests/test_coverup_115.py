# file mimesis/providers/business.py:40-49
# lines [46, 47, 48]
# branches []

import pytest
from mimesis.providers.business import Business


@pytest.fixture
def business_provider():
    return Business()


def test_company_type_full_coverage(business_provider):
    # Test the non-abbreviated company type
    company_type_full = business_provider.company_type(abbr=False)
    assert isinstance(company_type_full, str)
    assert len(company_type_full) > 0

    # Test the abbreviated company type
    company_type_abbr = business_provider.company_type(abbr=True)
    assert isinstance(company_type_abbr, str)
    assert len(company_type_abbr) > 0
    assert company_type_abbr != company_type_full
