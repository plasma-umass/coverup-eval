# file: dataclasses_json/mm.py:318-369
# asked: {"lines": [318, 322, 323, 324, 326, 327, 332, 333, 334, 336, 337, 338, 340, 342, 343, 349, 350, 351, 352, 353, 355, 356, 357, 359, 360, 361, 362, 363, 364, 365, 366, 367, 369], "branches": [[337, 338], [337, 340], [349, 350], [349, 355], [350, 351], [350, 357]]}
# gained: {"lines": [318, 322, 323, 324, 326, 327, 332, 333, 334, 336, 337, 338, 340, 342, 343, 349, 350, 351, 352, 353, 355, 356, 357, 359, 360, 361, 362, 363, 364, 365, 366, 367, 369], "branches": [[337, 338], [349, 350], [349, 355], [350, 351], [350, 357]]}

import pytest
import typing
from dataclasses import dataclass, fields as dc_fields
from marshmallow import Schema, post_load
from dataclasses_json.mm import build_schema

@dataclass
class TestClass:
    a: int
    b: str
    dataclass_json_config: typing.Optional[str] = None

def _decode_dataclass(cls, kvs, partial):
    return cls(**kvs)

def _handle_undefined_parameters_safe(cls, kvs, usage):
    return kvs

def schema(cls, mixin, infer_missing):
    return {}

class _ExtendedEncoder:
    def __init__(self, *args, **kwargs):
        pass
    def encode(self, obj):
        return str(obj)

@pytest.fixture
def mock_dependencies(monkeypatch):
    monkeypatch.setattr('dataclasses_json.mm._decode_dataclass', _decode_dataclass)
    monkeypatch.setattr('dataclasses_json.mm._handle_undefined_parameters_safe', _handle_undefined_parameters_safe)
    monkeypatch.setattr('dataclasses_json.mm.schema', schema)
    monkeypatch.setattr('dataclasses_json.mm._ExtendedEncoder', _ExtendedEncoder)

def test_build_schema(mock_dependencies):
    DataClassSchema = build_schema(TestClass, None, False, False)
    
    # Check if the schema class is created correctly
    assert hasattr(DataClassSchema, 'Meta')
    assert hasattr(DataClassSchema, 'make_testclass')
    assert hasattr(DataClassSchema, 'dumps')
    assert hasattr(DataClassSchema, 'dump')
    
    # Create an instance of the schema
    schema_instance = DataClassSchema()
    
    # Test make_instance method
    obj = schema_instance.make_testclass({'a': 1, 'b': 'test'})
    assert isinstance(obj, TestClass)
    assert obj.a == 1
    assert obj.b == 'test'
    
    # Test dumps method
    json_str = schema_instance.dumps(obj)
    assert isinstance(json_str, str)
    
    # Test dump method
    dumped = schema_instance.dump(obj)
    assert isinstance(dumped, dict)
    assert dumped['a'] == 1
    assert dumped['b'] == 'test'
    
    # Test dump method with many=True
    dumped_many = schema_instance.dump([obj], many=True)
    assert isinstance(dumped_many, list)
    assert len(dumped_many) == 1
    assert dumped_many[0]['a'] == 1
    assert dumped_many[0]['b'] == 'test'
