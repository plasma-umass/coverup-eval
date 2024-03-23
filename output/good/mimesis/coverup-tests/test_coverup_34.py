# file mimesis/providers/base.py:89-103
# lines [89, 96, 97, 99, 100, 101, 103]
# branches ['96->97', '96->99', '100->101', '100->103']

import pytest
from mimesis.exceptions import UnsupportedLocale
from mimesis.providers.base import BaseDataProvider
from mimesis import locales

class DummyProvider(BaseDataProvider):
    pass

def test_setup_locale_with_default_locale(mocker):
    mocker.patch('mimesis.providers.base.locales.DEFAULT_LOCALE', 'en')
    provider = DummyProvider()
    provider._setup_locale()
    assert provider.locale == 'en'

def test_setup_locale_with_supported_locale(mocker):
    mocker.patch('mimesis.providers.base.locales.SUPPORTED_LOCALES', ['en', 'ru'])
    provider = DummyProvider()
    provider._setup_locale('ru')
    assert provider.locale == 'ru'

def test_setup_locale_with_unsupported_locale(mocker):
    mocker.patch('mimesis.providers.base.locales.SUPPORTED_LOCALES', ['en'])
    provider = DummyProvider()
    with pytest.raises(UnsupportedLocale):
        provider._setup_locale('unsupported_locale')
