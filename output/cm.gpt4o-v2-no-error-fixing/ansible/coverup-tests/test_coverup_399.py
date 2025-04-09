# file: lib/ansible/utils/_junit_xml.py:49-55
# asked: {"lines": [49, 50, 51, 52, 53, 55], "branches": []}
# gained: {"lines": [49, 50, 51, 52, 53, 55], "branches": []}

import dataclasses
import pytest
from ansible.utils._junit_xml import TestFailure, TestResult

def test_testfailure_tag():
    # Create an instance of TestFailure
    failure_instance = TestFailure()

    # Assert that the tag property returns 'failure'
    assert failure_instance.tag == 'failure'
