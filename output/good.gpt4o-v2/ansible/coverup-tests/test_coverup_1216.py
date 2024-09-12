# file: lib/ansible/utils/_junit_xml.py:109-125
# asked: {"lines": [114, 120, 123], "branches": [[113, 114], [119, 120], [122, 123]]}
# gained: {"lines": [114, 120, 123], "branches": [[113, 114], [119, 120], [122, 123]]}

import pytest
from xml.etree import ElementTree as ET
from ansible.utils._junit_xml import TestCase, TestError, TestFailure

def test_get_xml_element_with_skipped():
    test_case = TestCase(
        name="test_case",
        skipped="Test was skipped",
        errors=[],
        failures=[]
    )
    element = test_case.get_xml_element()
    skipped_element = element.find('skipped')
    assert skipped_element is not None
    assert skipped_element.text == "Test was skipped"

def test_get_xml_element_with_system_out():
    test_case = TestCase(
        name="test_case",
        system_out="System out message",
        errors=[],
        failures=[]
    )
    element = test_case.get_xml_element()
    system_out_element = element.find('system-out')
    assert system_out_element is not None
    assert system_out_element.text == "System out message"

def test_get_xml_element_with_system_err():
    test_case = TestCase(
        name="test_case",
        system_err="System error message",
        errors=[],
        failures=[]
    )
    element = test_case.get_xml_element()
    system_err_element = element.find('system-err')
    assert system_err_element is not None
    assert system_err_element.text == "System error message"
