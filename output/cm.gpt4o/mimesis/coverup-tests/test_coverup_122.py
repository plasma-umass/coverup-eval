# file mimesis/providers/text.py:13-15
# lines [13, 14]
# branches []

import pytest
from mimesis.providers.text import Text

def test_text_provider_initialization():
    # Test the initialization of the Text provider
    text_provider = Text()
    assert isinstance(text_provider, Text)

    # Test some basic functionality if applicable
    # For example, if Text has a method called 'word', we can test it
    if hasattr(text_provider, 'word'):
        word = text_provider.word()
        assert isinstance(word, str)
        assert len(word) > 0

# Clean up after the test if necessary
@pytest.fixture(autouse=True)
def cleanup(mocker):
    yield
    mocker.stopall()
