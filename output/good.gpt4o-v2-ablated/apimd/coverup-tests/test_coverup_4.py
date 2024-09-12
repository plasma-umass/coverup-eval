# file: apimd/parser.py:31-33
# asked: {"lines": [31, 33], "branches": []}
# gained: {"lines": [31, 33], "branches": []}

import pytest

from apimd.parser import _m

def test_m_with_no_names():
    assert _m() == ""

def test_m_with_single_name():
    assert _m("module") == "module"

def test_m_with_multiple_names():
    assert _m("module", "submodule") == "module.submodule"

def test_m_with_empty_and_non_empty_names():
    assert _m("module", "", "submodule") == "module.submodule"

def test_m_with_all_empty_names():
    assert _m("", "", "") == ""
