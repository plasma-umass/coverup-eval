# file mimesis/builtins/ru.py:66-75
# lines [66, 74, 75]
# branches []

import pytest
from mimesis.builtins.ru import RussiaSpecProvider

def test_passport_number(mocker):
    provider = RussiaSpecProvider()
    
    # Mock the random.randint method to control its output
    mock_randint = mocker.patch.object(provider.random, 'randint', return_value=560430)
    
    passport_number = provider.passport_number()
    
    # Assert that the mocked randint method was called with the correct arguments
    mock_randint.assert_called_once_with(100000, 999999)
    
    # Assert that the passport number is as expected
    assert passport_number == 560430
