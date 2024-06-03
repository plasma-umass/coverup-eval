# file dataclasses_json/mm.py:201-208
# lines [201, 202, 203, 208]
# branches []

import pytest
from unittest.mock import patch
from dataclasses_json.mm import SchemaF, Schema

class DummyClass:
    pass

def test_schemaf_loads():
    # Create a dummy schema class inheriting from SchemaF
    class DummySchema(SchemaF[DummyClass]):
        def loads(self, json_data, many=True, partial=None, unknown=None, **kwargs):
            return [DummyClass()]

    # Patch the __init__ method of SchemaF to prevent NotImplementedError
    with patch.object(SchemaF, '__init__', lambda self: None):
        schema = DummySchema()

        # Mock the input data
        json_data = '[{"key": "value"}]'

        # Call the loads method and assert the result
        result = schema.loads(json_data)
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], DummyClass)
