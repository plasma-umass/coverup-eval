# file lib/ansible/utils/_junit_xml.py:266-268
# lines [266, 268]
# branches []

import pytest
import xml.etree.ElementTree as ET
from xml.dom import minidom
from ansible.utils._junit_xml import _pretty_xml

def test_pretty_xml():
    # Create a sample XML element
    element = ET.Element('root')
    child = ET.SubElement(element, 'child')
    child.text = 'sample text'

    # Call the function to test
    pretty_xml = _pretty_xml(element)

    # Verify the output is a pretty formatted XML string
    assert pretty_xml.startswith('<?xml version="1.0" ?>')
    assert '<root>' in pretty_xml
    assert '<child>sample text</child>' in pretty_xml
    assert '</root>' in pretty_xml

    # Clean up: No specific cleanup required as no external resources are used
