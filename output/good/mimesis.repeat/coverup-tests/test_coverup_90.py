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
    quote = text_provider.quote()
    assert quote in text_provider._data['quotes']
