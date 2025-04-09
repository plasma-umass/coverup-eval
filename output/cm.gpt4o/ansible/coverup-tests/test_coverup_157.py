# file lib/ansible/utils/_junit_xml.py:18-46
# lines [18, 19, 20, 21, 22, 23, 25, 26, 27, 29, 30, 31, 34, 36, 37, 38, 41, 43, 44, 46]
# branches ['26->exit', '26->27']

import pytest
import xml.etree.ElementTree as ET
from unittest import mock
from ansible.utils._junit_xml import TestResult

def test_testresult_post_init():
    class ConcreteTestResult(TestResult):
        @property
        def tag(self) -> str:
            return "concrete"

    result = ConcreteTestResult()
    assert result.type == "concrete"

def test_testresult_get_attributes():
    class ConcreteTestResult(TestResult):
        @property
        def tag(self) -> str:
            return "concrete"

    result = ConcreteTestResult(message="test message", type="test type")
    attributes = result.get_attributes()
    assert attributes == {"message": "test message", "type": "test type"}

def test_testresult_get_xml_element():
    class ConcreteTestResult(TestResult):
        @property
        def tag(self) -> str:
            return "concrete"

    result = ConcreteTestResult(output="test output", message="test message", type="test type")
    element = result.get_xml_element()
    assert element.tag == "concrete"
    assert element.attrib == {"message": "test message", "type": "test type"}
    assert element.text == "test output"
