# file mimesis/providers/text.py:72-77
# lines [72, 77]
# branches []

import pytest
from mimesis.providers.text import Text

def test_text_title(mocker):
    # Mock the text method to ensure it returns a predictable value
    mocker.patch.object(Text, 'text', return_value='Mocked Title')
    
    text_provider = Text()
    title = text_provider.title()
    
    # Assert that the title method returns the value from the text method
    assert title == 'Mocked Title'
