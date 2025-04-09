# file: string_utils/generation.py:21-38
# asked: {"lines": [21, 33, 35, 36, 38], "branches": [[35, 36], [35, 38]]}
# gained: {"lines": [21, 33, 35, 36, 38], "branches": [[35, 36], [35, 38]]}

import pytest
from string_utils.generation import uuid
from uuid import uuid4

def test_uuid_default(monkeypatch):
    # Mock uuid4 to return a known value
    mock_uuid = uuid4()
    monkeypatch.setattr('string_utils.generation.uuid4', lambda: mock_uuid)
    
    result = uuid()
    assert result == str(mock_uuid), f"Expected {str(mock_uuid)}, but got {result}"

def test_uuid_as_hex(monkeypatch):
    # Mock uuid4 to return a known value
    mock_uuid = uuid4()
    monkeypatch.setattr('string_utils.generation.uuid4', lambda: mock_uuid)
    
    result = uuid(as_hex=True)
    assert result == mock_uuid.hex, f"Expected {mock_uuid.hex}, but got {result}"
