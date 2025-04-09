# file: lib/ansible/utils/_junit_xml.py:99-107
# asked: {"lines": [99, 101, 102, 103, 104, 105, 106], "branches": []}
# gained: {"lines": [99, 101, 102, 103, 104, 105, 106], "branches": []}

import pytest
import decimal
from ansible.utils._junit_xml import TestCase

@pytest.fixture
def test_case():
    return TestCase(
        name="test_case",
        assertions=5,
        classname="TestClass",
        status="success",
        time=decimal.Decimal("1.23")
    )

def test_get_attributes(test_case):
    attributes = test_case.get_attributes()
    assert attributes == {
        "assertions": "5",
        "classname": "TestClass",
        "name": "test_case",
        "status": "success",
        "time": "1.23"
    }

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Perform any necessary cleanup here
