# file: apimd/parser.py:31-33
# asked: {"lines": [31, 33], "branches": []}
# gained: {"lines": [31, 33], "branches": []}

import pytest
from apimd.parser import _m

def test_m_with_single_name():
    result = _m("module1")
    assert result == "module1"

def test_m_with_multiple_names():
    result = _m("module1", "module2", "module3")
    assert result == "module1.module2.module3"

def test_m_with_empty_string():
    result = _m("module1", "", "module3")
    assert result == "module1.module3"

def test_m_with_all_empty_strings():
    result = _m("", "", "")
    assert result == ""
