# file lib/ansible/utils/_junit_xml.py:128-141
# lines [128, 129, 130, 131, 132, 133, 134, 135, 137, 138, 139, 140]
# branches []

import pytest
from ansible.utils._junit_xml import TestSuite
import datetime

def test_test_suite_creation():
    # Create a TestSuite instance with all fields populated
    timestamp = datetime.datetime.now()
    test_suite = TestSuite(
        name="TestSuite1",
        hostname="localhost",
        id="1",
        package="test_package",
        timestamp=timestamp,
        properties={"key": "value"},
        cases=[],
        system_out="System output",
        system_err="System error"
    )

    # Assert that all fields are correctly set
    assert test_suite.name == "TestSuite1"
    assert test_suite.hostname == "localhost"
    assert test_suite.id == "1"
    assert test_suite.package == "test_package"
    assert test_suite.timestamp == timestamp
    assert test_suite.properties == {"key": "value"}
    assert test_suite.cases == []
    assert test_suite.system_out == "System output"
    assert test_suite.system_err == "System error"

def test_test_suite_defaults():
    # Create a TestSuite instance with default values
    test_suite = TestSuite(name="TestSuite2")

    # Assert that default fields are correctly set
    assert test_suite.name == "TestSuite2"
    assert test_suite.hostname is None
    assert test_suite.id is None
    assert test_suite.package is None
    assert test_suite.timestamp is None
    assert test_suite.properties == {}
    assert test_suite.cases == []
    assert test_suite.system_out is None
    assert test_suite.system_err is None
