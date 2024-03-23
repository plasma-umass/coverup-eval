# file mimesis/builtins/ru.py:77-88
# lines [85, 86, 87]
# branches []

import pytest
from mimesis.builtins.ru import RussiaSpecProvider

def test_series_and_number(mocker):
    # Mock the passport_series and passport_number methods
    mocker.patch.object(RussiaSpecProvider, 'passport_series', return_value='57 16 ')
    mocker.patch.object(RussiaSpecProvider, 'passport_number', return_value='805199')

    provider = RussiaSpecProvider()

    # Call the method under test
    result = provider.series_and_number()

    # Assert that the result is the concatenation of the series and number
    assert result == '57 16 805199'
