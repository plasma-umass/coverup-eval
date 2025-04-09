# file: dataclasses_json/mm.py:318-369
# asked: {"lines": [], "branches": [[337, 340]]}
# gained: {"lines": [], "branches": [[337, 340]]}

import pytest
from unittest.mock import patch
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from dataclasses_json.mm import build_schema
from marshmallow import Schema

@dataclass_json
@dataclass
class TestClass:
    a: int
    b: str

def test_build_schema_dumps_with_cls():
    schema_cls = build_schema(TestClass, mixin=None, infer_missing=False, partial=False)
    instance = TestClass(a=1, b="test")
    
    # Mock the Schema.dumps method to ensure it is called with the correct arguments
    with patch.object(Schema, 'dumps', return_value='{"a": 1, "b": "test"}') as mock_dumps:
        result = schema_cls().dumps(instance)
        mock_dumps.assert_called_once()
        assert result == '{"a": 1, "b": "test"}'

def test_build_schema_dumps_without_cls():
    schema_cls = build_schema(TestClass, mixin=None, infer_missing=False, partial=False)
    instance = TestClass(a=1, b="test")
    
    # Mock the Schema.dumps method to ensure it is called with the correct arguments
    with patch.object(Schema, 'dumps', return_value='{"a": 1, "b": "test"}') as mock_dumps:
        result = schema_cls().dumps(instance, cls=None)
        mock_dumps.assert_called_once()
        assert result == '{"a": 1, "b": "test"}'

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Add any necessary cleanup code here

