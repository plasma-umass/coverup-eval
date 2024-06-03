# file lib/ansible/module_utils/pycompat24.py:35-47
# lines [35, 47]
# branches []

import sys
import pytest
from unittest import mock

# Assuming the function get_exception is imported from ansible.module_utils.pycompat24
from ansible.module_utils.pycompat24 import get_exception

def test_get_exception(mocker):
    # Mock sys.exc_info to return a specific exception
    mock_exc_info = (None, Exception("Test Exception"), None)
    mocker.patch('sys.exc_info', return_value=mock_exc_info)
    
    try:
        raise Exception("Test Exception")
    except Exception:
        e = get_exception()
        assert str(e) == "Test Exception"
