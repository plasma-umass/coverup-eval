# file mimesis/providers/base.py:199-202
# lines [199, 201, 202]
# branches []

import pytest
from mimesis import locales
from mimesis.providers.base import BaseDataProvider

def test_base_data_provider_str_representation(mocker):
    # Mocking the BaseDataProvider to add a locale attribute
    mocker.patch.object(BaseDataProvider, 'locale', 'en', create=True)
    provider = BaseDataProvider()

    # Asserting the __str__ method returns the expected string
    assert str(provider) == 'BaseDataProvider <en>'

    # Cleanup is not necessary as mocker.patch will undo the mocking after the test
