# file lib/ansible/module_utils/urls.py:503-507
# lines [503, 504, 505, 506, 507]
# branches []

import pytest
from ansible.module_utils.urls import MissingModuleError

def test_missing_module_error():
    message = "This is a test message"
    import_traceback = "Traceback would be here"

    try:
        raise MissingModuleError(message, import_traceback)
    except MissingModuleError as e:
        assert e.args[0] == message
        assert e.import_traceback == import_traceback
