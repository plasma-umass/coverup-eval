# file mimesis/providers/person.py:404-413
# lines [404, 412, 413]
# branches []

import pytest
from mimesis.providers.person import Person
from mimesis import Generic

@pytest.fixture
def person():
    generic = Generic()
    return generic.person

def test_worldview(person, mocker):
    # Mock the data to control the output
    mocker.patch.object(person, '_data', {'worldview': ['Pantheism', 'Atheism', 'Theism']})
    
    # Mock the random.choice method to return a specific value
    mocker.patch('mimesis.random.Random.choice', return_value='Pantheism')
    
    # Call the method
    worldview = person.worldview()
    
    # Assert that the returned value is what we mocked
    assert worldview == 'Pantheism'
