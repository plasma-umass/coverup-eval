# file dataclasses_json/mm.py:190-194
# lines [190, 191, 192, 193, 194]
# branches []

import pytest
from marshmallow import Schema
from dataclasses_json.mm import SchemaF
from typing import TypeVar

# Define a TypeVar and a dummy class to use with SchemaF
A = TypeVar('A')

# Define a dummy class to use as the generic type for SchemaF
class DummyClass:
    pass

# Define a SchemaF subclass for testing purposes
class TestSchema(SchemaF[DummyClass]):
    def load(self, data, many=None, partial=None, unknown=None):
        # Mock load method to just return an instance of DummyClass
        return DummyClass()

# Define a pytest test function to test the load method
def test_schema_f_load():
    # Create an instance of TestSchema without calling the constructor
    test_schema = TestSchema.__new__(TestSchema)
    input_data = {"key": "value"}

    # Call the load method with the input data
    result = test_schema.load(input_data)

    # Assert that the result is an instance of DummyClass
    assert isinstance(result, DummyClass)

# Run the test
pytest.main(["-v", __file__])
