# file: lib/ansible/module_utils/common/text/converters.py:262-267
# asked: {"lines": [262, 263, 264, 265, 266, 267], "branches": [[263, 264], [263, 265], [265, 266], [265, 267]]}
# gained: {"lines": [262, 263, 264, 265, 266, 267], "branches": [[263, 264], [263, 265], [265, 266], [265, 267]]}

import pytest
import datetime
from ansible.module_utils.common.text.converters import _json_encode_fallback
from ansible.module_utils.common._collections_compat import Set

def test_json_encode_fallback_with_set(monkeypatch):
    class MockSet(Set):
        def __init__(self, iterable):
            self._data = set(iterable)
        
        def __iter__(self):
            return iter(self._data)
        
        def __len__(self):
            return len(self._data)
        
        def __contains__(self, item):
            return item in self._data

    monkeypatch.setattr("ansible.module_utils.common._collections_compat.Set", MockSet)
    test_set = MockSet([1, 2, 3])
    result = _json_encode_fallback(test_set)
    assert result == [1, 2, 3]

def test_json_encode_fallback_with_datetime():
    test_datetime = datetime.datetime(2023, 10, 1, 12, 0, 0)
    result = _json_encode_fallback(test_datetime)
    assert result == "2023-10-01T12:00:00"

def test_json_encode_fallback_with_unsupported_type():
    class UnsupportedType:
        pass

    test_obj = UnsupportedType()
    with pytest.raises(TypeError, match="Cannot json serialize"):
        _json_encode_fallback(test_obj)
