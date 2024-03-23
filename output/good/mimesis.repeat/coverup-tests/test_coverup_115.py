# file mimesis/providers/cryptographic.py:54-71
# lines [54, 67, 69, 70, 71]
# branches ['69->exit', '69->70']

import pytest
from mimesis.enums import Algorithm
from mimesis.exceptions import NonEnumerableError
from mimesis.providers.cryptographic import Cryptographic

@pytest.fixture
def cryptographic_provider():
    return Cryptographic()

def test_hash_with_supported_algorithm(cryptographic_provider):
    # Test with a supported algorithm
    supported_algorithm = Algorithm.MD5
    result = cryptographic_provider.hash(algorithm=supported_algorithm)
    assert len(result) == 32  # MD5 produces a 32-character hexadecimal number

def test_hash_with_unsupported_algorithm(cryptographic_provider):
    # Test with an unsupported algorithm
    with pytest.raises(NonEnumerableError):
        cryptographic_provider.hash(algorithm="unsupported_algorithm")

def test_hash_with_default_algorithm(cryptographic_provider):
    # Test with default algorithm (SHA256)
    result = cryptographic_provider.hash()
    # The default algorithm is not specified, so we cannot assume it's SHA256.
    # We should check that the result is a valid hexadecimal number instead.
    assert all(c in '0123456789abcdef' for c in result)
