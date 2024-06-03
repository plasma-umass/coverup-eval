# file mimesis/builtins/ru.py:15-18
# lines [15, 17, 18]
# branches []

import pytest
from mimesis.builtins.ru import RussiaSpecProvider
from mimesis.providers.base import BaseProvider

def test_russia_spec_provider_initialization(mocker):
    # Mock the _pull method to ensure it is called
    mock_pull = mocker.patch.object(RussiaSpecProvider, '_pull', autospec=True)

    # Create an instance of RussiaSpecProvider
    provider = RussiaSpecProvider(seed=1234)

    # Assert that the locale is set correctly
    assert provider.locale == 'ru'

    # Assert that the seed is set correctly
    assert provider.seed == 1234

    # Assert that the _pull method was called with the correct datafile
    mock_pull.assert_called_once_with(provider._datafile)
