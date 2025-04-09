# file lib/ansible/utils/_junit_xml.py:49-55
# lines [49, 50, 51, 52, 53, 55]
# branches []

import pytest
from ansible.utils._junit_xml import TestFailure

def test_testfailure_tag_property():
    failure = TestFailure(message="Some failure message", output="Some output", type="SomeType")
    assert failure.tag == 'failure'
