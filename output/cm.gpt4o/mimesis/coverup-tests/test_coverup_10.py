# file mimesis/providers/cryptographic.py:119-135
# lines [119, 120, 130, 131, 133, 134, 135]
# branches ['130->131', '130->133']

import pytest
from mimesis.providers.cryptographic import Cryptographic

@pytest.fixture
def cryptographic_provider():
    return Cryptographic()

def test_mnemonic_phrase_default_separator(cryptographic_provider):
    phrase = cryptographic_provider.mnemonic_phrase()
    assert isinstance(phrase, str)
    assert len(phrase.split(' ')) == 12

def test_mnemonic_phrase_custom_separator(cryptographic_provider):
    separator = '-'
    phrase = cryptographic_provider.mnemonic_phrase(separator=separator)
    assert isinstance(phrase, str)
    assert len(phrase.split(separator)) == 12

def test_mnemonic_phrase_custom_length(cryptographic_provider):
    length = 15
    phrase = cryptographic_provider.mnemonic_phrase(length=length)
    assert isinstance(phrase, str)
    assert len(phrase.split(' ')) == length

def test_mnemonic_phrase_custom_length_and_separator(cryptographic_provider):
    length = 8
    separator = '|'
    phrase = cryptographic_provider.mnemonic_phrase(length=length, separator=separator)
    assert isinstance(phrase, str)
    assert len(phrase.split(separator)) == length
