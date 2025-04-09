# file mimesis/providers/cryptographic.py:33-52
# lines [33, 34, 47, 49, 50, 52]
# branches ['49->50', '49->52']

import pytest
from mimesis.providers.cryptographic import Cryptographic
from uuid import UUID

def test_uuid_as_object():
    # Test when as_object is True
    result = Cryptographic.uuid(as_object=True)
    assert isinstance(result, UUID), "Expected result to be an instance of UUID"

def test_uuid_as_string():
    # Test when as_object is False
    result = Cryptographic.uuid(as_object=False)
    assert isinstance(result, str), "Expected result to be a string"
    # Ensure the string can be converted back to a UUID
    assert isinstance(UUID(result), UUID), "Expected result to be convertible to a UUID"
