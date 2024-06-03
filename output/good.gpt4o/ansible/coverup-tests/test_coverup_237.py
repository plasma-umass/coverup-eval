# file lib/ansible/utils/_junit_xml.py:109-125
# lines [109, 111, 113, 114, 116, 117, 119, 120, 122, 123, 125]
# branches ['113->114', '113->116', '119->120', '119->122', '122->123', '122->125']

import pytest
import xml.etree.ElementTree as ET
import dataclasses

# Assuming the TestCase class is defined in ansible.utils._junit_xml
from ansible.utils._junit_xml import TestCase

@pytest.fixture
def mock_test_case():
    @dataclasses.dataclass
    class MockError:
        def get_xml_element(self):
            return ET.Element('error')

    @dataclasses.dataclass
    class MockFailure:
        def get_xml_element(self):
            return ET.Element('failure')

    @dataclasses.dataclass
    class MockTestCase(TestCase):
        name: str
        skipped: str = None
        errors: list = dataclasses.field(default_factory=list)
        failures: list = dataclasses.field(default_factory=list)
        system_out: str = None
        system_err: str = None

        def get_attributes(self):
            return {'name': self.name}

    return MockTestCase(
        name="test_case_name",
        skipped="Test skipped",
        errors=[MockError()],
        failures=[MockFailure()],
        system_out="System out message",
        system_err="System err message"
    )

def test_get_xml_element(mock_test_case):
    element = mock_test_case.get_xml_element()
    
    assert element.tag == 'testcase'
    assert element.attrib['name'] == "test_case_name"
    assert element.find('skipped').text == "Test skipped"
    assert element.find('error') is not None
    assert element.find('failure') is not None
    assert element.find('system-out').text == "System out message"
    assert element.find('system-err').text == "System err message"
