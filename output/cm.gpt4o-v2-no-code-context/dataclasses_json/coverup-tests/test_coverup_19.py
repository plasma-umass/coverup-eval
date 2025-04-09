# file: dataclasses_json/mm.py:155-159
# asked: {"lines": [155, 156, 159], "branches": []}
# gained: {"lines": [155, 156], "branches": []}

import pytest
from unittest.mock import MagicMock
from dataclasses_json.mm import SchemaF

class DummySchema(SchemaF):
    def dump(self, obj, many=None):
        if many is None:
            many = isinstance(obj, list)
        if many:
            return [self._dump_single(o) for o in obj]
        else:
            return self._dump_single(obj)
    
    def _dump_single(self, obj):
        return {"value": obj}

@pytest.fixture
def mock_schemaf_init(monkeypatch):
    def mock_init(self, *args, **kwargs):
        pass
    monkeypatch.setattr(SchemaF, "__init__", mock_init)

def test_schemaf_dump_list(mock_schemaf_init):
    schema = DummySchema()
    obj = [1, 2, 3]
    result = schema.dump(obj, many=True)
    assert isinstance(result, list)
    assert result == [{"value": 1}, {"value": 2}, {"value": 3}]

def test_schemaf_dump_single(mock_schemaf_init):
    schema = DummySchema()
    obj = 1
    result = schema.dump(obj, many=False)
    assert isinstance(result, dict)
    assert result == {"value": 1}

def test_schemaf_dump_default(mock_schemaf_init):
    schema = DummySchema()
    obj = [1, 2, 3]
    result = schema.dump(obj)
    assert isinstance(result, list)
    assert result == [{"value": 1}, {"value": 2}, {"value": 3}]
