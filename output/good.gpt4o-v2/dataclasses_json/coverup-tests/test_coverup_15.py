# file: dataclasses_json/mm.py:182-188
# asked: {"lines": [182, 183, 184, 185, 188], "branches": []}
# gained: {"lines": [182, 183, 184, 185], "branches": []}

import pytest
from unittest.mock import patch
from dataclasses_json.mm import SchemaF

def test_schemaf_load_list_overload():
    with patch.object(SchemaF, '__init__', lambda x: None):
        schema = SchemaF()
        data = []  # Provide appropriate test data here
        try:
            result = schema.load(data, many=True, partial=None, unknown=None)
        except NotImplementedError:
            result = []
        assert result is None
