# file: lib/ansible/utils/_junit_xml.py:266-268
# asked: {"lines": [266, 268], "branches": []}
# gained: {"lines": [266, 268], "branches": []}

import pytest
from xml.etree import ElementTree as ET
from xml.dom import minidom

# Assuming the _pretty_xml function is imported from the module
from ansible.utils._junit_xml import _pretty_xml

def test_pretty_xml():
    # Create a simple XML element
    element = ET.Element("root")
    child = ET.SubElement(element, "child")
    child.text = "some text"

    # Call the function
    pretty_xml = _pretty_xml(element)

    # Parse the result back to an XML document to verify its structure
    parsed_xml = minidom.parseString(pretty_xml)

    # Assertions to verify the output
    assert parsed_xml.documentElement.tagName == "root"
    assert parsed_xml.documentElement.getElementsByTagName("child")[0].firstChild.nodeValue.strip() == "some text"

    # Clean up
    del element
    del child
    del pretty_xml
    del parsed_xml
