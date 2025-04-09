# file: lib/ansible/module_utils/common/text/converters.py:150-238
# asked: {"lines": [207, 208, 210], "branches": [[205, 207], [207, 208], [207, 210]]}
# gained: {"lines": [207, 208, 210], "branches": [[205, 207], [207, 208], [207, 210]]}

import pytest
from ansible.module_utils.common.text.converters import to_text
from ansible.module_utils.six import binary_type, text_type

def test_to_text_surrogate_or_strict():
    # Test when errors is 'surrogate_or_strict' and HAS_SURROGATEESCAPE is False
    obj = b'hello'
    encoding = 'utf-8'
    errors = 'surrogate_or_strict'
    nonstring = 'simplerepr'
    
    # Mock HAS_SURROGATEESCAPE to be False
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr('ansible.module_utils.common.text.converters.HAS_SURROGATEESCAPE', False)
        result = to_text(obj, encoding, errors, nonstring)
    
    assert result == 'hello'

def test_to_text_surrogate_or_replace():
    # Test when errors is 'surrogate_or_replace' and HAS_SURROGATEESCAPE is False
    obj = b'hello'
    encoding = 'utf-8'
    errors = 'surrogate_or_replace'
    nonstring = 'simplerepr'
    
    # Mock HAS_SURROGATEESCAPE to be False
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr('ansible.module_utils.common.text.converters.HAS_SURROGATEESCAPE', False)
        result = to_text(obj, encoding, errors, nonstring)
    
    assert result == 'hello'

def test_to_text_surrogate_then_replace():
    # Test when errors is 'surrogate_then_replace' and HAS_SURROGATEESCAPE is False
    obj = b'hello'
    encoding = 'utf-8'
    errors = 'surrogate_then_replace'
    nonstring = 'simplerepr'
    
    # Mock HAS_SURROGATEESCAPE to be False
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr('ansible.module_utils.common.text.converters.HAS_SURROGATEESCAPE', False)
        result = to_text(obj, encoding, errors, nonstring)
    
    assert result == 'hello'
