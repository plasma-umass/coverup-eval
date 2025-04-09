# file mimesis/providers/cryptographic.py:54-71
# lines []
# branches ['69->exit']

import pytest
from mimesis.providers import Cryptographic
from mimesis.enums import Algorithm
from mimesis.exceptions import NonEnumerableError
import hashlib

def test_hash_with_valid_algorithm(mocker):
    crypto = Cryptographic()

    # Mock the uuid method to return a fixed value
    mocker.patch.object(crypto, 'uuid', return_value='test-uuid')

    # Test with a valid algorithm
    result = crypto.hash(Algorithm.SHA256)
    expected_hash = hashlib.sha256('test-uuid'.encode()).hexdigest()
    assert result == expected_hash

def test_hash_with_invalid_algorithm():
    crypto = Cryptographic()

    # Test with an invalid algorithm
    with pytest.raises(NonEnumerableError):
        crypto.hash('invalid_algorithm')

def test_hash_with_nonexistent_algorithm(mocker):
    crypto = Cryptographic()

    # Mock the uuid method to return a fixed value
    mocker.patch.object(crypto, 'uuid', return_value='test-uuid')

    # Mock the _validate_enum method to return a non-existent algorithm
    mocker.patch.object(crypto, '_validate_enum', return_value='nonexistent_algorithm')

    # Test with a non-existent algorithm
    result = crypto.hash(Algorithm.SHA256)
    assert result is None
