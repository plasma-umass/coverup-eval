# file: lib/ansible/utils/_junit_xml.py:49-55
# asked: {"lines": [49, 50, 51, 52, 53, 55], "branches": []}
# gained: {"lines": [49, 50, 51, 52, 53, 55], "branches": []}

import pytest
from ansible.utils._junit_xml import TestFailure

def test_test_failure_tag():
    test_failure = TestFailure()
    assert test_failure.tag == 'failure'
