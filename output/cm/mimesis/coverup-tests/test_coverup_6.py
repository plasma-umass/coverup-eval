# file mimesis/providers/cryptographic.py:33-52
# lines [33, 34, 47, 49, 50, 52]
# branches ['49->50', '49->52']

import pytest
from mimesis.providers.cryptographic import Cryptographic
from uuid import UUID

def test_cryptographic_uuid():
    # Test with as_object=False, should return a string
    result_str = Cryptographic.uuid()
    assert isinstance(result_str, str)
    assert UUID(result_str)  # This should be a valid UUID string

    # Test with as_object=True, should return a UUID object
    result_uuid = Cryptographic.uuid(as_object=True)
    assert isinstance(result_uuid, UUID)
