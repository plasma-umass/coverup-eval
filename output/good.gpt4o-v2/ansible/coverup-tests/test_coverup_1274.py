# file: lib/ansible/module_utils/common/text/converters.py:150-238
# asked: {"lines": [208], "branches": [[207, 208]]}
# gained: {"lines": [208], "branches": [[207, 208]]}

import pytest
from ansible.module_utils.common.text.converters import to_text
from ansible.module_utils.six import binary_type, text_type

def test_to_text_with_surrogate_or_strict():
    # Test when errors is 'surrogate_or_strict' and obj is binary_type
    obj = b'test'
    result = to_text(obj, errors='surrogate_or_strict')
    assert result == 'test'

def test_to_text_with_surrogate_or_strict_non_binary():
    # Test when errors is 'surrogate_or_strict' and obj is not binary_type
    obj = 123
    result = to_text(obj, errors='surrogate_or_strict')
    assert result == '123'

def test_to_text_with_surrogate_or_strict_nonstring_strict():
    # Test when errors is 'surrogate_or_strict' and nonstring is 'strict'
    obj = 123
    with pytest.raises(TypeError):
        to_text(obj, errors='surrogate_or_strict', nonstring='strict')

def test_to_text_with_surrogate_or_strict_no_surrogateescape(monkeypatch):
    # Test when errors is 'surrogate_or_strict' and HAS_SURROGATEESCAPE is False
    monkeypatch.setattr('ansible.module_utils.common.text.converters.HAS_SURROGATEESCAPE', False)
    obj = b'test'
    result = to_text(obj, errors='surrogate_or_strict')
    assert result == 'test'
