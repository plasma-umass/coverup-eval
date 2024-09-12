# file: lib/ansible/module_utils/common/text/converters.py:33-147
# asked: {"lines": [106, 107, 109, 115, 116, 121, 122, 123, 124, 134, 136], "branches": [[104, 106], [106, 107], [106, 109], [116, 121], [116, 124]]}
# gained: {"lines": [134, 136], "branches": []}

import pytest
from ansible.module_utils.common.text.converters import to_bytes

def test_to_bytes_surrogate_or_strict():
    assert to_bytes('test', errors='surrogate_or_strict') == b'test'

def test_to_bytes_surrogate_then_replace():
    assert to_bytes('test\uDC80', errors='surrogate_then_replace') == b'test\x80'

def test_to_bytes_nonstring_simplerepr():
    class TestClass:
        def __str__(self):
            raise UnicodeError

        def __repr__(self):
            raise UnicodeError

    assert to_bytes(TestClass(), nonstring='simplerepr') == b''

def test_to_bytes_nonstring_empty():
    assert to_bytes(object(), nonstring='empty') == b''

def test_to_bytes_nonstring_passthru():
    obj = object()
    assert to_bytes(obj, nonstring='passthru') is obj

def test_to_bytes_nonstring_strict():
    with pytest.raises(TypeError, match='obj must be a string type'):
        to_bytes(object(), nonstring='strict')

def test_to_bytes_invalid_nonstring():
    with pytest.raises(TypeError, match="Invalid value invalid for to_bytes' nonstring parameter"):
        to_bytes(object(), nonstring='invalid')
