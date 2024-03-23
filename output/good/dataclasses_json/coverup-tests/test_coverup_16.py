# file dataclasses_json/mm.py:143-145
# lines [143, 144]
# branches []

import pytest
from dataclasses_json.mm import SchemaF
from marshmallow import fields, post_load, Schema
from typing import TypeVar, Generic

# Define a type variable and a dummy dataclass for testing
T = TypeVar('T')

class DummyDataClass(Generic[T]):
    def __init__(self, value: T):
        self.value = value

# Define a Schema subclass for DummyDataClass
class DummySchema(Schema):
    value = fields.Field()

    @post_load
    def make_dummy_dataclass(self, data, **kwargs):
        return DummyDataClass(**data)

# Test function to cover the SchemaF class
def test_schemaf_generic():
    # Create an instance of the schema
    schema = DummySchema()

    # Serialize a DummyDataClass instance
    dummy_instance = DummyDataClass(value='test_value')
    serialized = schema.dump(dummy_instance)

    # Deserialize the serialized data
    deserialized = schema.load(serialized)

    # Assertions to verify postconditions
    assert serialized == {'value': 'test_value'}
    assert isinstance(deserialized, DummyDataClass)
    assert deserialized.value == 'test_value'

# Run the test
def test_schemaf():
    test_schemaf_generic()
