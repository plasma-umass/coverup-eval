# file: dataclasses_json/mm.py:318-369
# asked: {"lines": [318, 322, 323, 324, 326, 327, 332, 333, 334, 336, 337, 338, 340, 342, 343, 349, 350, 351, 352, 353, 355, 356, 357, 359, 360, 361, 362, 363, 364, 365, 366, 367, 369], "branches": [[337, 338], [337, 340], [349, 350], [349, 355], [350, 351], [350, 357]]}
# gained: {"lines": [318, 322, 323, 324, 326, 327, 332, 333, 334, 336, 337, 338, 340, 342, 343, 349, 350, 351, 352, 353, 355, 356, 357, 359, 360, 361, 362, 363, 364, 365, 366, 367, 369], "branches": [[337, 338], [349, 350], [349, 355], [350, 351], [350, 357]]}

import pytest
from unittest.mock import patch, MagicMock
from dataclasses import dataclass, field
from typing import Optional, Dict
from marshmallow import Schema
from dataclasses_json.mm import build_schema
from dataclasses_json.core import _ExtendedEncoder
from dataclasses_json.utils import CatchAllVar

@dataclass
class TestClass:
    a: int
    b: str
    dataclass_json_config: Optional[Dict] = field(default=None)
    catch_all: Optional[CatchAllVar] = field(default=None)

@pytest.fixture
def mock_schema():
    with patch('dataclasses_json.mm.schema', return_value={}) as mock:
        yield mock

def test_build_schema(mock_schema):
    TestSchema = build_schema(TestClass, mixin=None, infer_missing=True, partial=False)
    
    assert hasattr(TestSchema, 'Meta')
    assert hasattr(TestSchema.Meta, 'fields')
    assert 'a' in TestSchema.Meta.fields
    assert 'b' in TestSchema.Meta.fields
    assert 'dataclass_json_config' not in TestSchema.Meta.fields
    assert 'catch_all' not in TestSchema.Meta.fields

    assert hasattr(TestSchema, 'make_testclass')
    assert hasattr(TestSchema, 'dumps')
    assert hasattr(TestSchema, 'dump')

    instance = TestSchema()
    obj = TestClass(a=1, b='test')
    
    with patch('dataclasses_json.mm._decode_dataclass', return_value=obj) as mock_decode:
        result = instance.make_testclass({'a': 1, 'b': 'test'})
        assert result == obj
        mock_decode.assert_called_once_with(TestClass, {'a': 1, 'b': 'test'}, False)

    with patch('dataclasses_json.core._ExtendedEncoder', wraps=_ExtendedEncoder) as mock_encoder:
        result = instance.dumps(obj)
        assert isinstance(result, str)

    with patch('dataclasses_json.mm._handle_undefined_parameters_safe', return_value={}) as mock_handle:
        result = instance.dump(obj)
        assert isinstance(result, dict)
        mock_handle.assert_called_once_with(cls=obj, kvs={}, usage='dump')

        result = instance.dump([obj], many=True)
        assert isinstance(result, list)
        assert len(result) == 1
        mock_handle.assert_called_with(cls=obj, kvs={}, usage='dump')
