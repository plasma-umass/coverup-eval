# file mimesis/providers/text.py:65-70
# lines [65, 70]
# branches []

import pytest
from mimesis.providers.text import Text

@pytest.fixture
def text_provider():
    return Text()

def test_sentence(text_provider, mocker):
    # Mock the text method to ensure it is called with the correct parameters
    mocker.patch.object(text_provider, 'text', return_value='Mocked sentence.')
    
    # Call the sentence method
    result = text_provider.sentence()
    
    # Assert that the text method was called once with the correct parameter
    text_provider.text.assert_called_once_with(quantity=1)
    
    # Assert that the result is the mocked sentence
    assert result == 'Mocked sentence.'
