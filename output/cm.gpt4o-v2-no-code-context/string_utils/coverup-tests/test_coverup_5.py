# file: string_utils/generation.py:21-38
# asked: {"lines": [21, 33, 35, 36, 38], "branches": [[35, 36], [35, 38]]}
# gained: {"lines": [21, 33, 35, 36, 38], "branches": [[35, 36], [35, 38]]}

import pytest
from string_utils.generation import uuid
from uuid import UUID

def test_uuid_default():
    result = uuid()
    assert isinstance(result, str)
    assert len(result) == 36
    assert UUID(result)  # This will raise an exception if the format is incorrect

def test_uuid_as_hex():
    result = uuid(as_hex=True)
    assert isinstance(result, str)
    assert len(result) == 32
    assert UUID(result)  # This will raise an exception if the format is incorrect

