# file mimesis/providers/text.py:79-90
# lines [79, 88, 89, 90]
# branches []

import pytest
from mimesis.providers.text import Text
from unittest.mock import patch

@pytest.fixture
def text_provider():
    return Text('en')

def test_words_default_quantity(text_provider):
    with patch.object(text_provider, '_data', {'words': {'normal': ['science', 'network', 'god', 'octopus', 'love']}}):
        words_list = text_provider.words()
        assert len(words_list) == 5
        assert all(word in ['science', 'network', 'god', 'octopus', 'love'] for word in words_list)

def test_words_custom_quantity(text_provider):
    custom_quantity = 10
    with patch.object(text_provider, '_data', {'words': {'normal': ['science', 'network', 'god', 'octopus', 'love']}}):
        words_list = text_provider.words(quantity=custom_quantity)
        assert len(words_list) == custom_quantity
        assert all(word in ['science', 'network', 'god', 'octopus', 'love'] for word in words_list)
