# file: lib/ansible/module_utils/urls.py:503-507
# asked: {"lines": [506, 507], "branches": []}
# gained: {"lines": [506, 507], "branches": []}

import pytest
from ansible.module_utils.urls import MissingModuleError

def test_missing_module_error_initialization():
    message = "Test message"
    import_traceback = "Traceback details"
    
    error = MissingModuleError(message, import_traceback)
    
    assert str(error) == message
    assert error.import_traceback == import_traceback
