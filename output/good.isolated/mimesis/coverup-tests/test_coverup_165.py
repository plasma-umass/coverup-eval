# file mimesis/providers/text.py:43-52
# lines [51, 52]
# branches []

import pytest
from mimesis.providers.text import Text
from mimesis.random import Random

@pytest.fixture
def text_provider():
    return Text('en')

def test_level(text_provider, mocker):
    # Mock the internal data to contain a predictable 'level' list
    mocker.patch.object(text_provider, '_data', {'level': ['low', 'medium', 'high']})
    
    # Mock the random.choice method to return a specific value
    random_instance = Random()
    mocker.patch.object(random_instance, 'choice', return_value='medium')
    text_provider.random = random_instance
    
    # Call the method under test
    level = text_provider.level()
    
    # Assert that the return value is as expected
    assert level == 'medium'
