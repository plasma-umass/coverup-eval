# file dataclasses_json/mm.py:318-369
# lines [322, 323, 324, 326, 327, 332, 333, 334, 336, 337, 338, 340, 342, 343, 349, 350, 351, 352, 353, 355, 356, 357, 359, 360, 361, 362, 363, 364, 365, 366, 367, 369]
# branches ['337->338', '337->340', '349->350', '349->355', '350->351', '350->357']

import pytest
import typing
from dataclasses import dataclass, field, fields as dc_fields
from dataclasses_json import dataclass_json
from marshmallow import Schema, post_load
from dataclasses_json.mm import build_schema

@dataclass_json
@dataclass
class TestClass:
    a: int
    b: str
    c: typing.Optional[int] = None

def _decode_dataclass(cls, kvs, partial):
    return cls(**kvs)

def _handle_undefined_parameters_safe(cls, kvs, usage):
    return {}

class _ExtendedEncoder:
    def __init__(self, *args, **kwargs):
        pass
    def encode(self, obj):
        import json
        return json.dumps(obj)

def schema(cls, mixin, infer_missing):
    return {}

@pytest.fixture
def mocker_fixture(mocker):
    mocker.patch('dataclasses_json.mm._decode_dataclass', side_effect=_decode_dataclass)
    mocker.patch('dataclasses_json.mm._handle_undefined_parameters_safe', side_effect=_handle_undefined_parameters_safe)
    mocker.patch('dataclasses_json.mm._ExtendedEncoder', _ExtendedEncoder)
    mocker.patch('dataclasses_json.mm.schema', side_effect=schema)
    yield
    mocker.stopall()

def test_build_schema(mocker_fixture):
    DataClassSchema = build_schema(TestClass, None, False, False)
    
    # Create an instance of the schema
    schema_instance = DataClassSchema()
    
    # Test the make_instance method
    obj = schema_instance.make_testclass({'a': 1, 'b': 'test'})
    assert isinstance(obj, TestClass)
    assert obj.a == 1
    assert obj.b == 'test'
    
    # Test the dumps method
    json_str = schema_instance.dumps(obj)
    assert json_str is not None
    
    # Test the dump method
    dumped = schema_instance.dump(obj)
    assert dumped['a'] == 1
    assert dumped['b'] == 'test'
    
    # Test the dump method with many=True
    dumped_many = schema_instance.dump([obj], many=True)
    assert isinstance(dumped_many, list)
    assert dumped_many[0]['a'] == 1
    assert dumped_many[0]['b'] == 'test'
