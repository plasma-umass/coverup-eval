# file lib/ansible/module_utils/common/warnings.py:14-18
# lines [14, 15, 16, 18]
# branches ['15->16', '15->18']

import pytest
from ansible.module_utils.common.warnings import warn, _global_warnings

def test_warn_with_string():
    test_warning = "This is a test warning"
    warn(test_warning)
    assert test_warning in _global_warnings
    _global_warnings.remove(test_warning)  # Clean up after the test

def test_warn_with_non_string():
    with pytest.raises(TypeError):
        warn(123)  # Pass a non-string type to trigger the TypeError
