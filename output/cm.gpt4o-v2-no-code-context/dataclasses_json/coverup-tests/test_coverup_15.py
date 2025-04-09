# file: dataclasses_json/mm.py:190-194
# asked: {"lines": [190, 191, 192, 193, 194], "branches": []}
# gained: {"lines": [190, 191, 192, 193], "branches": []}

import pytest
from unittest.mock import patch
from dataclasses_json.mm import SchemaF

class DummySchema(SchemaF):
    def load(self, data, many=None, partial=None, unknown=None):
        return data

@pytest.fixture
def dummy_schema(monkeypatch):
    def mock_init(self, *args, **kwargs):
        pass
    monkeypatch.setattr(SchemaF, "__init__", mock_init)
    return DummySchema()

def test_load_with_overload(dummy_schema):
    data = {"key": "value"}
    result = dummy_schema.load(data)
    assert result == data

def test_load_with_many(dummy_schema):
    data = [{"key": "value1"}, {"key": "value2"}]
    result = dummy_schema.load(data, many=True)
    assert result == data

def test_load_with_partial(dummy_schema):
    data = {"key": "value"}
    result = dummy_schema.load(data, partial=True)
    assert result == data

def test_load_with_unknown(dummy_schema):
    data = {"key": "value"}
    result = dummy_schema.load(data, unknown="raise")
    assert result == data
