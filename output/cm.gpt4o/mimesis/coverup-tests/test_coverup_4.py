# file mimesis/providers/base.py:89-103
# lines [89, 96, 97, 99, 100, 101, 103]
# branches ['96->97', '96->99', '100->101', '100->103']

import pytest
from mimesis.providers.base import BaseDataProvider, UnsupportedLocale
from mimesis import locales

def test_setup_locale_default(mocker):
    provider = BaseDataProvider()
    mocker.patch('mimesis.locales.DEFAULT_LOCALE', 'en')
    provider._setup_locale()
    assert provider.locale == 'en'

def test_setup_locale_supported():
    provider = BaseDataProvider()
    provider._setup_locale('en')
    assert provider.locale == 'en'

def test_setup_locale_unsupported():
    provider = BaseDataProvider()
    with pytest.raises(UnsupportedLocale):
        provider._setup_locale('unsupported_locale')
