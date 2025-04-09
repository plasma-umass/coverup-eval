# file mimesis/providers/person.py:504-518
# lines [504, 518]
# branches []

import pytest
from mimesis.providers import Person
from pytest_mock import mocker

def test_identifier(mocker):
    person = Person()
    
    # Mock the random.custom_code method to control its output
    mock_custom_code = mocker.patch.object(person.random, 'custom_code', return_value='12-34/56')
    
    # Test the identifier method with a specific mask
    result = person.identifier(mask='##-##/##')
    
    # Assert that the custom_code method was called with the correct mask
    mock_custom_code.assert_called_once_with(mask='##-##/##')
    
    # Assert that the result is as expected
    assert result == '12-34/56'
