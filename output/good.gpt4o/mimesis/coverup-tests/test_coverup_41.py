# file mimesis/builtins/ru.py:77-88
# lines [77, 85, 86, 87]
# branches []

import pytest
from mimesis.builtins.ru import RussiaSpecProvider

def test_series_and_number(mocker):
    provider = RussiaSpecProvider()

    # Mock the methods to ensure they are called and return specific values
    mocker.patch.object(provider, 'passport_series', return_value='57 16 ')
    mocker.patch.object(provider, 'passport_number', return_value='805199')

    result = provider.series_and_number()

    # Assert that the result is as expected
    assert result == '57 16 805199'

    # Assert that the mocked methods were called
    provider.passport_series.assert_called_once()
    provider.passport_number.assert_called_once()
