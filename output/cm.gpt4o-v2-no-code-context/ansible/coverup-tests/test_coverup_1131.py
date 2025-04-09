# file: lib/ansible/module_utils/common/text/converters.py:33-147
# asked: {"lines": [106, 107, 109, 115, 116, 121, 122, 123, 124, 131, 132, 133, 134, 136, 139, 141, 142, 143, 145], "branches": [[104, 106], [106, 107], [106, 109], [116, 121], [116, 124], [137, 139], [139, 141], [139, 142], [142, 143], [142, 145]]}
# gained: {"lines": [106, 107, 109, 131, 132, 133, 134, 136, 139, 141, 142, 143, 145], "branches": [[104, 106], [106, 107], [106, 109], [137, 139], [139, 141], [139, 142], [142, 143], [142, 145]]}

import pytest
from ansible.module_utils.common.text.converters import to_bytes

def test_to_bytes_surrogate_or_strict(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.common.text.converters.HAS_SURROGATEESCAPE', False)
    result = to_bytes('test', errors='surrogate_or_strict')
    assert result == b'test'

def test_to_bytes_surrogate_or_replace(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.common.text.converters.HAS_SURROGATEESCAPE', False)
    result = to_bytes('test', errors='surrogate_or_replace')
    assert result == b'test'

def test_to_bytes_surrogate_then_replace():
    result = to_bytes('test\x80', errors='surrogate_then_replace')
    assert result == b'test\xc2\x80'

def test_to_bytes_nonstring_simplerepr():
    class CustomObject:
        def __str__(self):
            return 'custom_object'
    result = to_bytes(CustomObject(), nonstring='simplerepr')
    assert result == b'custom_object'

def test_to_bytes_nonstring_simplerepr_unicode_error():
    class CustomObject:
        def __str__(self):
            raise UnicodeError
        def __repr__(self):
            raise UnicodeError
    result = to_bytes(CustomObject(), nonstring='simplerepr')
    assert result == b''

def test_to_bytes_nonstring_passthru():
    obj = 12345
    result = to_bytes(obj, nonstring='passthru')
    assert result == obj

def test_to_bytes_nonstring_empty():
    result = to_bytes(12345, nonstring='empty')
    assert result == b''

def test_to_bytes_nonstring_strict():
    with pytest.raises(TypeError, match='obj must be a string type'):
        to_bytes(12345, nonstring='strict')

def test_to_bytes_nonstring_invalid():
    with pytest.raises(TypeError, match="Invalid value invalid for to_bytes' nonstring parameter"):
        to_bytes(12345, nonstring='invalid')
