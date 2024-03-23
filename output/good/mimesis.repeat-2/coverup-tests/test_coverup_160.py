# file mimesis/providers/person.py:317-326
# lines [326]
# branches []

import pytest
from mimesis.providers.person import Person
from unittest.mock import patch

@pytest.fixture
def person_provider():
    return Person()

def test_sex_method(person_provider):
    # Mock the gender method to ensure it's being called
    with patch.object(person_provider, 'gender', return_value='Male') as mock_gender:
        # Call the sex method which should call the gender method
        result = person_provider.sex()
        # Check that the gender method was called once
        mock_gender.assert_called_once()
        # Check that the result of sex method is the same as the gender method
        assert result == 'Male'
