# file: dataclasses_json/mm.py:210-214
# asked: {"lines": [210, 211, 212, 214], "branches": []}
# gained: {"lines": [210, 211, 212], "branches": []}

import pytest
from unittest.mock import patch
from dataclasses_json.mm import SchemaF

class DummySchema(SchemaF):
    def loads(self, json_data, many=None, partial=None, unknown=None, **kwargs):
        return json_data

@pytest.fixture
def dummy_schema(monkeypatch):
    def mock_init(self, *args, **kwargs):
        pass
    monkeypatch.setattr(SchemaF, "__init__", mock_init)
    return DummySchema()

def test_schemaf_loads_overload(dummy_schema):
    json_data = '{"key": "value"}'
    result = dummy_schema.loads(json_data)
    assert result == json_data

def test_schemaf_loads_with_kwargs(dummy_schema):
    json_data = '{"key": "value"}'
    result = dummy_schema.loads(json_data, many=True, partial=True, unknown='EXCLUDE', custom_arg='test')
    assert result == json_data
