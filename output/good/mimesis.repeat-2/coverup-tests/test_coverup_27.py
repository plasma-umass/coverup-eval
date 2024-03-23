# file mimesis/providers/base.py:89-103
# lines [89, 96, 97, 99, 100, 101, 103]
# branches ['96->97', '96->99', '100->101', '100->103']

import pytest
from mimesis.exceptions import UnsupportedLocale
from mimesis.providers.base import BaseDataProvider
from mimesis import locales

class DummyProvider(BaseDataProvider):
    pass

def test_base_data_provider_setup_locale_with_default_locale(mocker):
    mocker.patch('mimesis.providers.base.locales.DEFAULT_LOCALE', 'en')
    provider = DummyProvider()
    provider._setup_locale()
    assert provider.locale == 'en'

def test_base_data_provider_setup_locale_with_supported_locale(mocker):
    mocker.patch('mimesis.providers.base.locales.SUPPORTED_LOCALES', ['en', 'de'])
    provider = DummyProvider()
    provider._setup_locale('de')
    assert provider.locale == 'de'

def test_base_data_provider_setup_locale_with_unsupported_locale(mocker):
    mocker.patch('mimesis.providers.base.locales.SUPPORTED_LOCALES', ['en'])
    provider = DummyProvider()
    with pytest.raises(UnsupportedLocale):
        provider._setup_locale('unsupported_locale')

def test_base_data_provider_setup_locale_with_empty_locale(mocker):
    mocker.patch('mimesis.providers.base.locales.DEFAULT_LOCALE', 'en')
    mocker.patch('mimesis.providers.base.locales.SUPPORTED_LOCALES', ['en'])
    provider = DummyProvider()
    provider._setup_locale('')
    assert provider.locale == 'en'
