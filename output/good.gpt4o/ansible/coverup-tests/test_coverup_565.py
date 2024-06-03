# file lib/ansible/utils/_junit_xml.py:49-55
# lines [49, 50, 51, 52, 53, 55]
# branches []

import pytest
from ansible.utils._junit_xml import TestFailure

def test_test_failure_tag():
    failure = TestFailure()
    assert failure.tag == 'failure'
