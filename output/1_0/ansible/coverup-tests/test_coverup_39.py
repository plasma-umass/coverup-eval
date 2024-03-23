# file lib/ansible/module_utils/common/warnings.py:38-40
# lines [38, 40]
# branches []

import pytest
from ansible.module_utils.common.warnings import get_deprecation_messages, _global_deprecations

# Test function to cover get_deprecation_messages
def test_get_deprecation_messages():
    # Setup: Add a mock deprecation message to the global deprecations list
    mock_deprecation = "This is a mock deprecation message."
    _global_deprecations.append(mock_deprecation)

    # Exercise: Call the function under test
    deprecation_messages = get_deprecation_messages()

    # Verify: Check if the returned deprecation messages match the expected result
    assert deprecation_messages == (mock_deprecation,), "The deprecation messages do not match the expected tuple."

    # Cleanup: Remove the mock deprecation message from the global deprecations list
    _global_deprecations.remove(mock_deprecation)
