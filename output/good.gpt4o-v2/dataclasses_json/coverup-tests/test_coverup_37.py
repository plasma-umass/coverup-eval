# file: dataclasses_json/mm.py:178-180
# asked: {"lines": [180], "branches": []}
# gained: {"lines": [180], "branches": []}

import pytest
from dataclasses_json.mm import SchemaF

class TestSchemaF:
    def test_dumps(self, mocker):
        # Mock the __init__ method to bypass the NotImplementedError
        mocker.patch.object(SchemaF, '__init__', lambda x: None)
        
        schema = SchemaF()
        obj = []  # Using an empty list to match the typing.List[A] overload
        result = schema.dumps(obj)
        assert result is None  # Since the method is not implemented, it should return None
