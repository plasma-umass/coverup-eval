# file dataclasses_json/mm.py:155-159
# lines [155, 156, 159]
# branches []

import pytest
from unittest.mock import MagicMock
from dataclasses_json.mm import SchemaF

def test_schemaf_dump_overload():
    class DummySchema(SchemaF[int]):
        def __init__(self, *args, **kwargs):
            pass
        
        def dump(self, obj, many=None):
            if many:
                return [str(x) for x in obj]
            return str(obj)

    schema = DummySchema()
    
    # Test the overload with a list
    result = schema.dump([1, 2, 3], many=True)
    assert result == ['1', '2', '3']
    
    # Test the overload with a single object
    result = schema.dump(1, many=False)
    assert result == '1'
    
    # Test the overload with default many (None)
    result = schema.dump(1)
    assert result == '1'
