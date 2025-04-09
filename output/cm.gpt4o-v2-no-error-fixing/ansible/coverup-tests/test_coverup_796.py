# file: lib/ansible/utils/_junit_xml.py:99-107
# asked: {"lines": [101, 102, 103, 104, 105, 106], "branches": []}
# gained: {"lines": [101, 102, 103, 104, 105, 106], "branches": []}

import pytest
import decimal
from ansible.utils._junit_xml import TestCase

def test_get_attributes():
    test_case = TestCase(
        name="test_name",
        assertions=5,
        classname="test_class",
        status="success",
        time=decimal.Decimal("1.23")
    )
    
    attributes = test_case.get_attributes()
    
    assert attributes == {
        "assertions": "5",
        "classname": "test_class",
        "name": "test_name",
        "status": "success",
        "time": "1.23"
    }

    # Clean up
    del test_case
    del attributes
