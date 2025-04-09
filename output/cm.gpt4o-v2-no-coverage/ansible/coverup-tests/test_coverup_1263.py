# file: lib/ansible/utils/_junit_xml.py:172-186
# asked: {"lines": [174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185], "branches": []}
# gained: {"lines": [174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185], "branches": []}

import pytest
import datetime
import decimal
from ansible.utils._junit_xml import TestSuite

@pytest.fixture
def test_suite():
    return TestSuite(
        name="example",
        hostname="localhost",
        id="1",
        package="example_package",
        timestamp=datetime.datetime(2023, 10, 1, 12, 0, 0),
        properties={"key": "value"},
        cases=[],
        system_out="output",
        system_err="error"
    )

def test_get_attributes(test_suite):
    attributes = test_suite.get_attributes()
    assert attributes == {
        "disabled": str(test_suite.disabled),
        "errors": str(test_suite.errors),
        "failures": str(test_suite.failures),
        "hostname": "localhost",
        "id": "1",
        "name": "example",
        "package": "example_package",
        "skipped": str(test_suite.skipped),
        "tests": str(test_suite.tests),
        "time": str(test_suite.time),
        "timestamp": "2023-10-01T12:00:00"
    }

def test_get_attributes_no_timestamp(monkeypatch, test_suite):
    monkeypatch.setattr(test_suite, "timestamp", None)
    attributes = test_suite.get_attributes()
    assert "timestamp" not in attributes
