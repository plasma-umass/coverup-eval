# file lib/ansible/utils/_junit_xml.py:266-268
# lines [266, 268]
# branches []

import pytest
import xml.etree.ElementTree as ET
from ansible.utils._junit_xml import _pretty_xml

def test_pretty_xml():
    # Create a simple XML element
    element = ET.Element('testcase')
    element.set('name', 'test1')
    child = ET.SubElement(element, 'failure')
    child.text = 'This is a failure message.'

    # Call the function to be tested
    pretty_xml_str = _pretty_xml(element)

    # Assertions to verify the postconditions
    assert '<testcase name="test1">' in pretty_xml_str
    assert '<failure>' in pretty_xml_str
    assert 'This is a failure message.' in pretty_xml_str
    assert pretty_xml_str.startswith('<?xml version="1.0" ?>\n')
    assert '</testcase>' in pretty_xml_str

    # No cleanup is necessary as the test does not create any persistent resources
