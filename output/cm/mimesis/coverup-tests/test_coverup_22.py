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

def test_hash_with_valid_algorithm(cryptographic_provider):
    # Test with a valid algorithm
    for algorithm in Algorithm:
        result = cryptographic_provider.hash(algorithm=algorithm)
        assert isinstance(result, str)
        assert len(result) > 0

def test_hash_with_invalid_algorithm(cryptographic_provider):
    # Test with an invalid algorithm
    with pytest.raises(NonEnumerableError):
        cryptographic_provider.hash(algorithm="invalid_algorithm")
