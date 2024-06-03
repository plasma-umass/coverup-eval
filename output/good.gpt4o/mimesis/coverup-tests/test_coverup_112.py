# file mimesis/providers/person.py:115-123
# lines [115, 123]
# branches []

import pytest
from mimesis.providers.person import Person
from mimesis.enums import Gender

@pytest.fixture
def person():
    return Person()

def test_last_name_calls_surname(mocker, person):
    mock_surname = mocker.patch.object(person, 'surname', return_value='Doe')
    result = person.last_name(Gender.MALE)
    mock_surname.assert_called_once_with(Gender.MALE)
    assert result == 'Doe'
