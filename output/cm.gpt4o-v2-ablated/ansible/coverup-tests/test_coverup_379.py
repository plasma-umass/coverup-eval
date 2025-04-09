# file: lib/ansible/module_utils/pycompat24.py:35-47
# asked: {"lines": [35, 47], "branches": []}
# gained: {"lines": [35, 47], "branches": []}

import sys
import pytest

from ansible.module_utils.pycompat24 import get_exception

def test_get_exception_no_exception():
    # Test when no exception is raised
    assert get_exception() is None

def test_get_exception_with_exception():
    # Test when an exception is raised
    try:
        raise ValueError("Test exception")
    except ValueError:
        e = get_exception()
        assert isinstance(e, ValueError)
        assert str(e) == "Test exception"
