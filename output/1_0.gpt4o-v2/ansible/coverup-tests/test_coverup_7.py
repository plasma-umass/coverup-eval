# file: lib/ansible/module_utils/common/warnings.py:14-18
# asked: {"lines": [14, 15, 16, 18], "branches": [[15, 16], [15, 18]]}
# gained: {"lines": [14, 15, 16, 18], "branches": [[15, 16], [15, 18]]}

import pytest
from ansible.module_utils.common.warnings import warn, _global_warnings
from ansible.module_utils.six import string_types

def test_warn_with_string():
    # Ensure _global_warnings is empty before the test
    _global_warnings.clear()
    
    warning_message = "This is a warning"
    warn(warning_message)
    
    assert warning_message in _global_warnings

def test_warn_with_non_string():
    # Ensure _global_warnings is empty before the test
    _global_warnings.clear()
    
    with pytest.raises(TypeError) as excinfo:
        warn(12345)  # Passing a non-string type
    
    assert "warn requires a string not a" in str(excinfo.value)
