# file: lib/ansible/utils/_junit_xml.py:58-64
# asked: {"lines": [58, 59, 60, 61, 62, 64], "branches": []}
# gained: {"lines": [58, 59, 60, 61, 62, 64], "branches": []}

import pytest
from ansible.utils._junit_xml import TestError, TestResult

def test_testerror_tag():
    # Create an instance of TestError
    test_error = TestError()

    # Assert that the tag property returns 'error'
    assert test_error.tag == 'error'
