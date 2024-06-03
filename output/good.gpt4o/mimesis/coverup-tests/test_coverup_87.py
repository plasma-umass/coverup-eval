# file mimesis/providers/person.py:393-402
# lines [393, 401, 402]
# branches []

import pytest
from mimesis.providers.person import Person
from mimesis import Generic

@pytest.fixture
def person():
    generic = Generic('en')
    return generic.person

def test_political_views(person, mocker):
    # Mock the _data attribute to ensure the test is deterministic
    mock_data = {'political_views': ['Liberal', 'Conservative', 'Moderate']}
    mocker.patch.object(person, '_data', mock_data)
    
    # Mock the random.choice method to return a specific value
    mocker.patch.object(person.random, 'choice', return_value='Liberal')
    
    # Call the method and assert the expected value
    result = person.political_views()
    assert result == 'Liberal'
