# file: lib/ansible/utils/_junit_xml.py:249-254
# asked: {"lines": [249, 251, 252, 254], "branches": []}
# gained: {"lines": [249, 251, 252, 254], "branches": []}

import pytest
from xml.etree import ElementTree as ET
from unittest.mock import MagicMock
from ansible.utils._junit_xml import TestSuites

@pytest.fixture
def mock_testsuite():
    mock_suite = MagicMock()
    mock_suite.get_xml_element.return_value = ET.Element('testsuite')
    return mock_suite

def test_get_xml_element(monkeypatch, mock_testsuite):
    # Mock the get_attributes method to return a sample dictionary
    monkeypatch.setattr(TestSuites, 'get_attributes', lambda self: {'name': 'sample'})

    # Create a TestSuites instance with the mock suite
    test_suites = TestSuites(suites=[mock_testsuite])

    # Call the method under test
    result = test_suites.get_xml_element()

    # Verify the result
    assert result.tag == 'testsuites'
    assert result.attrib == {'name': 'sample'}
    assert len(result) == 1
    assert result[0].tag == 'testsuite'
