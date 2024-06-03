# file dataclasses_json/mm.py:196-199
# lines [199]
# branches []

import pytest
from dataclasses_json.mm import SchemaF
from marshmallow import Schema

class DummySchema(Schema):
    pass

class TestSchemaF(SchemaF[DummySchema]):
    def __init__(self, *args, **kwargs):
        pass

    def load(self, data, many=None, partial=None, unknown=None):
        return super().load(data, many=many, partial=partial, unknown=unknown)

def test_schemaf_load():
    schema = TestSchemaF()
    data = {"key": "value"}
    
    # Call the load method to ensure line 199 is executed
    result = schema.load(data)
    
    # Assert that the result is None since the method is a pass-through
    assert result is None
