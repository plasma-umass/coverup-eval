# file: lib/ansible/utils/_junit_xml.py:266-268
# asked: {"lines": [266, 268], "branches": []}
# gained: {"lines": [266, 268], "branches": []}

import pytest
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Assuming the function _pretty_xml is defined in ansible/utils/_junit_xml.py
from ansible.utils._junit_xml import _pretty_xml

def test_pretty_xml(monkeypatch):
    # Create a simple XML element
    element = ET.Element("root")
    child = ET.SubElement(element, "child")
    child.text = "This is a test"

    # Call the function to test
    pretty_xml = _pretty_xml(element)

    # Assert that the output is a pretty formatted XML string
    assert pretty_xml.startswith('<?xml version="1.0" ?>')
    assert '<root>' in pretty_xml
    assert '<child>This is a test</child>' in pretty_xml
    assert '</root>' in pretty_xml

    # Clean up any state if necessary (not needed in this case as no state is modified)

