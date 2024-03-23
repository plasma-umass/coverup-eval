# file mimesis/providers/internet.py:161-169
# lines [161, 169]
# branches []

import pytest
from mimesis.providers.internet import Internet

@pytest.fixture
def internet_provider():
    return Internet()

def test_emoji(internet_provider):
    emoji = internet_provider.emoji()
    assert isinstance(emoji, str)
    assert emoji.startswith(':') and emoji.endswith(':')

    # Clean up is not necessary in this case, as the test does not modify any state
