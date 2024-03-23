# file lib/ansible/module_utils/pycompat24.py:35-47
# lines [35, 47]
# branches []

import sys
import pytest

# Assuming the module is named pycompat24.py and is located in the lib/ansible/module_utils/ directory
from ansible.module_utils import pycompat24

def test_get_exception():
    try:
        raise ValueError("An error occurred")
    except Exception:
        e = pycompat24.get_exception()
        assert e.args[0] == "An error occurred"
    else:
        pytest.fail("ValueError was not raised")

# Ensure that the test does not affect other tests by modifying global state
def test_get_exception_cleanup(mocker):
    # Mock sys.exc_info to return a specific exception
    mock_exc_info = mocker.patch('sys.exc_info', return_value=(None, ValueError("Mocked error"), None))
    try:
        raise ValueError("An error occurred")
    except Exception:
        e = pycompat24.get_exception()
        assert e.args[0] == "Mocked error"
    else:
        pytest.fail("ValueError was not raised")
    # Verify that sys.exc_info was called
    mock_exc_info.assert_called_once()
