# file: lib/ansible/utils/_junit_xml.py:266-268
# asked: {"lines": [266, 268], "branches": []}
# gained: {"lines": [266, 268], "branches": []}

import pytest
import xml.etree.ElementTree as ET
from xml.dom import minidom
from ansible.utils._junit_xml import _pretty_xml

def test_pretty_xml(monkeypatch):
    # Create a simple XML element
    element = ET.Element("root")
    child = ET.SubElement(element, "child")
    child.text = "content"

    # Expected pretty XML string
    expected_xml = minidom.parseString(ET.tostring(element, encoding='unicode')).toprettyxml()

    # Call the function and assert the result
    result = _pretty_xml(element)
    assert result == expected_xml

    # Clean up any state if necessary (not needed in this case)
