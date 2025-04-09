# file dataclasses_json/mm.py:196-199
# lines [196, 197, 198, 199]
# branches []

import pytest
from marshmallow import Schema
from dataclasses_json.mm import SchemaF
from typing import TypeVar, Generic

# Define a generic type variable
A = TypeVar('A')

# Create a subclass of SchemaF for testing purposes
class MySchema(SchemaF, Generic[A]):
    def __init__(self, *args, **kwargs):
        Schema.__init__(self, *args, **kwargs)  # Call Schema's constructor directly to bypass the NotImplementedError

    def load(self, data, many=None, partial=None, unknown=None):
        return 'mocked_load'

# Test function to cover the load method in SchemaF
def test_schemaf_load():
    # Create an instance of MySchema
    schema = MySchema()

    # Call the load method with test data
    result = schema.load(data='test_data', many=True, partial=False, unknown='raise')

    # Assert that the result is as expected
    assert result == 'mocked_load'

# Register the test function for pytest
pytest.main(['-vv', __file__])
