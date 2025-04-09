# file: apimd/parser.py:31-33
# asked: {"lines": [31, 33], "branches": []}
# gained: {"lines": [31, 33], "branches": []}

import pytest

from apimd.parser import _m

def test_m_with_non_empty_strings():
    result = _m('module', 'submodule', 'subsubmodule')
    assert result == 'module.submodule.subsubmodule'

def test_m_with_some_empty_strings():
    result = _m('module', '', 'submodule', '', 'subsubmodule')
    assert result == 'module.submodule.subsubmodule'

def test_m_with_all_empty_strings():
    result = _m('', '', '')
    assert result == ''

def test_m_with_no_arguments():
    result = _m()
    assert result == ''
