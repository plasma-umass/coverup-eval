# file lib/ansible/module_utils/urls.py:503-507
# lines [503, 504, 505, 506, 507]
# branches []

import pytest
from ansible.module_utils.urls import MissingModuleError

def test_missing_module_error():
    message = "Failed to import module"
    import_traceback = "Traceback (most recent call last):\n..."

    # Create an instance of MissingModuleError
    error = MissingModuleError(message, import_traceback)

    # Verify that the message is set correctly
    assert str(error) == message

    # Verify that the import_traceback is set correctly
    assert error.import_traceback == import_traceback
