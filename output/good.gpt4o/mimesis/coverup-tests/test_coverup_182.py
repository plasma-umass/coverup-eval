# file mimesis/providers/base.py:199-202
# lines [201, 202]
# branches []

import pytest
from mimesis.providers.base import BaseDataProvider
from mimesis.locales import DEFAULT_LOCALE

class CustomProvider(BaseDataProvider):
    pass

def test_base_data_provider_str_with_locale(mocker):
    # Mock the locale attribute
    provider = CustomProvider()
    mocker.patch.object(provider, 'locale', 'en')
    result = str(provider)
    assert result == 'CustomProvider <en>'

def test_base_data_provider_str_without_locale():
    provider = CustomProvider()
    result = str(provider)
    assert result == f'CustomProvider <{DEFAULT_LOCALE}>'
