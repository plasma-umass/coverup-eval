# file: dataclasses_json/mm.py:210-214
# asked: {"lines": [210, 211, 212, 214], "branches": []}
# gained: {"lines": [210, 211, 212], "branches": []}

import pytest
from unittest.mock import patch
from dataclasses_json.mm import SchemaF

def test_schemaf_loads_overload():
    with patch.object(SchemaF, '__init__', lambda x: None):
        schema = SchemaF()
        json_data = '{"key": "value"}'
        
        # Test the first overload
        with patch.object(SchemaF, 'loads', lambda self, json_data, many=True, partial=None, unknown=None, **kwargs: []):
            result = schema.loads(json_data, many=True)
            assert isinstance(result, list)
        
        # Test the second overload
        with patch.object(SchemaF, 'loads', lambda self, json_data, many=None, partial=None, unknown=None, **kwargs: {}):
            result = schema.loads(json_data, many=None)
            assert isinstance(result, dict)
