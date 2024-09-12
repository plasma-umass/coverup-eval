# file: lib/ansible/utils/_junit_xml.py:99-107
# asked: {"lines": [101, 102, 103, 104, 105, 106], "branches": []}
# gained: {"lines": [101, 102, 103, 104, 105, 106], "branches": []}

import pytest
from ansible.utils._junit_xml import TestCase

@pytest.fixture
def test_case():
    return TestCase(
        assertions="assertion_value",
        classname="classname_value",
        name="name_value",
        status="status_value",
        time="time_value"
    )

def test_get_attributes(test_case):
    expected_attributes = {
        'assertions': 'assertion_value',
        'classname': 'classname_value',
        'name': 'name_value',
        'status': 'status_value',
        'time': 'time_value'
    }
    assert test_case.get_attributes() == expected_attributes
