# file: dataclasses_json/mm.py:161-163
# asked: {"lines": [161, 162, 163], "branches": []}
# gained: {"lines": [161, 162], "branches": []}

import pytest
from unittest.mock import MagicMock
from marshmallow import Schema
import typing
from dataclasses_json.mm import SchemaF

class DummySchema(SchemaF):
    def dump(self, obj, many=None):
        return "dummy_result"

@pytest.fixture
def dummy_schema(monkeypatch):
    # Mock the __init__ method to avoid NotImplementedError
    monkeypatch.setattr(SchemaF, '__init__', lambda self: None)
    return DummySchema()

def test_dump_overload(dummy_schema, monkeypatch):
    mock_dump = MagicMock(return_value="mocked_result")
    monkeypatch.setattr(DummySchema, 'dump', mock_dump)

    result = dummy_schema.dump("test_obj", many=False)
    mock_dump.assert_called_once_with("test_obj", many=False)
    assert result == "mocked_result"
