# file mimesis/providers/person.py:466-475
# lines [466, 474, 475]
# branches []

import pytest
from mimesis.providers.person import Person
from mimesis import Generic

@pytest.fixture
def person():
    generic = Generic()
    return generic.person

def test_language(person, mocker):
    # Mock the data to control the output
    languages = ['English', 'Spanish', 'Mandarin']
    mocker.patch.object(person, '_data', {'language': languages})
    mocker.patch.object(person.random, 'choice', side_effect=lambda x: x[0])

    # Call the method
    language = person.language()

    # Check that the first language in the mocked list is returned
    assert language == 'English'
