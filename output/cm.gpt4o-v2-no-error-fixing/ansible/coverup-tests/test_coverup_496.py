# file: lib/ansible/utils/_junit_xml.py:89-92
# asked: {"lines": [89, 90, 92], "branches": []}
# gained: {"lines": [89, 90, 92], "branches": []}

import pytest
from ansible.utils._junit_xml import TestCase, TestError

def test_is_error():
    # Create a TestCase instance with errors
    error_instance = TestCase(name="test_with_error", errors=[TestError(message="Error message")])
    assert error_instance.is_error is True

    # Create a TestCase instance without errors
    no_error_instance = TestCase(name="test_without_error")
    assert no_error_instance.is_error is False
