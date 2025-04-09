# file: lib/ansible/utils/_junit_xml.py:266-268
# asked: {"lines": [268], "branches": []}
# gained: {"lines": [268], "branches": []}

import pytest
from xml.etree import ElementTree as ET
from ansible.utils._junit_xml import _pretty_xml

def test_pretty_xml():
    # Create a simple XML element
    element = ET.Element("root")
    child = ET.SubElement(element, "child")
    child.text = "This is a test"

    # Call the function
    pretty_xml = _pretty_xml(element)

    # Assert the output is a pretty formatted XML string
    assert pretty_xml.startswith('<?xml version="1.0" ?>')
    assert "<root>" in pretty_xml
    assert "<child>This is a test</child>" in pretty_xml
    assert "</root>" in pretty_xml
