# file mimesis/providers/person.py:466-475
# lines [466, 474, 475]
# branches []

import pytest
from mimesis.providers.person import Person
from mimesis import Generic

@pytest.fixture
def person_provider():
    generic = Generic('en')
    return generic.person

def test_language(person_provider, mocker):
    # Mock the _data attribute to ensure the test is deterministic
    mock_languages = ['English', 'Spanish', 'French', 'German', 'Irish']
    mocker.patch.object(person_provider, '_data', {'language': mock_languages})
    
    # Call the language method and assert the result is one of the mock languages
    language = person_provider.language()
    assert language in mock_languages
