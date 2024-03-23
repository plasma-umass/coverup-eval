# file lib/ansible/utils/_junit_xml.py:256-258
# lines [256, 258]
# branches []

import pytest
from ansible.utils._junit_xml import TestSuites
from xml.etree.ElementTree import Element

# Mocking the get_xml_element method to return a simple XML Element
@pytest.fixture
def mock_get_xml_element(mocker):
    def _mock_get_xml_element(self):
        element = Element('testsuites')
        child = Element('testsuite')
        child.text = 'Test Suite'
        element.append(child)
        return element

    mocker.patch.object(TestSuites, 'get_xml_element', _mock_get_xml_element)

# Test function to improve coverage
def test_to_pretty_xml(mock_get_xml_element):
    test_suites = TestSuites()
    pretty_xml = test_suites.to_pretty_xml()
    assert pretty_xml.startswith('<?xml version="1.0" ?>\n<testsuites>')
    assert '<testsuite>Test Suite</testsuite>' in pretty_xml
    assert pretty_xml.endswith('</testsuites>\n')
