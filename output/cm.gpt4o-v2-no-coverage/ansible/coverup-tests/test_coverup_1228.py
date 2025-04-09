# file: lib/ansible/utils/_junit_xml.py:266-268
# asked: {"lines": [268], "branches": []}
# gained: {"lines": [268], "branches": []}

import pytest
from xml.etree import ElementTree as ET
from xml.dom import minidom
from ansible.utils._junit_xml import _pretty_xml

def test_pretty_xml():
    # Create a simple XML element
    element = ET.Element('root')
    child = ET.SubElement(element, 'child')
    child.text = 'This is a test'

    # Call the function
    pretty_xml = _pretty_xml(element)

    # Verify the output
    assert isinstance(pretty_xml, str)
    assert '<root>' in pretty_xml
    assert '<child>' in pretty_xml
    assert 'This is a test' in pretty_xml

    # Clean up
    del element
    del child
    del pretty_xml
