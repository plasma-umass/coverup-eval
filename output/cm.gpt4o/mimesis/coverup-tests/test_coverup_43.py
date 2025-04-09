# file mimesis/providers/person.py:30-41
# lines [30, 36, 37, 38, 39, 40]
# branches []

import pytest
from mimesis.providers.person import Person

@pytest.fixture
def mock_pull(mocker):
    return mocker.patch('mimesis.providers.person.Person._pull')

def test_person_initialization(mock_pull):
    person = Person(locale='en', seed=42)
    
    # Verify that the _pull method was called with the correct datafile
    mock_pull.assert_called_once_with('person.json')
    
    # Verify that the _store attribute is initialized correctly
    assert person._store == {'age': 0}
