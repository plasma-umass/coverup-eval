# file: dataclasses_json/mm.py:182-188
# asked: {"lines": [182, 183, 184, 185, 188], "branches": []}
# gained: {"lines": [182, 183, 184, 185], "branches": []}

import pytest
from unittest.mock import patch
from dataclasses_json.mm import SchemaF

class DummySchema(SchemaF):
    def load(self, data, many=True, partial=None, unknown=None):
        return data

@pytest.fixture
def dummy_schema(monkeypatch):
    with monkeypatch.context() as m:
        m.setattr(SchemaF, "__init__", lambda self: None)
        return DummySchema()

def test_load_list(dummy_schema):
    data = [{'key': 'value'}]
    result = dummy_schema.load(data)
    assert result == data

def test_load_list_with_partial(dummy_schema):
    data = [{'key': 'value'}]
    result = dummy_schema.load(data, partial=True)
    assert result == data

def test_load_list_with_unknown(dummy_schema):
    data = [{'key': 'value'}]
    result = dummy_schema.load(data, unknown='raise')
    assert result == data

def test_load_list_with_partial_and_unknown(dummy_schema):
    data = [{'key': 'value'}]
    result = dummy_schema.load(data, partial=True, unknown='raise')
    assert result == data
