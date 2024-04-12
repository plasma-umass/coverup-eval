# file mimesis/providers/text.py:92-100
# lines [92, 100]
# branches []

import pytest
from mimesis.providers.text import Text


@pytest.fixture
def text_provider():
    return Text('en')


def test_word(text_provider):
    word = text_provider.word()
    assert isinstance(word, str)
    assert len(word) > 0
