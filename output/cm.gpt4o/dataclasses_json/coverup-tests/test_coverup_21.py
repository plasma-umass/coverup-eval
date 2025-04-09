# file dataclasses_json/mm.py:196-199
# lines [196, 197, 198, 199]
# branches []

import pytest
from unittest.mock import patch
from dataclasses_json.mm import SchemaF

def test_schemaf_load():
    class DummySchema(SchemaF):
        def __init__(self, *args, **kwargs):
            pass

        def load(self, data, many=None, partial=None, unknown=None):
            return "loaded_data"

    dummy_schema = DummySchema()

    with patch.object(DummySchema, 'load', return_value="loaded_data") as mock_load:
        result = dummy_schema.load(data="test_data", many=True, partial=True, unknown="raise")
        mock_load.assert_called_once_with(data="test_data", many=True, partial=True, unknown="raise")
        assert result == "loaded_data"
