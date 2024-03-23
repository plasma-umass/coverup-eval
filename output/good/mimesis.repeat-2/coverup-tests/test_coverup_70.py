# file mimesis/providers/text.py:31-41
# lines [31, 37, 38, 40, 41]
# branches []

import pytest
from mimesis.providers.text import Text

@pytest.fixture
def text_provider():
    return Text('en')

def test_alphabet_uppercase(text_provider):
    uppercase_alphabet = text_provider.alphabet()
    assert uppercase_alphabet == text_provider._data['alphabet']['uppercase']
    assert all(letter.isupper() for letter in uppercase_alphabet)

def test_alphabet_lowercase(text_provider):
    lowercase_alphabet = text_provider.alphabet(lower_case=True)
    assert lowercase_alphabet == text_provider._data['alphabet']['lowercase']
    assert all(letter.islower() for letter in lowercase_alphabet)
