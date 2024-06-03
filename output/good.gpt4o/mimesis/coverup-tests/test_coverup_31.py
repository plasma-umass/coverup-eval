# file mimesis/providers/cryptographic.py:54-71
# lines [54, 67, 69, 70, 71]
# branches ['69->exit', '69->70']

import pytest
from mimesis.providers.cryptographic import Cryptographic
from mimesis.enums import Algorithm
from mimesis.exceptions import NonEnumerableError
import hashlib

def test_hash_with_valid_algorithm():
    crypto = Cryptographic()
    hash_value = crypto.hash(Algorithm.SHA256)
    assert isinstance(hash_value, str)
    assert len(hash_value) == 64  # SHA256 produces a 64-character hex string

def test_hash_with_invalid_algorithm():
    crypto = Cryptographic()
    with pytest.raises(NonEnumerableError):
        crypto.hash("INVALID_ALGORITHM")

def test_hash_with_default_algorithm():
    crypto = Cryptographic()
    hash_value = crypto.hash()
    assert isinstance(hash_value, str)
    # Default algorithm is not specified, so we can't assert the length

@pytest.fixture
def mock_uuid(mocker):
    return mocker.patch('mimesis.providers.cryptographic.Cryptographic.uuid', return_value='12345678-1234-5678-1234-567812345678')

def test_hash_with_mocked_uuid(mock_uuid):
    crypto = Cryptographic()
    hash_value = crypto.hash(Algorithm.SHA256)
    assert hash_value == hashlib.sha256(mock_uuid().encode()).hexdigest()
