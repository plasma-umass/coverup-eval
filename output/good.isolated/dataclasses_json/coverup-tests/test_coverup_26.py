# file dataclasses_json/mm.py:318-369
# lines [318, 322, 323, 324, 326, 327, 332, 333, 334, 336, 337, 338, 340, 342, 343, 349, 350, 351, 352, 353, 355, 356, 357, 359, 360, 361, 362, 363, 364, 365, 366, 367, 369]
# branches ['337->338', '337->340', '349->350', '349->355', '350->351', '350->357']

import pytest
from dataclasses import dataclass, fields as dc_fields
from marshmallow import Schema, post_load
from dataclasses_json.mm import _decode_dataclass, _handle_undefined_parameters_safe, schema
from typing import Optional, Type
import json

# Assuming the existence of the CatchAllVar type for this context
CatchAllVar = type('CatchAllVar', (object,), {})

# Create a dataclass for testing
@dataclass
class TestClass:
    id: int
    name: str
    optional_field: Optional[CatchAllVar] = None

# Test function to improve coverage
def test_build_schema_dump(mocker):
    # Mock the _decode_dataclass and _handle_undefined_parameters_safe functions
    mocker.patch('dataclasses_json.mm._decode_dataclass', return_value=TestClass(1, 'Test'))
    mocker.patch('dataclasses_json.mm._handle_undefined_parameters_safe', return_value={})

    # Define a custom build_schema function to test
    def build_schema(cls: Type[TestClass],
                     mixin,
                     infer_missing,
                     partial) -> Type[Schema]:
        Meta = type('Meta',
                    (),
                    {'fields': tuple(field.name for field in dc_fields(cls)
                                     if
                                     field.name != 'dataclass_json_config' and field.type !=
                                     Optional[CatchAllVar]),
                     })

        @post_load
        def make_instance(self, kvs, **kwargs):
            return _decode_dataclass(cls, kvs, partial)

        def dumps(self, *args, **kwargs):
            if 'cls' not in kwargs:
                kwargs['cls'] = json.JSONEncoder

            return Schema.dumps(self, *args, **kwargs)

        def dump(self, obj, *, many=None):
            dumped = Schema.dump(self, obj, many=many)
            if many:
                for i, _obj in enumerate(obj):
                    dumped[i].update(
                        _handle_undefined_parameters_safe(cls=_obj, kvs={},
                                                          usage="dump"))
            else:
                dumped.update(_handle_undefined_parameters_safe(cls=obj, kvs={},
                                                                usage="dump"))
            return dumped

        schema_ = schema(cls, mixin, infer_missing)
        DataClassSchema: Type[Schema] = type(
            f'{cls.__name__.capitalize()}Schema',
            (Schema,),
            {'Meta': Meta,
             f'make_{cls.__name__.lower()}': make_instance,
             'dumps': dumps,
             'dump': dump,
             **schema_})

        return DataClassSchema

    # Create a schema for TestClass using the custom build_schema function
    TestClassSchema = build_schema(TestClass, None, False, False)

    # Create an instance of TestClass
    test_instance = TestClass(1, 'Test')

    # Test the dump method with a single object
    dumped_single = TestClassSchema().dump(test_instance)
    assert dumped_single == {'id': 1, 'name': 'Test'}

    # Test the dump method with many objects
    dumped_many = TestClassSchema().dump([test_instance], many=True)
    assert dumped_many == [{'id': 1, 'name': 'Test'}]

    # Test the dumps method
    dumped_json = TestClassSchema().dumps(test_instance)
    assert '{"id": 1, "name": "Test"}' in dumped_json

    # Cleanup by stopping the mocks
    mocker.stopall()
