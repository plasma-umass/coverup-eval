# file mimesis/providers/base.py:199-202
# lines [199, 201, 202]
# branches []

import pytest
from mimesis import locales
from mimesis.providers.base import BaseDataProvider

def test_base_data_provider_str_representation():
    provider = BaseDataProvider()
    default_str = '{} <{}>'.format(BaseDataProvider.__name__, locales.DEFAULT_LOCALE)
    assert str(provider) == default_str

    # Mocking the locale attribute to test a different locale
    provider.locale = 'es'
    es_str = '{} <{}>'.format(BaseDataProvider.__name__, 'es')
    assert str(provider) == es_str
