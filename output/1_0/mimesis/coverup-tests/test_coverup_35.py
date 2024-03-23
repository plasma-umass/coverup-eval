# file mimesis/providers/business.py:19-26
# lines [19, 24, 25, 26]
# branches []

import pytest
from mimesis.providers.business import Business
from mimesis.exceptions import UnsupportedLocale


def test_business_init(mocker):
    # Mock the _pull method to ensure it's called with the correct datafile
    mocker.patch('mimesis.providers.business.BaseDataProvider._pull')

    # Create an instance of Business to trigger __init__
    business = Business()

    # Assert that _pull was called once with 'business.json'
    business._pull.assert_called_once_with('business.json')

    # Test with an unsupported locale to ensure it raises UnsupportedLocale
    with pytest.raises(UnsupportedLocale):
        Business(locale='unsupported_locale')

    # Clean up by unpatching the method
    mocker.stopall()
