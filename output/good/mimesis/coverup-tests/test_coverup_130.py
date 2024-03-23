# file mimesis/providers/person.py:317-326
# lines [317, 326]
# branches []

import pytest
from unittest.mock import patch
from mimesis.providers.person import Person

@pytest.fixture
def person_provider():
    return Person()

def test_sex_method(person_provider):
    # Test the alias method sex, which should call gender internally
    # We will use unittest.mock.patch to ensure that the gender method is called
    with patch.object(person_provider, 'gender') as mock_gender:
        # Call the sex method with some arguments
        args = ('arg1', 'arg2')
        kwargs = {'key1': 'value1', 'key2': 'value2'}
        person_provider.sex(*args, **kwargs)

        # Assert that the gender method was called with the same arguments
        mock_gender.assert_called_once_with(*args, **kwargs)
