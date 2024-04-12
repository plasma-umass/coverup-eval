# file mimesis/providers/base.py:199-202
# lines [199, 201, 202]
# branches []

import pytest
from mimesis.providers.base import BaseDataProvider
from mimesis import locales

class TestBaseDataProvider:
    def test_str_representation(self):
        # Create a subclass to add a 'locale' attribute for testing
        class TestableBaseDataProvider(BaseDataProvider):
            locale = locales.DEFAULT_LOCALE

        provider = TestableBaseDataProvider()
        expected_str = '{} <{}>'.format(provider.__class__.__name__, locales.DEFAULT_LOCALE)
        
        assert str(provider) == expected_str, "The __str__ representation should match the expected format with the default locale"
        
        # Test with a different locale
        custom_locale = 'es'
        provider.locale = custom_locale
        expected_str = '{} <{}>'.format(provider.__class__.__name__, custom_locale)
        
        assert str(provider) == expected_str, "The __str__ representation should match the expected format with the custom locale"
