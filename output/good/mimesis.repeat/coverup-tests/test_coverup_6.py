# file mimesis/providers/cryptographic.py:119-135
# lines [119, 120, 130, 131, 133, 134, 135]
# branches ['130->131', '130->133']

import pytest
from mimesis.providers.cryptographic import Cryptographic

@pytest.fixture
def cryptographic_provider():
    return Cryptographic()

def test_mnemonic_phrase_with_custom_separator(cryptographic_provider):
    custom_separator = '-'
    phrase = cryptographic_provider.mnemonic_phrase(separator=custom_separator)
    assert custom_separator in phrase
    assert len(phrase.split(custom_separator)) == 12

def test_mnemonic_phrase_with_default_separator(cryptographic_provider):
    phrase = cryptographic_provider.mnemonic_phrase()
    assert ' ' in phrase
    assert len(phrase.split(' ')) == 12

def test_mnemonic_phrase_with_length(cryptographic_provider):
    custom_length = 6
    phrase = cryptographic_provider.mnemonic_phrase(length=custom_length)
    assert len(phrase.split(' ')) == custom_length
