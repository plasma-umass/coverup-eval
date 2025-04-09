# file dataclasses_json/mm.py:210-214
# lines [210, 211, 212, 214]
# branches []

import pytest
from unittest.mock import MagicMock
from marshmallow import Schema
from dataclasses_json.mm import SchemaF

def test_schemaf_loads_overload():
    class DummySchema(SchemaF[int]):
        def __init__(self, *args, **kwargs):
            pass

        def loads(self, json_data, many=None, partial=None, unknown=None, **kwargs):
            return 42

    schema = DummySchema()
    result = schema.loads('{"key": "value"}')
    assert result == 42

    # Clean up
    del DummySchema
    del schema
