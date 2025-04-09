# file: lib/ansible/utils/_junit_xml.py:256-258
# asked: {"lines": [258], "branches": []}
# gained: {"lines": [258], "branches": []}

import pytest
from xml.etree import ElementTree as ET
from ansible.utils._junit_xml import TestSuites

def test_to_pretty_xml(monkeypatch):
    # Mock the _pretty_xml function
    def mock_pretty_xml(element):
        return "<xml>pretty</xml>"

    monkeypatch.setattr("ansible.utils._junit_xml._pretty_xml", mock_pretty_xml)

    # Mock the get_xml_element method
    def mock_get_xml_element(self):
        return ET.Element("testsuites")

    monkeypatch.setattr(TestSuites, "get_xml_element", mock_get_xml_element)

    # Create an instance of TestSuites
    test_suites = TestSuites()

    # Call the to_pretty_xml method
    result = test_suites.to_pretty_xml()

    # Assert the result
    assert result == "<xml>pretty</xml>"
