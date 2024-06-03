# file lib/ansible/module_utils/common/text/converters.py:262-267
# lines [262, 263, 264, 265, 266, 267]
# branches ['263->264', '263->265', '265->266', '265->267']

import pytest
import datetime
from ansible.module_utils.common.text.converters import _json_encode_fallback

def test_json_encode_fallback_set():
    test_set = {1, 2, 3}
    result = _json_encode_fallback(test_set)
    assert result == [1, 2, 3]

def test_json_encode_fallback_datetime():
    test_datetime = datetime.datetime(2023, 10, 1, 12, 0, 0)
    result = _json_encode_fallback(test_datetime)
    assert result == "2023-10-01T12:00:00"

def test_json_encode_fallback_type_error():
    class UnserializableObject:
        pass

    test_obj = UnserializableObject()
    with pytest.raises(TypeError, match="Cannot json serialize"):
        _json_encode_fallback(test_obj)
