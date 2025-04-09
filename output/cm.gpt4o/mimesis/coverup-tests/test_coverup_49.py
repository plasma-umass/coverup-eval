# file mimesis/providers/text.py:79-90
# lines [79, 88, 89, 90]
# branches []

import pytest
from mimesis.providers.text import Text
from mimesis import Generic

@pytest.fixture
def text_provider():
    generic = Generic()
    return generic.text

def test_words_quantity(text_provider):
    # Test with default quantity
    words = text_provider.words()
    assert len(words) == 5
    assert all(isinstance(word, str) for word in words)

    # Test with specific quantity
    quantity = 10
    words = text_provider.words(quantity=quantity)
    assert len(words) == quantity
    assert all(isinstance(word, str) for word in words)

    # Test with zero quantity
    words = text_provider.words(quantity=0)
    assert len(words) == 0

    # Test with negative quantity
    words = text_provider.words(quantity=-5)
    assert len(words) == 0

    # Test with large quantity
    quantity = 1000
    words = text_provider.words(quantity=quantity)
    assert len(words) == quantity
    assert all(isinstance(word, str) for word in words)
