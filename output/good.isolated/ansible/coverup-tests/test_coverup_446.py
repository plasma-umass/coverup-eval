# file lib/ansible/module_utils/common/text/converters.py:262-267
# lines [262, 263, 264, 265, 266, 267]
# branches ['263->264', '263->265', '265->266', '265->267']

import datetime
import pytest
from ansible.module_utils.common.text.converters import _json_encode_fallback
from ansible.module_utils._text import to_native

def test_json_encode_fallback_with_set():
    test_set = {'a', 'b', 'c'}
    assert _json_encode_fallback(test_set) == ['a', 'b', 'c']

def test_json_encode_fallback_with_datetime():
    test_datetime = datetime.datetime(2023, 1, 1, 12, 0)
    assert _json_encode_fallback(test_datetime) == "2023-01-01T12:00:00"

def test_json_encode_fallback_with_unserializable_type():
    with pytest.raises(TypeError) as excinfo:
        _json_encode_fallback(object())
    assert "Cannot json serialize" in str(excinfo.value)
