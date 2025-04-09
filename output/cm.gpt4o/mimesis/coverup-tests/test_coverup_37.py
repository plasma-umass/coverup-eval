# file mimesis/providers/text.py:31-41
# lines [31, 37, 38, 40, 41]
# branches []

import pytest
from mimesis.providers.text import Text

@pytest.fixture
def text_provider():
    return Text()

def test_alphabet_uppercase(text_provider):
    alphabet = text_provider.alphabet(lower_case=False)
    assert alphabet is not None
    assert all(char.isupper() for char in alphabet)

def test_alphabet_lowercase(text_provider):
    alphabet = text_provider.alphabet(lower_case=True)
    assert alphabet is not None
    assert all(char.islower() for char in alphabet)
