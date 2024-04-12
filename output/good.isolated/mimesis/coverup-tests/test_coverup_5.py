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
    assert custom_separator.join(phrase.split(custom_separator)) == phrase

def test_mnemonic_phrase_with_default_separator(cryptographic_provider):
    phrase = cryptographic_provider.mnemonic_phrase()
    assert ' '.join(phrase.split(' ')) == phrase

def test_mnemonic_phrase_with_length(cryptographic_provider):
    length = 5
    phrase = cryptographic_provider.mnemonic_phrase(length=length)
    assert len(phrase.split(' ')) == length
