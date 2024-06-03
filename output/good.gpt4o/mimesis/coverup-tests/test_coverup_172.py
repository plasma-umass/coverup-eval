# file mimesis/providers/person.py:444-453
# lines [452, 453]
# branches []

import pytest
from mimesis.providers import Person
from unittest.mock import patch

def test_university(mocker):
    person = Person()
    mock_data = {'university': ['MIT', 'Harvard', 'Stanford']}
    
    # Mock the _data attribute to ensure the specific lines are executed
    mocker.patch.object(person, '_data', mock_data)
    
    # Mock the random.choice method to control the output
    mocker.patch.object(person.random, 'choice', side_effect=lambda x: x[0])
    
    university = person.university()
    
    # Assert that the university returned is the first one in the mock list
    assert university == 'MIT'
