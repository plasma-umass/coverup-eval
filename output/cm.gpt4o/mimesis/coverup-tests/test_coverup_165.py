# file mimesis/providers/base.py:89-103
# lines [97]
# branches ['96->97']

import pytest
from mimesis.providers.base import BaseDataProvider
from mimesis.exceptions import UnsupportedLocale
from mimesis import locales

def test_setup_locale_with_empty_locale():
    provider = BaseDataProvider()
    
    # Test with empty locale to trigger the default assignment
    provider._setup_locale('')
    
    # Assert that the locale is set to the default locale
    assert provider.locale == locales.DEFAULT_LOCALE

def test_setup_locale_with_none_locale():
    provider = BaseDataProvider()
    
    # Test with None as locale to trigger the default assignment
    provider._setup_locale(None)
    
    # Assert that the locale is set to the default locale
    assert provider.locale == locales.DEFAULT_LOCALE
