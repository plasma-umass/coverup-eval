# file: lib/ansible/utils/_junit_xml.py:49-55
# asked: {"lines": [49, 50, 51, 52, 53, 55], "branches": []}
# gained: {"lines": [49, 50, 51, 52, 53, 55], "branches": []}

import pytest
from ansible.utils._junit_xml import TestFailure

def test_testfailure_tag():
    # Create an instance of TestFailure
    test_failure = TestFailure()

    # Assert that the tag property returns 'failure'
    assert test_failure.tag == 'failure'
