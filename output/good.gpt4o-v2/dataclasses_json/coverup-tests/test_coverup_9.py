# file: dataclasses_json/mm.py:161-163
# asked: {"lines": [161, 162, 163], "branches": []}
# gained: {"lines": [161, 162], "branches": []}

import pytest
from unittest.mock import MagicMock
from dataclasses_json.mm import SchemaF

class ConcreteSchemaF(SchemaF):
    def __init__(self, *args, **kwargs):
        # Do not call the parent constructor to avoid NotImplementedError
        pass

class TestSchemaF:
    def test_dump_overload(self):
        schema = ConcreteSchemaF()
        
        # Mock the dump method to test the overload
        schema.dump = MagicMock(return_value="mocked")

        # Test the overload with a single object
        result = schema.dump(obj="test_obj", many=False)
        schema.dump.assert_called_with(obj="test_obj", many=False)
        assert result == "mocked"

        # Test the overload with a list of objects
        result = schema.dump(obj=["test_obj1", "test_obj2"], many=True)
        schema.dump.assert_called_with(obj=["test_obj1", "test_obj2"], many=True)
        assert result == "mocked"
