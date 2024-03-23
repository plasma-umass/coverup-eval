# file mimesis/builtins/ru.py:15-18
# lines [15, 17, 18]
# branches []

import pytest
from mimesis.builtins import RussiaSpecProvider

def test_russia_spec_provider_initialization(mocker):
    # Mock the _pull method to ensure it's called during initialization
    mocker.patch.object(RussiaSpecProvider, '_pull')

    # Create an instance of RussiaSpecProvider
    provider = RussiaSpecProvider()

    # Assert that the _pull method was called once with the correct datafile
    provider._pull.assert_called_once_with(provider._datafile)

    # Assert that the locale is set to 'ru'
    assert provider.locale == 'ru'
