# file lib/ansible/utils/_junit_xml.py:128-141
# lines [128, 129, 130, 131, 132, 133, 134, 135, 137, 138, 139, 140]
# branches []

import pytest
import datetime
from ansible.utils._junit_xml import TestSuite, TestCase

def test_testsuite_initialization():
    # Create a TestSuite instance with all fields populated
    timestamp = datetime.datetime.now()
    properties = {"key1": "value1", "key2": "value2"}
    cases = [TestCase(name="test_case_1"), TestCase(name="test_case_2")]
    system_out = "System output"
    system_err = "System error"
    
    suite = TestSuite(
        name="test_suite",
        hostname="localhost",
        id="1",
        package="test_package",
        timestamp=timestamp,
        properties=properties,
        cases=cases,
        system_out=system_out,
        system_err=system_err
    )
    
    # Assertions to verify the TestSuite instance
    assert suite.name == "test_suite"
    assert suite.hostname == "localhost"
    assert suite.id == "1"
    assert suite.package == "test_package"
    assert suite.timestamp == timestamp
    assert suite.properties == properties
    assert suite.cases == cases
    assert suite.system_out == system_out
    assert suite.system_err == system_err

def test_testsuite_default_initialization():
    # Create a TestSuite instance with only the required field
    suite = TestSuite(name="default_test_suite")
    
    # Assertions to verify the default values
    assert suite.name == "default_test_suite"
    assert suite.hostname is None
    assert suite.id is None
    assert suite.package is None
    assert suite.timestamp is None
    assert suite.properties == {}
    assert suite.cases == []
    assert suite.system_out is None
    assert suite.system_err is None
