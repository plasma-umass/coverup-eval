# file mimesis/providers/person.py:382-391
# lines [382, 390, 391]
# branches []

import pytest
from mimesis.providers.person import Person
from mimesis import Generic

@pytest.fixture
def person_provider():
    generic = Generic('en')
    return generic.person

def test_occupation(person_provider, mocker):
    mock_data = {'occupation': ['Programmer', 'Engineer', 'Artist']}
    mocker.patch.object(person_provider, '_data', mock_data)
    
    job = person_provider.occupation()
    assert job in mock_data['occupation']
