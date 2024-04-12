# file lib/ansible/utils/_junit_xml.py:188-203
# lines [190, 192, 193, 195, 197, 198, 200, 201, 203]
# branches ['192->193', '192->195', '197->198', '197->200', '200->201', '200->203']

import pytest
import xml.etree.ElementTree as ET
from ansible.utils._junit_xml import TestSuite

def test_get_xml_element_with_properties_system_out_and_err():
    # Setup the TestSuite with properties, system_out, and system_err
    test_suite = TestSuite(
        name="test_suite",
        properties={"key1": "value1", "key2": "value2"},
        system_out="System Out Message",
        system_err="System Err Message",
        cases=[]
    )

    # Call the method under test
    xml_element = test_suite.get_xml_element()

    # Assertions to verify the XML structure
    assert xml_element.tag == "testsuite"
    assert xml_element.find("properties") is not None
    assert len(xml_element.find("properties")) == 2  # Two properties were added
    assert xml_element.find("system-out") is not None
    assert xml_element.find("system-out").text == "System Out Message"
    assert xml_element.find("system-err") is not None
    assert xml_element.find("system-err").text == "System Err Message"

    # Clean up (no persistent state, so nothing to clean up in this case)
