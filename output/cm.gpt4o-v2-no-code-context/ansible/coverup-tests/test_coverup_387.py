# file: lib/ansible/module_utils/common/text/converters.py:262-267
# asked: {"lines": [262, 263, 264, 265, 266, 267], "branches": [[263, 264], [263, 265], [265, 266], [265, 267]]}
# gained: {"lines": [262, 263, 264, 265, 266, 267], "branches": [[263, 264], [263, 265], [265, 266], [265, 267]]}

import pytest
from ansible.module_utils.common.text.converters import _json_encode_fallback
from datetime import datetime
from collections.abc import Set

def test_json_encode_fallback_with_set():
    class CustomSet(Set):
        def __init__(self, *elements):
            self._elements = set(elements)
        
        def __contains__(self, element):
            return element in self._elements
        
        def __iter__(self):
            return iter(self._elements)
        
        def __len__(self):
            return len(self._elements)
    
    custom_set = CustomSet(1, 2, 3)
    result = _json_encode_fallback(custom_set)
    assert result == [1, 2, 3]

def test_json_encode_fallback_with_datetime():
    dt = datetime(2023, 10, 1, 12, 0, 0)
    result = _json_encode_fallback(dt)
    assert result == "2023-10-01T12:00:00"

def test_json_encode_fallback_with_unsupported_type():
    class UnsupportedType:
        pass
    
    with pytest.raises(TypeError, match="Cannot json serialize"):
        _json_encode_fallback(UnsupportedType())
