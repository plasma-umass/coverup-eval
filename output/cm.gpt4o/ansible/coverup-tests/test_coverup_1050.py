# file lib/ansible/module_utils/common/text/converters.py:33-147
# lines [106, 107, 109, 115, 116, 121, 122, 123, 124, 129, 130, 131, 132, 133, 134, 136, 139, 141, 142, 143, 145, 147]
# branches ['104->106', '106->107', '106->109', '116->121', '116->124', '128->129', '137->139', '139->141', '139->142', '142->143', '142->145']

import pytest
from ansible.module_utils.common.text.converters import to_bytes

def test_to_bytes_surrogate_or_strict(mocker):
    mocker.patch('ansible.module_utils.common.text.converters.HAS_SURROGATEESCAPE', False)
    result = to_bytes('test', errors='surrogate_or_strict')
    assert result == b'test'

def test_to_bytes_surrogate_or_replace(mocker):
    mocker.patch('ansible.module_utils.common.text.converters.HAS_SURROGATEESCAPE', False)
    result = to_bytes('test', errors='surrogate_or_replace')
    assert result == b'test'

def test_to_bytes_unicode_encode_error(mocker):
    mocker.patch('ansible.module_utils.common.text.converters.HAS_SURROGATEESCAPE', True)
    with pytest.raises(UnicodeEncodeError):
        to_bytes('test\uDC80', encoding='ascii', errors='strict')

def test_to_bytes_nonstring_simplerepr():
    class CustomObject:
        def __str__(self):
            raise UnicodeError

        def __repr__(self):
            raise UnicodeError

    result = to_bytes(CustomObject(), nonstring='simplerepr')
    assert result == b''

def test_to_bytes_nonstring_passthru():
    obj = object()
    result = to_bytes(obj, nonstring='passthru')
    assert result is obj

def test_to_bytes_nonstring_empty():
    result = to_bytes(object(), nonstring='empty')
    assert result == b''

def test_to_bytes_nonstring_strict():
    with pytest.raises(TypeError, match='obj must be a string type'):
        to_bytes(object(), nonstring='strict')

def test_to_bytes_nonstring_invalid():
    with pytest.raises(TypeError, match="Invalid value invalid for to_bytes' nonstring parameter"):
        to_bytes(object(), nonstring='invalid')
