# file: lib/ansible/utils/_junit_xml.py:249-254
# asked: {"lines": [249, 251, 252, 254], "branches": []}
# gained: {"lines": [249, 251, 252, 254], "branches": []}

import pytest
from xml.etree import ElementTree as ET
from unittest.mock import MagicMock

# Assuming the TestSuites class and its dependencies are defined in ansible.utils._junit_xml
from ansible.utils._junit_xml import TestSuites, TestSuite

@pytest.fixture
def mock_testsuites(monkeypatch):
    # Mock the get_attributes method
    monkeypatch.setattr(TestSuites, "get_attributes", lambda self: {"name": "mocked_name"})
    
    # Create a mock suite with a get_xml_element method
    mock_suite = MagicMock(spec=TestSuite)
    mock_suite.get_xml_element.return_value = ET.Element("testsuite")
    
    # Create an instance of TestSuites with the mock suite
    testsuites = TestSuites(suites=[mock_suite])
    
    return testsuites

def test_get_xml_element(mock_testsuites):
    element = mock_testsuites.get_xml_element()
    
    # Assertions to verify the element structure
    assert element.tag == "testsuites"
    assert element.attrib == {"name": "mocked_name"}
    assert len(element) == 1
    assert element[0].tag == "testsuite"
