# file: lib/ansible/module_utils/pycompat24.py:35-47
# asked: {"lines": [35, 47], "branches": []}
# gained: {"lines": [35, 47], "branches": []}

import sys
import pytest

# Assuming the function get_exception is defined in a module named pycompat24
from ansible.module_utils.pycompat24 import get_exception

def test_get_exception(monkeypatch):
    class MockException(Exception):
        pass

    def mock_exc_info():
        return (None, MockException("test exception"), None)

    monkeypatch.setattr(sys, 'exc_info', mock_exc_info)

    try:
        raise MockException("test exception")
    except MockException:
        e = get_exception()
        assert isinstance(e, MockException)
        assert str(e) == "test exception"
