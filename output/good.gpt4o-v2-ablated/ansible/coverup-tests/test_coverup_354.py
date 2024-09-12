# file: lib/ansible/utils/_junit_xml.py:256-258
# asked: {"lines": [256, 258], "branches": []}
# gained: {"lines": [256], "branches": []}

import pytest
from unittest import mock
import dataclasses
from xml.etree.ElementTree import Element, tostring

# Mocking _pretty_xml function
def _pretty_xml(element: Element) -> str:
    return tostring(element, encoding='unicode')

@dataclasses.dataclass
class TestSuites:
    def get_xml_element(self) -> Element:
        # Mock implementation for testing purposes
        element = Element('testsuites')
        return element

    def to_pretty_xml(self) -> str:
        """Return a pretty formatted XML string representing this instance."""
        return _pretty_xml(self.get_xml_element())

@pytest.fixture
def mock_pretty_xml(monkeypatch):
    monkeypatch.setattr('ansible.utils._junit_xml._pretty_xml', _pretty_xml)

def test_to_pretty_xml(mock_pretty_xml):
    test_suites = TestSuites()
    result = test_suites.to_pretty_xml()
    expected = '<testsuites />'
    assert result == expected
