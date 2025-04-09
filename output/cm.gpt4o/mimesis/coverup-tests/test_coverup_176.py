# file mimesis/providers/person.py:404-413
# lines [412, 413]
# branches []

import pytest
from mimesis.providers import Person
from unittest.mock import patch

def test_worldview(mocker):
    person = Person()
    mock_data = {'worldview': ['Pantheism', 'Atheism', 'Agnosticism']}
    
    # Mock the _data attribute
    mocker.patch.object(person, '_data', mock_data)
    
    # Mock the random.choice method to return a specific value
    mocker.patch.object(person.random, 'choice', side_effect=lambda x: x[0])
    
    result = person.worldview()
    
    # Assert that the result is one of the mocked worldviews
    assert result in mock_data['worldview']
    assert result == 'Pantheism'
