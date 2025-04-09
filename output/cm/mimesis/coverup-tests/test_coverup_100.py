# file mimesis/providers/text.py:13-15
# lines [13, 14]
# branches []

import pytest
from mimesis.providers.text import Text
from mimesis import Generic

@pytest.fixture
def text_provider():
    return Text()

def test_text_provider(text_provider):
    assert isinstance(text_provider, Text)
    # Add more assertions here to test the functionality of Text class methods
