# file mimesis/providers/text.py:113-122
# lines [113, 121, 122]
# branches []

import pytest
from mimesis.providers.text import Text
from mimesis import Generic

@pytest.fixture
def text_provider():
    return Text()

def test_quote(text_provider):
    # Mock the data to ensure the test is predictable
    text_provider._data = {'quotes': ["Bond... James Bond.", "May the Force be with you."]}
    
    # Test that quote is one of the provided quotes
    quote = text_provider.quote()
    assert quote in text_provider._data['quotes']
