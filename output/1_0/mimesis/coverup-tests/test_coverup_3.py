# file mimesis/exceptions.py:12-24
# lines [12, 13, 15, 20, 21, 23, 24]
# branches []

import pytest
from mimesis.exceptions import UnsupportedLocale

def test_unsupported_locale_exception():
    locale = 'xx-xx'
    exception = UnsupportedLocale(locale)
    
    assert str(exception) == 'Locale «xx-xx» is not supported'
    assert exception.locale == locale
