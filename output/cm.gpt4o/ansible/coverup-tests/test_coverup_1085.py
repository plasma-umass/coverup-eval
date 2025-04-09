# file lib/ansible/module_utils/common/text/converters.py:150-238
# lines [207, 208, 210, 223, 224, 225, 226, 228, 231, 232, 233, 234, 236]
# branches ['205->207', '207->208', '207->210', '229->231', '231->232', '231->233', '233->234', '233->236']

import pytest
from ansible.module_utils.common.text.converters import to_text

def test_to_text_surrogate_or_strict(mocker):
    mocker.patch('ansible.module_utils.common.text.converters.HAS_SURROGATEESCAPE', False)
    assert to_text(b'hello', errors='surrogate_or_strict') == 'hello'

def test_to_text_surrogate_or_replace(mocker):
    mocker.patch('ansible.module_utils.common.text.converters.HAS_SURROGATEESCAPE', False)
    assert to_text(b'hello', errors='surrogate_or_replace') == 'hello'

def test_to_text_nonstring_simplerepr_unicode_error(mocker):
    class UnicodeErrorObject:
        def __str__(self):
            raise UnicodeError()
        def __repr__(self):
            raise UnicodeError()
    assert to_text(UnicodeErrorObject(), nonstring='simplerepr') == ''

def test_to_text_nonstring_passthru():
    obj = 12345
    assert to_text(obj, nonstring='passthru') == obj

def test_to_text_nonstring_empty():
    assert to_text(12345, nonstring='empty') == ''

def test_to_text_nonstring_strict():
    with pytest.raises(TypeError, match='obj must be a string type'):
        to_text(12345, nonstring='strict')

def test_to_text_nonstring_invalid():
    with pytest.raises(TypeError, match="Invalid value invalid for to_text's nonstring parameter"):
        to_text(12345, nonstring='invalid')
