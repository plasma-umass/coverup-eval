# file string_utils/generation.py:21-38
# lines [21, 33, 35, 36, 38]
# branches ['35->36', '35->38']

import pytest
from string_utils.generation import uuid
from uuid import UUID

def test_uuid_default():
    result = uuid()
    assert isinstance(result, str)
    assert len(result) == 36
    assert '-' in result
    # Validate that the result is a valid UUID
    UUID(result)

def test_uuid_as_hex():
    result = uuid(as_hex=True)
    assert isinstance(result, str)
    assert len(result) == 32
    assert '-' not in result
    # Validate that the result is a valid hex representation of a UUID
    UUID(result, version=4)
