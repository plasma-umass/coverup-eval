# file mimesis/providers/person.py:317-326
# lines [317, 326]
# branches []

import pytest
from mimesis.providers.person import Person

def test_sex_method(mocker):
    person = Person()
    
    # Mock the gender method to ensure it is called with the correct arguments
    mock_gender = mocker.patch.object(person, 'gender', return_value='male')
    
    # Call the sex method with some arguments
    result = person.sex('arg1', kwarg1='value1')
    
    # Assert that the gender method was called with the same arguments
    mock_gender.assert_called_once_with('arg1', kwarg1='value1')
    
    # Assert that the result of the sex method is the same as the mocked return value of gender
    assert result == 'male'
