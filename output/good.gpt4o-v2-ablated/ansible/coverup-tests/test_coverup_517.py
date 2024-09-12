# file: lib/ansible/utils/_junit_xml.py:256-258
# asked: {"lines": [258], "branches": []}
# gained: {"lines": [258], "branches": []}

import pytest
from unittest import mock
import dataclasses
from ansible.utils._junit_xml import TestSuites

@pytest.fixture
def mock_pretty_xml(monkeypatch):
    mock_pretty = mock.Mock(return_value="<xml></xml>")
    monkeypatch.setattr("ansible.utils._junit_xml._pretty_xml", mock_pretty)
    return mock_pretty

@pytest.fixture
def mock_get_xml_element(monkeypatch):
    mock_element = mock.Mock(return_value="<element></element>")
    monkeypatch.setattr(TestSuites, "get_xml_element", mock_element)
    return mock_element

def test_to_pretty_xml(mock_pretty_xml, mock_get_xml_element):
    test_suites = TestSuites()
    result = test_suites.to_pretty_xml()
    
    mock_get_xml_element.assert_called_once()
    mock_pretty_xml.assert_called_once_with("<element></element>")
    assert result == "<xml></xml>"
