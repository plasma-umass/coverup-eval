# file: dataclasses_json/mm.py:318-369
# asked: {"lines": [], "branches": [[337, 340]]}
# gained: {"lines": [], "branches": [[337, 340]]}

import pytest
from marshmallow import Schema
from dataclasses import dataclass
from dataclasses_json.mm import build_schema
from dataclasses_json.core import _ExtendedEncoder

@dataclass
class TestClass:
    field1: int
    field2: str

def test_dumps_with_cls():
    schema_cls = build_schema(TestClass, mixin=None, infer_missing=False, partial=False)
    schema_instance = schema_cls()
    
    # Test the dumps method to ensure the 'cls' key is added to kwargs
    data = TestClass(field1=1, field2="test")
    json_data = schema_instance.dumps(data, cls=_ExtendedEncoder)
    
    assert '"field1": 1' in json_data
    assert '"field2": "test"' in json_data

def test_dumps_without_cls():
    schema_cls = build_schema(TestClass, mixin=None, infer_missing=False, partial=False)
    schema_instance = schema_cls()
    
    # Test the dumps method without providing 'cls' in kwargs
    data = TestClass(field1=1, field2="test")
    json_data = schema_instance.dumps(data)
    
    assert '"field1": 1' in json_data
    assert '"field2": "test"' in json_data

@pytest.fixture
def mock_schema_dump(mocker):
    return mocker.patch.object(Schema, 'dumps', return_value='{"field1": 1, "field2": "test"}')

def test_dumps_with_mock(mock_schema_dump):
    schema_cls = build_schema(TestClass, mixin=None, infer_missing=False, partial=False)
    schema_instance = schema_cls()
    
    data = TestClass(field1=1, field2="test")
    json_data = schema_instance.dumps(data)
    
    mock_schema_dump.assert_called_once()
    assert json_data == '{"field1": 1, "field2": "test"}'
