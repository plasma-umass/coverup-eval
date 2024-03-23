# file mimesis/providers/cryptographic.py:33-52
# lines [33, 34, 47, 49, 50, 52]
# branches ['49->50', '49->52']

import pytest
from mimesis.providers.cryptographic import Cryptographic
from uuid import UUID

def test_cryptographic_uuid_as_str():
    # Test the uuid method with default as_object=False
    result = Cryptographic.uuid()
    assert isinstance(result, str)
    assert UUID(result).version == 4

def test_cryptographic_uuid_as_object():
    # Test the uuid method with as_object=True
    result = Cryptographic.uuid(as_object=True)
    assert isinstance(result, UUID)
    assert result.version == 4
