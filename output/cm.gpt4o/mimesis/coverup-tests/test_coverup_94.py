# file mimesis/providers/text.py:43-52
# lines [43, 51, 52]
# branches []

import pytest
from mimesis.providers.text import Text
from mimesis import Generic

@pytest.fixture
def text_provider():
    generic = Generic()
    return generic.text

def test_level(text_provider, mocker):
    # Mock the _data attribute to ensure the test is deterministic
    mock_data = {'level': ['low', 'medium', 'high', 'critical']}
    mocker.patch.object(text_provider, '_data', mock_data)
    
    # Call the method and assert the result is one of the expected levels
    result = text_provider.level()
    assert result in mock_data['level']
