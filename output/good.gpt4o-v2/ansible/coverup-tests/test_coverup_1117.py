# file: lib/ansible/module_utils/common/text/converters.py:33-147
# asked: {"lines": [106, 107, 109, 115, 116, 121, 122, 123, 124, 131, 132, 133, 134, 136, 139, 141, 142, 143, 145], "branches": [[104, 106], [106, 107], [106, 109], [116, 121], [116, 124], [137, 139], [139, 141], [139, 142], [142, 143], [142, 145]]}
# gained: {"lines": [131, 132, 133, 139, 141, 142, 143, 145], "branches": [[137, 139], [139, 141], [139, 142], [142, 143], [142, 145]]}

import pytest
from ansible.module_utils.common.text.converters import to_bytes
from ansible.module_utils.six import text_type

def test_to_bytes_surrogate_or_strict():
    assert to_bytes("test", errors='surrogate_or_strict') == b'test'

def test_to_bytes_surrogate_then_replace():
    assert to_bytes("test\uDC80", errors='surrogate_then_replace') == b'test\x80'

def test_to_bytes_nonstring_empty():
    assert to_bytes(123, nonstring='empty') == b''

def test_to_bytes_nonstring_passthru():
    assert to_bytes(123, nonstring='passthru') == 123

def test_to_bytes_nonstring_strict():
    with pytest.raises(TypeError, match='obj must be a string type'):
        to_bytes(123, nonstring='strict')

def test_to_bytes_nonstring_invalid():
    with pytest.raises(TypeError, match="Invalid value invalid for to_bytes' nonstring parameter"):
        to_bytes(123, nonstring='invalid')

def test_to_bytes_unicode_error_in_str():
    class UnicodeErrorInStr:
        def __str__(self):
            raise UnicodeError("str error")
        def __repr__(self):
            return "valid"
    assert to_bytes(UnicodeErrorInStr()) == b'valid'

def test_to_bytes_unicode_error_in_repr():
    class UnicodeErrorInRepr:
        def __str__(self):
            return "valid"
        def __repr__(self):
            raise UnicodeError("repr error")
    assert to_bytes(UnicodeErrorInRepr()) == b'valid'
