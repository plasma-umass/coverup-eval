# file: lib/ansible/module_utils/common/warnings.py:33-35
# asked: {"lines": [33, 35], "branches": []}
# gained: {"lines": [33, 35], "branches": []}

import pytest
from ansible.module_utils.common import warnings

def test_get_warning_messages(monkeypatch):
    # Setup: Ensure _global_warnings has some warnings
    test_warnings = ["Warning 1", "Warning 2"]
    monkeypatch.setattr(warnings, "_global_warnings", test_warnings)

    # Call the function
    result = warnings.get_warning_messages()

    # Assertions
    assert result == tuple(test_warnings)

    # Cleanup is handled by monkeypatch, no state pollution
