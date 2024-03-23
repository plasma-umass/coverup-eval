# file lib/ansible/module_utils/common/warnings.py:33-35
# lines [33, 35]
# branches []

import pytest
from ansible.module_utils.common.warnings import get_warning_messages, warn

# Assuming that the _global_warnings list is not exposed directly,
# we will use the warn function to add warnings and then check if
# get_warning_messages returns them correctly.

def test_get_warning_messages(mocker):
    # Setup: clear the global warnings list before the test
    mocker.patch('ansible.module_utils.common.warnings._global_warnings', new=[])
    
    # Test: add some warnings
    warn("warning 1")
    warn("warning 2")
    
    # Verify: get_warning_messages should return the warnings we added
    warnings = get_warning_messages()
    assert warnings == ("warning 1", "warning 2"), "Warnings did not match expected values"
    
    # Cleanup: clear the global warnings list after the test
    # This is done automatically by the mocker.patch
