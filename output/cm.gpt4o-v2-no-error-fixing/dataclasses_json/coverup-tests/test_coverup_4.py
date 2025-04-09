# file: dataclasses_json/mm.py:190-194
# asked: {"lines": [190, 191, 192, 193, 194], "branches": []}
# gained: {"lines": [190, 191, 192, 193], "branches": []}

import pytest
from unittest.mock import patch
from dataclasses_json.mm import SchemaF

def test_schemaf_load_overload():
    with pytest.raises(NotImplementedError):
        schema = SchemaF()
    
    # Test the overloads
    with patch.object(SchemaF, 'load', return_value=None) as mock_load:
        schema = SchemaF.__new__(SchemaF)
        
        # Test the first overload
        result = schema.load(data=[], many=True, partial=None, unknown=None)
        mock_load.assert_called_with(data=[], many=True, partial=None, unknown=None)
        assert result is None
        
        # Test the second overload
        result = schema.load(data={}, many=None, partial=None, unknown=None)
        mock_load.assert_called_with(data={}, many=None, partial=None, unknown=None)
        assert result is None
