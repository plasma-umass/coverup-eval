# file lib/ansible/utils/_junit_xml.py:58-64
# lines [58, 59, 60, 61, 62, 64]
# branches []

import pytest
from ansible.utils._junit_xml import TestError

def test_testerror_tag_property():
    test_error = TestError()
    assert test_error.tag == 'error'
