# file mimesis/providers/base.py:89-103
# lines [89, 96, 97, 99, 100, 101, 103]
# branches ['96->97', '96->99', '100->101', '100->103']

import pytest
from mimesis.exceptions import UnsupportedLocale
from mimesis.providers.base import BaseDataProvider
from mimesis import locales

def test_base_data_provider_setup_locale_with_unsupported_locale():
    provider = BaseDataProvider()
    with pytest.raises(UnsupportedLocale):
        provider._setup_locale(locale='unsupported_locale')

def test_base_data_provider_setup_locale_with_supported_locale():
    provider = BaseDataProvider()
    supported_locale = list(locales.SUPPORTED_LOCALES)[0]
    provider._setup_locale(locale=supported_locale)
    assert provider.locale == supported_locale.lower()

def test_base_data_provider_setup_locale_with_default_locale():
    provider = BaseDataProvider()
    provider._setup_locale(locale='')
    assert provider.locale == locales.DEFAULT_LOCALE.lower()
