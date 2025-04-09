# file: lib/ansible/utils/_junit_xml.py:99-107
# asked: {"lines": [99, 101, 102, 103, 104, 105, 106], "branches": []}
# gained: {"lines": [99, 101, 102, 103, 104, 105, 106], "branches": []}

import pytest
from ansible.utils._junit_xml import TestCase

def test_get_attributes():
    test_case = TestCase(
        assertions="assertion_value",
        classname="classname_value",
        name="name_value",
        status="status_value",
        time="time_value"
    )
    
    attributes = test_case.get_attributes()
    
    assert attributes["assertions"] == "assertion_value"
    assert attributes["classname"] == "classname_value"
    assert attributes["name"] == "name_value"
    assert attributes["status"] == "status_value"
    assert attributes["time"] == "time_value"
