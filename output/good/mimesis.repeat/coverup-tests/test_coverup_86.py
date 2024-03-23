# file mimesis/providers/text.py:43-52
# lines [43, 51, 52]
# branches []

import pytest
from mimesis.providers.text import Text
from mimesis import Generic

@pytest.fixture
def text_provider():
    return Text()

def test_level(text_provider):
    # Mock the data to ensure the test is predictable
    text_provider._data = {'level': ['low', 'medium', 'high', 'critical']}
    
    # Generate a level and assert it is in the predefined levels
    level = text_provider.level()
    assert level in text_provider._data['level']

    # Clean up is not necessary as the fixture will provide a fresh instance for each test
