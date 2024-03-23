# file mimesis/providers/text.py:124-133
# lines [124, 132, 133]
# branches []

import pytest
from mimesis.providers.text import Text
from mimesis.random import Random

@pytest.fixture
def text_provider():
    return Text()

def test_color(text_provider, mocker):
    # Mock the internal data with a known dictionary
    mocker.patch.object(text_provider, '_data', {'color': ['Red', 'Green', 'Blue']})
    
    # Mock the Random.choice method to return a specific value
    mocker.patch.object(Random, 'choice', return_value='Red')
    
    # Call the method
    color = text_provider.color()
    
    # Assert that the returned color is what we mocked
    assert color == 'Red'
