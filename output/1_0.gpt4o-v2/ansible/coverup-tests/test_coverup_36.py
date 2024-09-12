# file: lib/ansible/module_utils/common/warnings.py:38-40
# asked: {"lines": [38, 40], "branches": []}
# gained: {"lines": [38, 40], "branches": []}

import pytest
from ansible.module_utils.common import warnings

def test_get_deprecation_messages(monkeypatch):
    # Ensure _global_deprecations is empty before the test
    monkeypatch.setattr(warnings, '_global_deprecations', [])

    # Test when _global_deprecations is empty
    assert warnings.get_deprecation_messages() == ()

    # Add a deprecation message and test again
    warnings._global_deprecations.append('Deprecation warning 1')
    assert warnings.get_deprecation_messages() == ('Deprecation warning 1',)

    # Clean up after the test
    warnings._global_deprecations.clear()
