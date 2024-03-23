# file mimesis/providers/person.py:30-41
# lines [30, 36, 37, 38, 39, 40]
# branches []

import pytest
from mimesis.providers import Person
from unittest.mock import patch

@pytest.fixture
def mock_pull():
    with patch('mimesis.providers.person.Person._pull') as mock:
        yield mock

def test_person_init(mock_pull):
    seed = 12345
    person = Person(seed=seed)

    assert person._datafile == 'person.json'
    assert person._store == {'age': 0}
    mock_pull.assert_called_once_with('person.json')
